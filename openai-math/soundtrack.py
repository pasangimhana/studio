#!/usr/bin/env python3
"""Synthesises the soundtrack for index.html from scratch (numpy only), locked to the same CUES the animation uses.

usage: python3 soundtrack.py out.wav
"""
import json
import re
import sys
import wave
from pathlib import Path

import numpy as np

SR = 44100
HERE = Path(__file__).resolve().parent
CUES = json.loads(re.search(r"const CUES = (\{.*?\});", (HERE / "index.html").read_text()).group(1))
DUR = CUES["dur"]
N = int(DUR * SR)
rng = np.random.default_rng(722)

# ---------------------------------------------------------------- helpers
def midi(m):
    return 440.0 * 2 ** ((m - 69) / 12)

def tt(sec):
    return np.arange(int(sec * SR)) / SR

def noise(sec):
    return rng.standard_normal(int(sec * SR))

def spectral(x, fn):
    """Zero-phase filter: multiply the spectrum by fn(freqs)."""
    n = len(x)
    X = np.fft.rfft(x, n)
    return np.fft.irfft(X * fn(np.fft.rfftfreq(n, 1 / SR)), n)

def lp(x, fc, order=2):
    return spectral(x, lambda f: 1 / np.sqrt(1 + (f / fc) ** (2 * order)))

def hp(x, fc, order=2):
    return spectral(x, lambda f: 1 / np.sqrt(1 + (fc / np.maximum(f, 1e-3)) ** (2 * order)))

def bp(x, lo, hi):
    return hp(lp(x, hi), lo)

def sweep_noise(sec, f0, f1, q=1.6, shape=None):
    """Noise through a band-pass whose centre glides f0 -> f1 (or follows shape(u)), via windowed overlap-add."""
    n = int(sec * SR)
    hop, win = 1024, 2048
    src = rng.standard_normal(n + win)
    out = np.zeros(n + win)
    w = np.hanning(win)
    freqs = np.fft.rfftfreq(win, 1 / SR)
    for start in range(0, n, hop):
        u = start / max(1, n)
        fc = shape(u) if shape else f0 * (f1 / f0) ** u
        band = np.exp(-0.5 * (np.log2(np.maximum(freqs, 1) / fc) * q) ** 2)
        seg = np.fft.irfft(np.fft.rfft(src[start:start + win] * w) * band, win)
        out[start:start + win] += seg
    out = out[:n]
    return out / (np.abs(out).max() + 1e-9)

class Bus:
    def __init__(self):
        self.x = np.zeros((2, N), dtype=np.float64)

    def add(self, t0, sig, gain=1.0, pan=0.0):
        i0 = int(round(t0 * SR))
        if i0 >= N:
            return
        if sig.ndim == 1:
            a = (pan + 1) * np.pi / 4
            sig = np.stack([sig * np.cos(a), sig * np.sin(a)]) * np.sqrt(2)
        j0, j1 = max(0, i0), min(N, i0 + sig.shape[1])
        if j1 > j0:
            self.x[:, j0:j1] += gain * sig[:, j0 - i0:j1 - i0]

drums, bass, pad, keys, fx = Bus(), Bus(), Bus(), Bus(), Bus()

# ---------------------------------------------------------------- harmony
CHORDS = {
    "Am": ([57, 60, 64, 69], 33), "F": ([53, 57, 60, 65], 29), "C": ([55, 60, 64, 67], 36),
    "G": ([55, 59, 62, 67], 31), "Gsus": ([55, 60, 62, 67], 31), "Am9": ([57, 60, 64, 71, 76], 33),
}
PROG = ["Am", "F", "C", "G"]
# (start, end, seconds per chord or a fixed chord name)
SECTIONS = [(0, 15, 4), (15, 19, 2), (19, 41, 2), (41, 51, 2), (51, 59, 2), (59, 71, 2), (71, 75, "Gsus"), (75, 93, 2), (93, 108, 4), (108, DUR, "Am9")]

def chord_spans():
    spans = []
    for a, b, d in SECTIONS:
        if isinstance(d, str):
            spans.append((a, b, d))
            continue
        k, t = 0, a
        while t < b - 1e-6:
            spans.append((t, min(b, t + d), PROG[k % 4]))
            t += d
            k += 1
    return spans

SPANS = chord_spans()

def chord_at(t):
    for a, b, c in SPANS:
        if a <= t < b:
            return c
    return "Am"

# ---------------------------------------------------------------- instruments
def pad_tone(freq, sec, bright=1.0):
    t = tt(sec)
    out = np.zeros((2, len(t)))
    for ch, det in ((0, -0.004), (1, 0.004)):
        f = freq * (1 + det)
        for h in range(1, 8):
            out[ch] += np.sin(2 * np.pi * f * h * t + h * 0.7 + ch) / h ** (1.9 - 0.5 * bright)
    return out

def env(sec, atk, rel):
    n = int(sec * SR)
    e = np.ones(n)
    a, r = int(atk * SR), int(rel * SR)
    if a:
        e[:a] = np.linspace(0, 1, a) ** 2
    if r:
        e[-r:] *= np.linspace(1, 0, r) ** 2
    return e

def kick(vel=1.0):
    t = tt(0.5)
    f = 46 + 120 * np.exp(-t / 0.032)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.3)
    click = hp(noise(0.5), 2500) * np.exp(-t / 0.004) * 0.25
    return np.tanh(1.6 * (body + click)) * vel

def snare(vel=1.0):
    t = tt(0.32)
    tone = np.sin(2 * np.pi * 185 * t) * np.exp(-t / 0.05) * 0.5
    nz = bp(noise(0.32), 900, 7000) * np.exp(-t / 0.11)
    return (tone + nz / (np.abs(nz).max() + 1e-9)) * 0.7 * vel

def hat(vel=1.0, open_=False):
    sec = 0.32 if open_ else 0.08
    t = tt(sec)
    nz = hp(noise(sec), 7000)
    return nz / (np.abs(nz).max() + 1e-9) * np.exp(-t / (0.11 if open_ else 0.022)) * vel

def pluck(m, sec=0.9, decay=0.35, bright=1.0):
    t = tt(sec)
    f = midi(m)
    mod = np.sin(2 * np.pi * f * 2 * t) * 1.4 * bright * np.exp(-t / 0.08)
    s = np.sin(2 * np.pi * f * t + mod) + 0.25 * np.sin(2 * np.pi * f * 3 * t) * np.exp(-t / 0.05)
    return s * np.exp(-t / decay) * np.minimum(1, t / 0.002)

def bass_note(m, sec, vel=1.0):
    t = tt(sec)
    f = midi(m)
    s = np.sin(2 * np.pi * f * t) + 0.35 * np.sin(2 * np.pi * 2 * f * t) + 0.12 * np.sin(2 * np.pi * 3 * f * t)
    return np.tanh(1.3 * s) * np.minimum(1, t / 0.004) * np.exp(-t / (sec * 0.45)) * vel

def impact(k):
    t = tt(3.0)
    f = 34 + 70 * np.exp(-t / 0.07)
    boom = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.75)
    crack = lp(noise(3.0), 4000) * np.exp(-t / 0.05) * 0.18
    tail = lp(noise(3.0), 900) * np.exp(-t / 0.5) * 0.05
    return np.tanh(1.4 * (boom + crack + tail)) * k

# ---------------------------------------------------------------- pad + sub drone
for a, b, c in SPANS:
    notes, root = CHORDS[c]
    sec = (b - a) + 0.9
    e = env(sec, 0.35 if a > 0 else 0.8, 0.9)
    bright = 1.4 if 75 <= a < 93 else 1.0
    sig = sum(pad_tone(midi(m), sec, bright) for m in notes) * e
    # quiet intro and reflection, fuller once the beat is in
    gain = 0.022 if a < 15 else 0.03 if a < 19 else 0.032 if a >= 93 else 0.04
    if a >= 108:
        sec = DUR - a + 0.1
        e = env(sec, 0.05, 4.5)
        sig = sum(pad_tone(midi(m), sec, 1.1) for m in notes) * e
        gain = 0.045
    pad.add(a, sig, gain)
    # sub drone outside the beat sections
    if a < 19 or a >= 93 or 71 <= a < 75:
        s = np.sin(2 * np.pi * midi(root + 12) * tt(sec)) * e
        bass.add(a, s, 0.1 if 71 <= a < 75 else 0.06)
pad.x = np.stack([lp(ch, 2600) for ch in pad.x])

# ---------------------------------------------------------------- drums + bass line
kick_times = []
for a, b, level in CUES["drums"]:
    nb = int(round((b - a) / 0.5))
    for i in range(nb):
        t = a + i * 0.5
        if level == 3:
            # the build: kicks on quarters, a snare roll that doubles its rate each second
            drums.add(t, kick(0.75), 0.55)
            kick_times.append(t)
            continue
        lv = 1.0 if level == 2 else 0.8  # leave headroom so the drop hits harder
        drums.add(t, kick(), 0.62 * lv)
        kick_times.append(t)
        if i % 2 == 1:
            drums.add(t, snare(), 0.32 * lv, 0.05)
        drums.add(t + 0.25, hat(0.8, open_=(level == 2)), 0.13 if level == 2 else 0.16, 0.3)
        if level == 2:
            for s16 in (0.125, 0.375):
                drums.add(t + s16, hat(0.45), 0.09, -0.3)
        # offbeat bass
        root = CHORDS[chord_at(t + 0.25)][1]
        bass.add(t + 0.25, bass_note(root + 12, 0.24, 1.0), 0.3 * lv)
        if level == 2:
            bass.add(t, np.sin(2 * np.pi * midi(root) * tt(0.5)) * env(0.5, 0.01, 0.1), 0.2)
# snare roll in the build
for a, b, level in CUES["drums"]:
    if level != 3:
        continue
    t = a
    while t < b - 1e-6:
        u = (t - a) / (b - a)
        rate = 0.25 if u < 0.25 else 0.125 if u < 0.5 else 0.0625 if u < 0.85 else 0.03125
        drums.add(t, snare(0.35 + 0.65 * u), 0.3, (u - 0.5) * 0.4)
        t += rate

# sidechain: duck pad and bass after each kick
duck = np.ones(N)
tn = np.arange(int(0.35 * SR)) / SR
shape = 1 - 0.55 * np.exp(-tn / 0.11)
for kt in kick_times:
    i0 = int(kt * SR)
    j = min(N, i0 + len(shape))
    duck[i0:j] = np.minimum(duck[i0:j], shape[:j - i0])
pad.x *= duck
bass.x *= duck

# ---------------------------------------------------------------- arps
def arp(a, b, step, decay, gain, octave, bright):
    t, k = a, 0
    pattern = [0, 1, 2, 3, 2, 1]
    while t < b - 1e-6:
        notes = CHORDS[chord_at(t)][0]
        m = notes[pattern[k % len(pattern)] % len(notes)] + octave
        keys.add(t, pluck(m, decay * 3, decay, bright), gain, 0.35 * np.sin(k * 1.3))
        t += step
        k += 1

arp(75, 93, 0.125, 0.12, 0.05, 12, 1.0)
arp(93, 107.5, 0.25, 0.45, 0.07, 12, 0.6)

# ---------------------------------------------------------------- one-shots
PENTA = [69, 72, 74, 76, 79, 81, 84, 86, 88, 91, 93]
for i, t in enumerate(CUES["blip"]):
    keys.add(t, pluck(PENTA[i], 1.6, 0.6), 0.18, 0.25 * (-1) ** i)
    keys.add(t, pluck(PENTA[i] + 12, 1.2, 0.35, 0.5), 0.06, -0.25 * (-1) ** i)
for i, t in enumerate(CUES["ticks"]):
    keys.add(t, pluck(PENTA[i], 0.6, 0.18), 0.16, -0.6 + i * 0.13)
for i, t in enumerate(CUES["pops"]):
    keys.add(t, pluck(PENTA[(i + 3) % len(PENTA)], 0.7, 0.22), 0.15, 0.3 * (-1) ** i)
    fx.add(t, hp(noise(0.03), 4000) * np.exp(-tt(0.03) / 0.006), 0.05)
# final chord, struck
for j, m in enumerate(CHORDS["Am9"][0]):
    keys.add(CUES["end"] + j * 0.06, pluck(m + 12, 5.5, 1.6, 0.4), 0.09, -0.4 + j * 0.2)

# typing clicks
a, b = CUES["type"]
t = a
while t < b:
    c = hp(noise(0.012), 3000) * np.exp(-tt(0.012) / 0.0025)
    c += np.sin(2 * np.pi * (1500 + rng.random() * 600) * tt(0.012)) * np.exp(-tt(0.012) / 0.003) * 0.4
    fx.add(t, c, 0.05 + rng.random() * 0.04, rng.random() * 0.6 - 0.3)
    t += 0.055 + rng.random() * 0.045

# chalk-like scribble when an equation writes itself on
for t in CUES["write"]:
    sec = 1.3
    nz = bp(noise(sec), 2200, 7500)
    am = (0.5 + 0.5 * np.sin(2 * np.pi * 9 * tt(sec) + rng.random() * 6)) ** 3
    fx.add(t, nz / np.abs(nz).max() * am * env(sec, 0.05, 0.4), 0.05)

for t in CUES["whoosh"]:
    sec = 0.9
    w = sweep_noise(sec, 300, 300, q=1.2, shape=lambda u: 300 * 12 ** np.sin(np.pi * u))
    w *= np.sin(np.pi * np.linspace(0, 1, len(w))) ** 2
    fx.add(t - 0.45, np.stack([w, np.roll(w, 300)]), 0.2)

for a, b in CUES["riser"]:
    sec = b - a
    r = sweep_noise(sec, 250, 7000, q=1.0) * np.linspace(0, 1, int(sec * SR)) ** 2.2
    tone = np.sin(2 * np.pi * np.cumsum(220 * 4 ** np.linspace(0, 1, int(sec * SR))) / SR) * np.linspace(0, 1, int(sec * SR)) ** 3
    fx.add(a, np.stack([r, np.roll(r, 400)]), 0.22)
    fx.add(a, tone, 0.05)

for t, k in CUES["impact"]:
    fx.add(t, impact(k), 0.55)

# ---------------------------------------------------------------- reverb + master
def reverb(x, seconds=2.6, predelay=0.02):
    n = int(seconds * SR)
    t = np.arange(n) / SR
    ir = np.zeros((2, n + int(predelay * SR)))
    for ch in range(2):
        ir[ch, int(predelay * SR):] = lp(rng.standard_normal(n), 5000) * np.exp(-t / 0.75)
    ir /= np.sqrt((ir ** 2).sum(axis=1, keepdims=True))
    size = 1 << int(np.ceil(np.log2(x.shape[1] + ir.shape[1])))
    out = np.zeros_like(x)
    for ch in range(2):
        out[ch] = np.fft.irfft(np.fft.rfft(x[ch], size) * np.fft.rfft(ir[ch], size), size)[:x.shape[1]]
    return out

send = pad.x * 0.35 + keys.x * 0.6 + fx.x * 0.25 + drums.x * 0.06
wet = reverb(send)
mix = drums.x + bass.x + pad.x + keys.x + fx.x + wet * 0.45
mix = np.stack([hp(ch, 28) for ch in mix])

# master fades match the picture
fade = np.ones(N)
fade[:int(0.6 * SR)] = np.linspace(0, 1, int(0.6 * SR))
fade[-int(0.9 * SR):] = np.linspace(1, 0, int(0.9 * SR)) ** 1.5
mix *= fade

mix /= np.abs(mix).max() + 1e-9
mix = np.tanh(1.5 * mix) / np.tanh(1.5)
mix *= 0.72 / (np.abs(mix).max() + 1e-9)  # lands near -14 LUFS integrated

out = sys.argv[1] if len(sys.argv) > 1 else str(HERE / "soundtrack.wav")
pcm = (mix.T * 32767).astype("<i2")
with wave.open(out, "wb") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print("wrote", out, f"{DUR}s", "rms", round(float(np.sqrt((mix ** 2).mean())), 3))
