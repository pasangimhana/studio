# Open-Source Kernels, Not Olympiads, Carried Nathan Chen

Chen Guangyu (陈广宇, "Nathan Chen", @nathancgy4) is real, and the core of his record holds up. He joined Moonshot AI's Kimi team in November 2025 at 16. He is listed first of three equal-contribution co-first authors on "Attention Residuals". He co-designed Block AttnRes, which became one of Kimi K3's two headline architecture components. On 15 October 2026 he announced that he had left Kimi, without saying where he was going. No credential got him there. A public trail did: GPU-kernel tutorials in Triton and TileLang, a merged DeltaFormer model of roughly 1,900 lines in the flash-linear-attention (FLA) repo co-authored with a future Kimi colleague, a seven-week internship at the startup Tilde Research, and mentors who opened doors at the right moments. Two parts of your premise need correcting. He has no olympiad medals, but he spent two and a half years climbing to **Codeforces Candidate Master (peak rating 2026)** before he started ML. And his focused ML phase lasted only **about nine months** before Moonshot hired him. That is fast, but it sat on top of years of serious coding. The viral @NFT_Chen post gets his résumé mostly right and his ending wrong. No reputable outlet, Anthropic statement or post of his own confirms an Anthropic "Scaling RL" role. "Poached by Dario within 24 hours" has no support. The screenshotted Sholto Douglas reply reads as an invitation plus a question about his university plans, not a welcome aboard. The method he used can be copied over an estimated 12–24 months of near-full-time work: learn in public, ship code into the open-source project a lab depends on, and take a stepping-stone internship. Reaching the same result at his age and speed also took mentors, timing and senior collaborators, and no roadmap can guarantee those.

## Two papers, four merged pull requests and a kernel blog make up the verified record

His professional identity is consistent across platforms, which makes the facts checkable:

- **Homepage.** nathanchen.me describes "ml research at kimi (moonshot)" on "llm scaling & pretraining (e.g., kimi k3)", after earlier "applied interp research at Tilde Research" ([nathanchen.me](https://nathanchen.me/)).
- **GitHub (Nathancgy).** Lists Kimi as his company, pins MoonshotAI/Attention-Residuals and fla-org/flash-linear-attention, and links to his X account and to the Codeforces handle **Nathan4** ([GitHub](https://github.com/Nathancgy)).
- **Google Scholar.** Lists exactly two papers ([Google Scholar](https://scholar.google.com/citations?hl=en&user=I35qZvMAAAAJ)).

Be careful with name collisions. Search results mix him up with the Olympic figure skater Nathan Chen, with dozens of robotics, translation and speech papers by other researchers named "Guangyu Chen", and with a different "Guanduo Chen" who appears on the same AttnRes author list ([arXiv](https://arxiv.org/abs/2603.15031)). Any long publication list attributed to him is almost certainly a merged profile.

The publication record has few entries but high impact:

- **"Attention Residuals"** (arXiv 2603.15031, 16 March 2026, 37 named authors). It lists him first among three equal-contribution authors, with Yu Zhang and Jianlin Su. The paper states that authors appear "in order of the significance of their contributions, with those in project leadership roles appearing last" ([arXiv PDF](https://arxiv.org/pdf/2603.15031)).
- **The Kimi K3 technical report** (arXiv 2607.24653). He is one of roughly 400 contributors, listed alphabetically with no roles ([arXiv](https://arxiv.org/abs/2607.24653)).
- **Not on earlier Kimi papers.** A name check against arXiv author lists found him absent from Kimi Linear, K2, K2.5, Kimi-VL and k1.5 ([arXiv API](https://export.arxiv.org/api/query?search_query=au:%22Guangyu%20Chen%22&max_results=80&sortBy=submittedDate&sortOrder=descending)).

Everything else is blog posts and code. **MoMoE**, a memory-optimized mixture-of-experts implementation with fused Triton kernels, credits "Nathan Chen" among its Tilde authors. SonicMoE, an ICLR 2026 paper from Tri Dao, Ion Stoica and colleagues, cites it as prior work ([SonicMoE](https://arxiv.org/html/2512.14080)). His **Co-ALIBI** repository contains forward and backward Triton kernels for a contextual-attention variant and claims about 180 TFLOPS forward on an H100 ([Co-ALIBI](https://github.com/Nathancgy/Co-ALIBI)). He has also written kernel tutorials and an optimizer derivation ([blog index](https://nathanchen.me/public/blog.html)).

What he contributed to Attention Residuals is the part the viral framing gets wrong. The paper replaces the fixed, unit-weight residual sum of a Transformer with softmax attention over earlier layers' outputs. Each layer gets one learned "pseudo-query" vector, so it can choose which earlier representations to draw on ([arXiv PDF](https://arxiv.org/pdf/2603.15031)). Media accounts drawn from Su Jianlin say **Su originated the idea and built the first version**. Chen and Zhang Yu then validated it at larger scale and co-proposed **Block AttnRes**, which groups layers into blocks to cut memory and communication cost ([36Kr](https://eu.36kr.com/zh/p/3737678705967369); [经济参考报](https://www.jjckb.cn/20260725/f1f27b8b4f9c40f3a4aa344a29e132bd/c.html)). Block AttnRes is the version that could ship. It matches a baseline trained with **1.25x more compute** and adds **under 2% inference latency**. It was validated on a 48B-total, 3B-active MoE trained on roughly 1.4T tokens, where GPQA-Diamond rose from 36.9 to 44.4 ([AttnRes README](https://github.com/MoonshotAI/Attention-Residuals)).

His role, in other words, was making the idea work at frontier scale, through systems design plus scaling experiments, and that is the skill labs hire for. He has pushed back on the hype himself: "不要造神" ("don't make a god out of me"). He credits his co-first authors and the infra team as each "indispensable" ([InfoQ](https://www.infoq.cn/article/CI5daAFmzhA1IWN2Z6zD)). K3 itself is a 2.8T-parameter MoE with 104B active parameters, "built on Kimi Delta Attention and Attention Residuals" ([arXiv](https://arxiv.org/abs/2607.24653)). His Kimi work also reportedly included speeding up the Kimi Delta Attention (KDA) GPU kernels with Zhang Yu, optimizer research and K3 launch demos ([BlockBeats](https://www.theblockbeats.info/flash/371927)). Two December 2025 FLA commits are the public trace of the kernel work: "[KDA] Changed all exp to exp2" and a fused backward kernel ([FLA commits](https://github.com/fla-org/flash-linear-attention/commits?author=Nathancgy)).

## Nine months of ML rested on three years of competitive coding and strong mentors

"No olympiad" is literally true and practically misleading. 中国新闻周刊 states plainly that he has "no olympiad gold medal, no grade-skipping, and no child-coding-genius narrative" ([中国新闻周刊 via ifeng](https://news.ifeng.com/c/8vO7wsFXz3e)). I found no NOI, IOI or IMO record. But the Codeforces API shows a long, steady climb:

- The account **Nathan4** was registered in July 2022, and its first rated contest scored 431.
- It played **48 rated contests**.
- Its rating rose from 1600 to 1944 over 2024.
- It peaked at **2026 (Candidate Master)** at Educational Round 174 on **18 February 2025**, which was also its last rated contest ([Codeforces API](https://codeforces.com/api/user.rating?handle=Nathan4)).

He linked that account from his own blog and GitHub. He also wrote a Codeforces post titled "Stop saying learning cp is useless in the real world" ([Codeforces](https://codeforces.com/blog/entry/134864)). Baidu Baike also claims USACO Platinum, which I could not verify ([Baidu Baike](https://baike.baidu.com/en/item/Chen%20Guangyu/3397209)).

The accurate summary is that he was not a competition prodigy, but he was a dedicated amateur with strong algorithmic fluency. Writing tiled, index-heavy Triton kernels rewards exactly that fluency. He was on a US-style university-application track, where olympiad medals are not the main currency the way they are on China's 竞赛 route. That probably explains the absence better than any lack of ability ([中国新闻周刊 via ifeng](https://news.ifeng.com/c/8vO7wsFXz3e)).

"About two years" depends on where you start the clock. Sources disagree on when his ML study began. 中国新闻周刊 says both "2024" and "March 2025" in the same article. His own essay and 经济参考报 point to February 2025, right after a hackathon ([China Research Collective translation](https://chinaresearchcollective.substack.com/p/nathan-chen-from-hackathon-to-silicon); [经济参考报](https://www.jjckb.cn/20260725/f1f27b8b4f9c40f3a4aa344a29e132bd/c.html)). Measured from that start:

| Interval | Approximate length |
|---|---|
| Focused ML study to Moonshot hire (Nov 2025) | about **9 months** |
| Focused ML study to Attention Residuals | about 13 months |
| April 2024 life reset to October 2026 departure | about 2.5 years |
| First rated Codeforces contest to Moonshot | about **3.3 years** |

The two-year figure therefore understates his runway as a programmer and overstates how long the ML sprint took.

His pre-ML years were also not idle. His GitHub shows web, iOS and C++ projects from 2023. In 2024 he added applied machine learning: a small-object detector for debris in drone imagery, single-cell perturbation prediction, and a Codeforces "Year in Review" web app. Forks of Karpathy's llm.c and the ARENA interpretability curriculum show what he was reading ([GitHub repositories](https://github.com/Nathancgy?tab=repositories)). He tried other things too: a Shopify store, a short-video account that reached 290k followers in four days, a youth open-source community and a crypto bot ([China Research Collective](https://chinaresearchcollective.substack.com/p/nathan-chen-from-hackathon-to-silicon)). In April 2024 he dropped activities he had been collecting for college applications and started reading about AI safety. That August he attended a 10-day AI-and-rationality camp abroad, where he was the youngest participant ([blog](https://nathanchen.me/public/Be%20Yourself.html)).

The biggest thing the "self-taught" story leaves out is mentorship. At a February 2025 middle-school hackathon, judge 董科含 of MiraclePlus (奇绩创坛, formerly YC China) singled out his "ThirdArm" project. Dong later mentored him and brought him into a small youth program whose members included IOI gold medalists ([QbitAI](https://www.qbitai.com/2026/03/388493.html)). Dong also introduced him to DeepSeek's Jingyang Yuan, first author of Native Sparse Attention. Chen later wrote: "If I have to pick someone who has personally taught me the most about ML, it's him" ([X](https://x.com/nathancgy4/status/1950579905974218869)). A teenager with a DeepSeek researcher as an informal tutor is not starting from zero, even with no degree.

## Public kernels and upstream code opened every door

His learning method was output-first, with an AI tutor. He says he started out not knowing what a Transformer was. He downloaded classic papers, fed them to Gemini, and asked it "countless questions". He skipped multi-year video course sequences as too slow: "In this era, AI is the best teacher" ([China Research Collective](https://chinaresearchcollective.substack.com/p/nathan-chen-from-hackathon-to-silicon)). For GPU programming he skipped tutorials altogether: "I didn't study Triton systematically… the more effective way is to find a relevant paper, understand its algorithm, then read the Triton code in FLA" ([中国新闻周刊 via ifeng](https://tech.ifeng.com/c/8vOAQCPnjzP)). His Triton matmul tutorial opens with him "just on day 3 of learning Triton from scratch" ([blog](https://nathanchen.me/public/Triton-Matrix-Multiplication.html)). Each post documents something he had learned days earlier, built around production kernels rather than toy examples.

| When | What he did | Why it mattered |
|---|---|---|
| Jul 2022 – Feb 2025 | 48 rated Codeforces contests, rating 431 → 2026 ([Codeforces API](https://codeforces.com/api/user.rating?handle=Nathan4)) | Built the algorithmic fluency that kernel work reuses |
| 2023 – 2024 | Web, iOS and C++ projects; drone-imagery detector; single-cell ML; llm.c and ARENA forks ([GitHub](https://github.com/Nathancgy?tab=repositories)) | Habit of shipping; first contact with LLM code |
| Feb 2025 | Hackathon "ThirdArm" leads to mentor 董科含, who introduces DeepSeek's Jingyang Yuan ([essay](https://chinaresearchcollective.substack.com/p/nathan-chen-from-hackathon-to-silicon)) | Network and direction |
| Mar 2025 | Builds Figart-AI for a "Moonshot 48" hackathon; organizer and placement unconfirmed ([Figart-AI](https://github.com/Nathancgy/Figart-AI)) | Early product-building practice |
| Apr – May 2025 | Starts tweeting. Nuclear-norm "Tauon" optimizer take-home. Triton matmul post. DeltaNet analysis draws a reply from FLA founder Songlin Yang ([blog index](https://nathanchen.me/public/blog.html); [ifeng](https://news.ifeng.com/c/8vO7wsFXz3e)) | Public visibility in the efficient-attention niche |
| May – Jul 2025 | Co-ALIBI Triton kernels; two-line TileLang bugfix PR #604; TileLang FlashAttention he says beats FA-2 by 1.3x ([TileLang PR](https://github.com/tile-ai/tilelang/pull/604); [blog](https://nathanchen.me/public/Flash-Attention-Tilelang.html)) | Concrete proof of kernel skill |
| Jul – Aug 2025 | Seven-week Tilde Research internship; MoMoE; an exploratory project on 144 H100s ([China Research Collective](https://chinaresearchcollective.substack.com/p/nathan-chen-from-hackathon-to-silicon)) | Industry research experience |
| Sep 2025 | FLA PR #585 "[DeltaFormer] Add Model" merged, about 1,918 lines, co-authored with Yu Zhang. Viral Triton threads ([FLA PR #585](https://github.com/fla-org/flash-linear-attention/pull/585)) | The recruiting channel into Moonshot |
| Nov 2025 | Joins Kimi at 16, recruited from the FLA community ([LatePost](https://m.163.com/dy/article/KS8RC3EL0531M1CO.html)) | Frontier-lab access |
| Dec 2025 – Jul 2026 | KDA kernel PRs; Attention Residuals (Mar); K3 report (Jul) ([arXiv](https://arxiv.org/abs/2603.15031)) | The headline results |
| 15 Oct 2026 | Announces he has left Kimi; no destination given ([扬子晚报](https://www.yzwb.net/news/txs/202610/t20261015_402791.html)) | — |

Three doors opened, and each followed the same pattern: **a specific senior person saw a specific public artifact.**

**First door: Tilde Research.** He shared a technical reflection on X. The author of the post he was reflecting on replied, and Tilde's CEO saw the exchange and contacted him through his personal website. Tilde set a one-week take-home: derive and implement an optimizer under the nuclear norm and train a NanoGPT-scale model with it. He finished it overnight. His own write-up calls the result "bad" because a sign error meant "I optimized the nuclear norm in the opposite direction". He still got the offer ([Tauon post](https://nathanchen.me/public/Tauon-Optimizer.html); [China Research Collective](https://chinaresearchcollective.substack.com/p/nathan-chen-from-hackathon-to-silicon)). He later said that what opened the door "was not just skills, but the growth I showed after the first conversation" ([中国新闻周刊 via ifeng](https://news.ifeng.com/c/8vO7wsFXz3e)). That is a useful signal about what early-stage employers actually evaluate.

**Second door: the internship itself.** Tilde had fewer than 10 people, five of them interns. He worked on MoMoE and ran an exploratory project on 144 H100s ([经济参考报 via Sina](https://finance.sina.com.cn/wm/2026-07-25/doc-iniiytzm4490647.shtml); [China Research Collective](https://chinaresearchcollective.substack.com/p/nathan-chen-from-hackathon-to-silicon)).

**Third door: Moonshot.** Two months before he joined Kimi, his DeltaFormer PR merged into FLA, co-authored with Yu Zhang, the first author of Kimi Linear and an FLA co-maintainer. LatePost reports that Kimi recruited "active developers who contributed heavily", Zhang Yu and Chen Guangyu, from the FLA community, which is where Moonshot's linear-attention work lives ([LatePost via NetEase](https://m.163.com/dy/article/KS8RC3EL0531M1CO.html)).

The visibility was real but modest. His September 2025 threads included a Triton tutorial with 99k views and 1k likes, and about 1,000 of his roughly 1,500 followers arrived in a single week ([blog](https://nathanchen.me/public/Twitter%20is%20Awesome,%20but%20Don't%20Optimize%20for%20Virality.html)). None of his own repositories has more than 39 stars. A viral repo was not the mechanism. **Merged upstream code, reviewed by a future colleague, plus writing that showed how he thinks** was. His own advice says the same: "Don't be the tutorial guy. Optimize for conversations, not impressions. Post what you're actually curious about" ([blog](https://nathanchen.me/public/Twitter%20is%20Awesome,%20but%20Don't%20Optimize%20for%20Virality.html)), and "I got my first internship because of a tweet followed by a virtual call!" ([blog](https://nathanchen.me/public/Be%20Yourself.html)).

## The viral post gets the résumé right and the ending wrong

| Claim in the @NFT_Chen post | Verdict | What the evidence shows |
|---|---|---|
| A 17-year-old ex-Kimi researcher | **True** | Reported age 17; he thanked Kimi for hiring him at 16 and announced his departure around 15 Oct 2026 ([扬子晚报](https://www.yzwb.net/news/txs/202610/t20261015_402791.html); [BlockBeats](https://www.theblockbeats.info/flash/371927)) |
| "Recruited to Moonshot's core team at 16" | **Age true; "core team" overstated** | Xinhua's 经济参考报 calls him an **intern**. LatePost says he was recruited from the FLA community. His X bio read "member of technical staff @kimi_moonshot" ([经济参考报](https://www.jjckb.cn/20260725/f1f27b8b4f9c40f3a4aa344a29e132bd/c.html); [LatePost](https://m.163.com/dy/article/KS8RC3EL0531M1CO.html); [X](https://x.com/nathancgy4)) |
| Co-first author of "Attention Residuals" | **True** | Listed first of three equal-contribution authors. The core idea is credited to Su Jianlin ([arXiv PDF](https://arxiv.org/pdf/2603.15031); [36Kr](https://eu.36kr.com/zh/p/3737678705967369)) |
| "Liked by Musk" | **Roughly true, imprecise** | Media report that Musk called it "impressive work from Kimi", which is praise for the team's paper. The original post was not independently verified ([经济参考报 via Sina](https://finance.sina.com.cn/wm/2026-07-25/doc-iniiytzm4490647.shtml)) |
| "Contributed to K3 foundational architecture" | **True, with nuance** | Block AttnRes is one of K3's two headline components, and he worked on KDA kernels. He is one of about 400 alphabetically listed contributors, so "rewrote K3's core architecture" headlines overstate it ([arXiv K3](https://arxiv.org/abs/2607.24653); [21财经](https://m.21jingji.com/article/20260720/herald/cbcd5d12c5de5d1cfc0151814843a6c8.html)) |
| "Poached by Dario within 24 hours" | **No evidence** | Every report says he gave no reason for leaving and named no destination ([BlockBeats](https://www.theblockbeats.info/flash/371927)) |
| "Scaling RL Member of Technical Staff at Anthropic with the Sholto team" | **Unverified** | No media report, Anthropic statement or post of his own. The only "Anthropic" link found is forum commenters guessing from a San Francisco reference ([locdd forum](https://www.locdd.com/t/topic/100607)) |

The Anthropic claim is plausible enough to spread, which is why it deserves care. Sholto Douglas does work on scaling reinforcement learning at Anthropic. He announced joining in early 2025, and a podcast in October 2026 described him as an RL tech lead there ([X](https://x.com/_sholtodouglas/status/1895610467818901609); [Joe Lonsdale podcast](https://blog.joelonsdale.com/p/ep-164-inside-anthropic-with-sholto)). So the team name in the viral post is real. The "Member of Technical Staff" title proves nothing either, because Chen's own X bio already used it for his Kimi role.

A Kimi-to-Anthropic move would also have been unusually newsworthy in 2026. Anthropic publicly accused Moonshot of distillation in September, after White House OSTP allegations in July about how K3 was trained ([CNBC](https://www.cnbc.com/2026/09/11/chinese-ai-labs-moonshot-deepseek-alibaba-anthropic.html); [Techmeme](https://www.techmeme.com/260722/p32)). Yet searches in English and Chinese found no coverage of such a hire. His homepage, when checked on 15 October 2026, still showed only Kimi ([nathanchen.me](https://nathanchen.me/)).

The Sholto reply in your screenshot points away from a confirmed hire, not toward one. The machine-translated text reads roughly: "Congrats bro — great to see you last week. Is the plan still [university]? You should come to SF and work with prime/base10 and their team!" The university name is omitted here under this report's privacy rule. That university is consistent with a verified university email on his Google Scholar profile.

Three readings follow if the screenshot is authentic:

- **"Great to see you last week"** shows they had recently met in person, so the network is real.
- **"Is the plan still [university]?"** shows that Sholto understood Chen's default next step to be starting university, which matches 扬子晚报's guess that he left to enroll ([扬子晚报](https://www.yzwb.net/news/txs/202610/t20261015_402791.html)).
- **"You should come to SF"** is a suggestion, not a congratulation on joining Anthropic.

"prime/base10" is ambiguous. Prime Intellect (a large-scale RL training lab) and Baseten (an inference company) are plausible referents, and if that is what it means, Sholto was pointing him toward non-Anthropic teams. That reading is low-confidence, because the original English wording and context are unverified.

The reading that best fits the evidence as of 15 October 2026 has four parts. He left Kimi. He has finished high school. He most likely has a university place lined up, though neither he nor the university has confirmed it. He has warm ties to US frontier-lab researchers, apparently including Sholto. A formal Anthropic role is unconfirmed, and "24 hours" and "Dario" look like embellishment typical of viral 天才少年 ("genius teen") posts.

## A six-stage roadmap that copies the mechanism, not the miracle

The part of his path you can copy is the loop: learn something hard, write it up while it is fresh, ship code into the repository where a lab's research lives, and let specific people see it. The durations below are **my estimates, not sourced figures**. They assume about 25–40 focused hours a week and access to modest rented GPU time. For comparison, his own Stages 1–3 took about seven months, from February to September 2025, on top of an existing Stage 0.

| Stage (estimated duration) | Learn | Build and publish | What Chen actually did |
|---|---|---|---|
| **0. Programming fluency** (est. 6–18 months from zero; skip if you can already solve ~1600–1900-rated problems or build non-trivial projects unaided) | Python plus one systems language, data structures, algorithms | Contest rating; a few shipped projects | 2.5 years of Codeforces to Candidate Master; web, iOS, C++ and applied-CV repos |
| **1. Build an LLM from scratch** (est. 2–4 months) | Linear algebra (including SVD and orthogonalization), probability, backprop, PyTorch, Transformer internals | GPT-2-small reproduction and a nanochat run, with loss curves and a write-up | Gemini-tutored paper reading from Feb 2025; earlier llm.c and ARENA forks |
| **2. Kernels in public** (est. 2–4 months) | Triton, roofline analysis, FlashAttention's online softmax, parallelism basics | A Triton matmul and a FlashAttention forward pass; a kernel for a non-standard attention variant; one reference-quality tutorial; a leaderboard submission | Triton matmul ("day 3"), Co-ALIBI kernels, TileLang FlashAttention, a `make_block_ptr` guide built on FLA kernels |
| **3. Upstream into a lab-adjacent repo** (est. 2–4 months, overlapping Stage 2) | The target repo's codebase and testing conventions | One small fix, then one full feature with tests, worked through with maintainers | Two-line TileLang fix (Jun 2025), then the full DeltaFormer model in FLA (Sep 2025) |
| **4. Small-scale original research** (est. 3–6 months) | Experimental design, seeds and variance, scaling-law fitting; RL for LLMs if that is your target | One rigorous ablation or scaling study, written up honestly, including negative results | The Tauon optimizer experiment (a failure he published) and a linear-attention variant repo. **No public RL work**, which is the gap for a Scaling-RL target |
| **5. Visibility and a stepping stone** (continuous; by this estimate a first offer lands somewhere around months 12–24 of Stages 1–5) | How to write for researchers and how to do cold outreach | X threads and blog posts, substantive replies to researchers, applications to small startups and structured programs | Started tweeting Apr 2025; a tweet led to a call and then the Tilde internship; FLA activity led to Kimi |

**Stage 0** is the step his story most often omits. You do not need Candidate Master. You do need to implement fiddly, index-heavy code correctly without hand-holding, because tiled GPU kernels demand exactly that.

**Stage 1** has an excellent free curriculum:

- **Karpathy's "Neural Networks: Zero to Hero"** assumes only "solid programming (Python)" and "intro-level math" ([karpathy.ai](https://karpathy.ai/zero-to-hero.html)).
- **Stanford's CS336, Spring 2026**, has public lectures and handouts. Its first assignment has you build a tokenizer, a Transformer and an optimizer from scratch ([CS336](https://cs336.stanford.edu/)).
- **Karpathy's nanochat** runs a full ChatGPT-style pipeline. Its smallest tier costs about $100 and takes about four hours on one 8×H100 node ([Analytics Vidhya](https://www.analyticsvidhya.com/blog/2025/10/andrej-karpathys-nanochat/)).

Copy his habit of using an LLM to interrogate papers line by line, then check your understanding by reimplementing.

**Stage 2** is where he got noticed, so treat its outputs as portfolio pieces, not homework:

- CS336's second assignment covers a Triton FlashAttention-2 and memory-efficient distributed training ([CS336](https://cs336.stanford.edu/)).
- **"How to Scale Your Model"**, co-authored by Sholto Douglas himself, teaches roofline analysis and parallelism ([scaling book](https://jax-ml.github.io/scaling-book/)).
- **GPU MODE** runs lectures plus kernel leaderboards that score submissions on runtime against reference kernels. That gives you an objective number to put next to your name ([GPU MODE](https://github.com/gpu-mode)).

The benchmark for "good enough" is a post like Simon Boehm's CUDA matmul write-up, which Sholto called "the world-class reference example" and said would be "an immediate" hire ([Dwarkesh Podcast](https://www.dwarkesh.com/p/sholto-douglas-trenton-bricken)).

**Stage 3** is the most transferable lesson, and the most under-rated. **Pick the repository a lab's research depends on, not the lab.** For Chen that was FLA, where Moonshot's Kimi Delta Attention lives. Copy the shape of his DeltaFormer PR: a layer, an HF-style model and config, roughly 990 lines of Triton ops, a naive reference implementation and tests ([FLA PR #585](https://github.com/fla-org/flash-linear-attention/pull/585)). For an RL target, Prime Intellect's **verifiers** library and **Environments Hub** accept community RL environments, and its **prime-rl** framework trained a 100B+ MoE on 512 H200s ([verifiers](https://github.com/PrimeIntellect-ai/verifiers); [INTELLECT-3](https://www.primeintellect.ai/blog/intellect-3)). That makes it a natural analog of FLA for anyone interested in where the "prime" in Sholto's reply might point.

**Stage 4** splits by target.

For architecture work, the **modded-nanogpt speedrun** is the closest public arena to his own work. Several records are depth-aggregation ideas in the same family as Attention Residuals: U-net skip connections (#11), partitioned hyperconnections (#73) and MUDD skip connections (#81). Submissions must clear p<0.01 significance with logs attached ([modded-nanogpt](https://github.com/KellerJordan/modded-nanogpt)). Reproduce the record, ablate a residual idea with multiple seeds, then use CS336's scaling-law assignment to test whether the gain holds across model sizes. That mirrors AttnRes's own method: five model sizes, hyperparameters tuned for the baseline, and a compute-equivalent comparison ([arXiv PDF](https://arxiv.org/pdf/2603.15031)).

If your goal is the role the viral post claims, weight RL more heavily than he did. Anthropic's RL Scaling Science team "studies how reinforcement learning behaves as we scale it". It asks for "a record of owning large experiments end to end" ([Anthropic Greenhouse](https://job-boards.greenhouse.io/anthropic/jobs/5264619008)). The project that mirrors this is SFT plus RL on math (CS336's fifth assignment), then GRPO from scratch on a 0.5–1.5B open model, then a small study of how reward scales with RL compute, rollout count and horizon.

**Stage 5** runs alongside everything else. Post what you are curious about and reply substantively to the researchers whose work you extend. Then pursue the realistic entry points:

- **Small research startups.** Tilde gave a 16-year-old 144 H100s.
- **The Anthropic Fellows Program.** It says "no PhD, prior ML experience, or published papers are required", provides about $15k a month in compute, and reports that more than 35% of fellows later joined Anthropic full-time ([Anthropic Alignment blog](https://alignment.anthropic.com/2025/anthropic-fellows-program-2026/)). Aggregators also list dedicated RL and ML Systems tracks ([Runway](https://app.joinrunway.io/explore/job/cmnsbkif20030la04ox9ayel8)).
- **The OpenAI Residency.** Applications for its 2026 cohort are closed ([OpenAI](https://openai.com/residency)).
- **Chinese labs.** DeepSeek said in June 2026 that all of its open roles accept interns ([36Kr](https://eu.36kr.com/de/p/3869415015404551)).

On math, the bar is undergraduate calculus, linear algebra, probability and statistics, not olympiad problem-solving. Those are CS336's stated prerequisites ([CS336](https://cs336.stanford.edu/)). Anthropic's RL research-engineer posting explicitly says strong candidates need not have "formal certifications or education credentials" or "academic research experience or publication history" ([Accel job board](https://jobs.accel.com/companies/anthropic/jobs/69411297-research-engineer-machine-learning-reinforcement-learning)).

## Copying the mechanism is realistic; copying the outcome is not

The encouraging part is real. Every input to his method is now free or cheap: the curriculum, the open repositories that accept PRs from strangers, the public leaderboards, the social platforms, and an AI tutor. Labs also hire this way on the record:

- **Sholto Douglas** was turned down by the graduate programs he wanted. He did independent research on a TPU research grant, and James Bradbury noticed his public questions and blog ("Who on earth are you?") before Google hired him. Sholto had "only been in the field for 1.5 years" when he was interviewed on Dwarkesh's podcast in March 2024 ([Dwarkesh Podcast](https://www.dwarkesh.com/p/sholto-douglas-trenton-bricken)).
- **Keller Jordan's** Muon optimizer was published as a blog post in December 2024, and secondary sources say he joined OpenAI that same month with no arXiv paper ([Muon post](https://kellerjordan.github.io/posts/muon/); [36Kr](https://www.36kr.com/p/3338821439222025)).

Chen's path is a third example of a single repeatable pattern: a hard, verifiable artifact on the most topical problem of the moment, seen by one senior person who reaches out.

The sobering part is equally real, and you should plan around it rather than ignore it.

**His path had enablers you cannot schedule.** A MiraclePlus mentor and a youth program full of IOI medalists. A DeepSeek researcher as an informal tutor. The resources to attend a camp abroad and take a San Francisco internship as a minor. A startup willing to give a teenager 144 H100s.

**He also had timing.** Linear attention was a hot topic in 2025, and FLA happened to be a direct pipeline into Moonshot.

**At Moonshot, senior colleagues supplied the core idea.** Su Jianlin originated AttnRes, and Chen extended and scaled it. Global amplification followed from Musk's comment and the 天才少年 news cycle.

**Survivorship bias is severe.** Nobody counts the teenagers who wrote good Triton posts and were never noticed. Even structured pipelines convert at modest rates. Fellows' 35% applies to an already highly selected pool. A LinkedIn analysis of MATS alumni found only about six working on capabilities at frontier companies ([Ryan Kidd](https://www.greaterwrong.com/posts/tPjAgWpsQrveFECWP/ryan-kidd-s-shortform)).

**The bar is rising.** The modded-nanogpt record has fallen from 45 minutes to 0.665 minutes, and some 2026 records come from AI research systems ([modded-nanogpt](https://github.com/KellerJordan/modded-nanogpt)). The easy speedrun wins are gone.

**"No credentials needed" does not mean "no experience needed".** The RL Scaling Science posting wants a record of large experiments owned end to end. If an Anthropic offer does materialize for Chen, it will have come after a year of frontier-lab pretraining work, not straight out of self-study.

My honest assessment for a motivated, already-strong programmer has three tiers, and it is judgment rather than sourced data:

- Following this roadmap at full intensity gives **good odds** of open-source recognition and a startup research internship within roughly 12–24 months.
- It gives **a real but minority chance** of a frontier-lab internship or fellowship.
- It gives **a small chance** of the full Chen trajectory on his timeline.

For most people who do make it, two to four years to a frontier research role is a more realistic horizon. The intermediate outcomes are not consolation prizes: each is the next door in his own sequence.

## Conclusion

The most useful correction to the legend is that Chen was not hired despite lacking credentials. He was hired on a different credential: **a merged PR, reviewed by the person who became his co-first author, in a community the lab already recruited from**. That reframes the replicator's main decision. The question is not which company to target or which olympiad you missed. It is which open-source project sits on the critical path of the research you want to do, and whether you can become one of its most useful contributors within a year. His speed came from two things anyone can now copy: learning output-first with an AI tutor, and publishing within days of learning. The gating step, a specific senior person paying attention, can only be made more likely, by putting more good work in front of the right small communities.

The Anthropic rumor, oddly, shows the same lesson from the other side. Whatever he does next, the screenshot you were sent shows his real currency in October 2026: in-person relationships with frontier researchers and an open invitation to San Francisco. A year of shipped work bought him that, not a 24-hour poaching. Anyone attempting this path should judge progress the same way, by which serious people know your work and would vouch for it, not by follower counts or headlines. Those relationships compound, while viral moments fade.
