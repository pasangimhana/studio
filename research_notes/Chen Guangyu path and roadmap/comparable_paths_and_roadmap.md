# Comparable non-traditional paths into frontier AI labs, and a realistic self-study roadmap toward LLM pretraining-architecture / RL-scaling research (context for Chen Guangyu / 陈广宇)

Research date: 2026-10-15. All dates below come from the sources. Secondary or aggregator sources are flagged.

---

## Q1. Well-documented non-traditional paths into frontier labs: what did these people actually do to get noticed?

### Takeaway
The documented cases follow one pattern. A person produced a **public, technically hard artifact on the most topical problem of the moment**: a blog post, an optimizer, a speedrun record, an open-source contribution, or a scaling-laws paper. That artifact was **seen by a specific senior person** who then reached out. Credentials barely appear in these stories, but networks, timing, and access to compute (TPU grants, startup GPUs) show up in almost every one. Chen Guangyu's reported path (open-source FLA → X visibility → SF startup internship → Moonshot) fits the pattern. **His reported move to Anthropic could not be confirmed** by any source found as of 2026-10-15.

### Cited Findings

**Chen Guangyu (陈广宇, "Nathan Chen") — the subject**
- QbitAI (量子位), 2026-03-17: he is a **17-year-old high-school student** and co-first author of Kimi's "Attention Residuals" paper, alongside Su Jianlin (苏剑林, creator of RoPE) and Zhang Yu (张宇, first author of Kimi Linear). He joined Moonshot AI in **November 2025** after a summer internship at a Silicon Valley AI startup. — [QbitAI](https://www.qbitai.com/2026/03/388493.html)
- How he got in, per QbitAI. Following the **Flash Linear Attention (FLA) open-source project on GitHub** first sparked his interest in ML and led to the invitation to join Kimi. He reportedly "didn't know what a Transformer was" when he started. He learned with guidance from DeepSeek researcher Yuan Jingyang (袁境阳), used Gemini as a study aid, read classic papers, and followed open-source projects. After joining he worked "downward" into papers, implementations, and Triton kernels. — [QbitAI](https://www.qbitai.com/2026/03/388493.html)
- Pre-ML history, per QbitAI. He tried a Shopify cross-border e-commerce store and ran short-video accounts. In Feb 2025 he presented "ThirdArm" (a third mechanical hand concept) at a Beijing middle-school hackathon. Judge Dong Kehan (董科含), a founding member of 奇绩创坛 (MiraclePlus), became his mentor and admitted him to a small youth program, where he met IOI gold medalists. He posted a reflection on someone's blog post on X. The author replied, and this drew the attention of a Silicon Valley AI startup CEO. He then interned in San Francisco for **7 weeks in summer 2025 after passing a timed overnight experiment**, and in his first two weeks defined and led an exploratory project on **144 H100 GPUs**. The startup was founded in late 2024, raised an $8M seed in early 2025, and has backers linked to OpenAI and Anthropic. — [QbitAI](https://www.qbitai.com/2026/03/388493.html)
- **Olympiad background:** QbitAI does **not** describe him as an olympiad medalist. IOI gold medalists appear only as peers he met in the youth program. — [QbitAI](https://www.qbitai.com/2026/03/388493.html)
- His contribution, per BlockBeats. Su Jianlin first proposed replacing residual connections with attention and verified preliminary results. Chen and Zhang Yu then proposed **Block AttnRes**, which reduces GPU memory and communication overhead and was later adopted in **Kimi K3**. With Zhang he also optimized GPU kernels for Kimi Delta Attention, researched training optimizers, and built K3 launch demos. — [BlockBeats](https://www.theblockbeats.info/flash/371927)
- BlockBeats reports that he announced he had left Kimi: he joined at 16 in Nov 2025 and stayed less than a year. He called it his best experience so far and gave **no destination**. The post date is not shown on the page. — [BlockBeats](https://www.theblockbeats.info/flash/371927)
- The paper was announced by Kimi on X and praised by Elon Musk. Per search-result summaries of the official post, the claims are ~1.25x compute advantage and <2% inference latency overhead. — [Kimi on X](https://x.com/Kimi_Moonshot/status/2033378587878072424); [TechNews.tw, 2026-03-23](https://technews.tw/2026/03/23/kimi-attention-residuals-17-year-old-ai/)
- **The Anthropic claim is unverified.** English and Chinese searches ("Chen Guangyu Anthropic Scaling RL", "陈广宇 加入 Anthropic") turned up no report of him joining Anthropic. The closest results were unrelated (e.g., Yao Shunyu's moves). A third-party profile (aggregator) still lists him as an ML researcher at Kimi, says he attends high school in Shenzhen, and says his ML journey began by contributing to FLA. — [Lessie profile (aggregator)](https://profile.lessie.ai/guangyu-chen)
- Anthropic does have an "RL Scaling Science" team. Its posting says the team "studies how reinforcement learning behaves as model size, compute, and task horizon grow" and turns that into frontier training recipes. — [Anthropic Greenhouse posting](https://job-boards.greenhouse.io/anthropic/jobs/5264619008)

**Sholto Douglas (Google DeepMind → Anthropic)** — Dwarkesh Podcast, episode dated **2024-03-28**
- The grad programs he wanted turned him down, so he did his own research on nights and weekends. Gwern's scaling hypothesis post made him "completely scaling-pilled". He used a **TPU research grant**, and **James Bradbury noticed his public questions and blog**: "Who on earth are you?" Bradbury then asked whether he wanted "to explore working with us here." — [Dwarkesh transcript](https://www.dwarkesh.com/p/sholto-douglas-trenton-bricken)
- He says he was hired "as an experiment" in pairing someone with "extremely high enthusiasm and agency" with some of the best engineers, and he was mentored by Reiner Pope and Anselm Levskaya. Before Google he worked at McKinsey. — [Dwarkesh transcript](https://www.dwarkesh.com/p/sholto-douglas-trenton-bricken); [Sankalp blog summary](https://sankalp.bearblog.dev/shoulto-and-trent-on-dwarkesh-podcast-its-amazing-how-you-can-become-world-class-at-something/)
- The episode intro quotes the remark that he had "only been in the field for 1.5 years" (as of March 2024). — [Dwarkesh transcript](https://www.dwarkesh.com/p/sholto-douglas-trenton-bricken)
- He later co-authored Google DeepMind's "How to Scale Your Model" (published 2025-02-04). — [How to Scale Your Model](https://jax-ml.github.io/scaling-book/)
- He is now at Anthropic, per an aggregator covering a later interview (low-reliability source). — [we0.ai](https://we0.ai/zh/articles/anthropic-s-sholto-douglas-on-agi-4t-ai-c-b1a7ffbc)

**Trenton Bricken (Anthropic interpretability)** — same episode
- He came from computational neuroscience ("no business there at all"). He was a first-year grad student without an advisor, met Anthropic's Tristan Hume by joining a group chatting at a conference, and says he "would've waited at least another year" to apply otherwise. He "still had to go through the whole hiring process." — [Dwarkesh transcript](https://www.dwarkesh.com/p/sholto-douglas-trenton-bricken)

**Andy Jones and Simon Boehm (cited by Sholto as hired from public work)**
- Andy Jones wrote a paper on "scaling laws as applied to board games". Sholto says it "demonstrated incredible engineering skill and incredible understanding of the most topical problem of the time", and that Anthropic and OpenAI reacted with "we would desperately like to hire you." — [Dwarkesh transcript](https://www.dwarkesh.com/p/sholto-douglas-trenton-bricken)
- Simon Boehm's CUDA matmul optimization blog post is, in Sholto's words, "the world-class reference example". Sholto says that kind of work would be "an immediate" hire. — [Dwarkesh transcript](https://www.dwarkesh.com/p/sholto-douglas-trenton-bricken)

**Keller Jordan (OpenAI)**
- His Muon post ("Muon: An optimizer for hidden layers in neural networks") is dated **2024-12-08** and is cited as a blog post (@misc), not a paper. It reports that Muon improved the NanoGPT speedrun record by 1.35x and the CIFAR-10 94% record from 3.3 to 2.6 A100-seconds. — [Keller Jordan blog](https://kellerjordan.github.io/posts/muon/)
- Secondary sources say he joined OpenAI in **December 2024**. 36Kr says he had no top-conference paper and no arXiv paper. Yuchen Jin (Hyperbolic co-founder, Muon co-author) said on X that Muon was "only a blog post" that got Jordan into OpenAI. Jin's further claim that Muon may be used for GPT-5 is **speculation**. — [36Kr](https://www.36kr.com/p/3338821439222025); [TechBang](https://www.techbang.com/posts/123808-muon-optimizer-gpt5-key-tech)
- His X profile reads "CIFAR-10 fanatic. Pretraining @OpenAI". A Digg thread quotes him saying big-lab researchers read almost no papers from top ML venues. — [Digg profile](https://digg.com/rankings/kellerjordan0); [Digg thread](https://digg.com/tech/kzx34yq2)
- The modded-nanogpt README records **Muon's introduction as record #3 (24.9 min, 2024-10-04, Keller Jordan and @jxbz)**. The Muon blog post gives 10/15/24 for the AdamW→Muon record, a minor discrepancy. — [modded-nanogpt](https://github.com/KellerJordan/modded-nanogpt); [Muon post](https://kellerjordan.github.io/posts/muon/)

**Chris Olah (Anthropic co-founder; no degree)**
- He dropped out of college in 2009 and received a **Thiel Fellowship** in 2012 ($100k to skip university). — [80,000 Hours podcast page](https://80000hours.org/podcast/episodes/chris-olah-unconventional-career-path/); [EA Forum summary](https://forum.effectivealtruism.org/posts/DxNSjxcMhFnHLztcN/chris-olah-on-working-at-top-ai-labs-without-an-undergrad)
- His blog posts (e.g., on LSTMs and representations) drew wide readership before he joined Google Brain in 2015. This is from an aggregator wiki. — [LongtermWiki](https://www.longtermwiki.com/people/chris-olah)
- Sholto says one of Jeff Dean's "most important hires he ever made was off a cold email". The transcript summary attributes this to Chris Olah, and that attribution may be the summarizer's, not Sholto's. — [Dwarkesh transcript](https://www.dwarkesh.com/p/sholto-douglas-trenton-bricken)

**Chinese labs' young-talent hiring**
- DeepSeek, Feb 2025: 52 openings in Beijing and Hangzhou, open to fresh grads and interns. The deep-learning researcher (AGI) role paid up to ¥1.54M/yr. Reports say DeepSeek looks for candidates' distinctive strengths rather than only top-ranked talent. — [TechNews.tw](https://technews.tw/2025/02/05/deepseek-annual-salary/); [ifeng](https://tech.ifeng.com/c/8gieUqRDDa7)
- DeepSeek, June 2026: 33 roles (algorithms, R&D, product) as part of a plan to at least double team size. **All roles accept interns.** — [36Kr (DE)](https://eu.36kr.com/de/p/3869415015404551)
- ByteDance Seed "Top Seed": the 2026 cohort (launched April 2025) targeted ~30 top **PhD** graduates in LLM research and said "不限专业背景" (any academic background). For the 2027 cohort it was merged into the "Seed 大模型人才校招" campus program, which aims for ~100 hires globally (April 2026). It still targets graduating students and interns, not high schoolers. — [ByteDance Top Seed page](https://seed.bytedance.com/zh/topseed); [Seed early career](https://seed.bytedance.com/zh/seedearlycareer); [Sina, 2026-04-01](https://finance.sina.com.cn/tech/discovery/2026-04-01/doc-inhsysmc5063415.shtml)
- No source found describes a formal Moonshot "天才少年" program. Chen's hire looks like a one-off invitation via open-source and personal networks. — [QbitAI](https://www.qbitai.com/2026/03/388493.html)

### Inferences
- **The common mechanism:** a public artifact on a frontier-relevant problem, plus a specific senior reader who reaches out. Bradbury found Sholto, Kimi found Chen via FLA/X, and OpenAI found Jordan's Muon post. Cold applications through the front door are not what these stories describe. Trenton is the exception: he got in through an in-person conference encounter.
- **The artifacts are narrow and verifiable:** a speedrun record, an optimizer that beats AdamW on a public benchmark, a kernel blog, a scaling-laws study. Quality can be checked in minutes, which is why missing credentials matter less.
- **Hidden enablers recur in every case.** Each had access to compute or mentorship that most self-learners lack: Sholto's TPU grant, Chen's MiraclePlus youth program, DeepSeek-researcher guidance, and 144 H100s at a startup, and Olah's Thiel Fellowship. The report should not present these paths as pure solo self-study.
- Chen's path also had an **intermediate step** (the SF startup internship) before the frontier lab. That step-stone pattern seems more replicable than a direct jump.
- Chen's **architecture work is closely related to an open speedrun-community thread.** modded-nanogpt records include "U-net skip connections" (#11), "Partitioned hyperconnections" (#73), and "MUDD skip connections" (#81), all of which are depth-wise residual-aggregation ideas like Attention Residuals. That makes it a natural public venue for replicating this type of work ([modded-nanogpt](https://github.com/KellerJordan/modded-nanogpt)).

### Gaps
- **No primary or secondary confirmation was found that Chen Guangyu joined Anthropic's Scaling RL team (or Anthropic at all)** as of 2026-10-15. Treat it as unverified.
- BlockBeats' departure post has no visible date.
- The QbitAI article gives no timeline for when he "didn't know what a Transformer was", so the true learning duration cannot be measured.
- Keller Jordan's own account of his hiring was not found. The "blog post got him hired" claim is secondhand (Yuchen Jin / Chinese media). His pre-2024 background (prior employment and education) was not verified in this session.
- It was not verified whether Andy Jones and Simon Boehm actually joined Anthropic. The transcript only gives Sholto's characterization.
- A widely reported link (Moonshot's Kimi models used Muon, and Su Jianlin worked on scaling Muon) was not verified this session.
- No account was found of other modded-nanogpt record-holders being hired by labs because of their records.

---

## Q2. What do Anthropic job postings and Anthropic people say is required?

### Takeaway
Anthropic's RL postings **explicitly say strong candidates need not have formal credentials, academic research experience, or publications**, but they ask for substantial **empirical, hands-on experience with large-scale training and distributed systems**. They still list a bachelor's degree "or equivalent experience". Anthropic people's stated hiring criteria are **agency** plus **"the ability to do something at a world-class level"**, shown through public work.

### Cited Findings
- **Research Engineer, ML (Reinforcement Learning)**, London (posting now closed, "6+ months ago"):
  - Good fit: proficient Python and async/concurrent programming (e.g., Trio); PyTorch, TensorFlow, or JAX; **"industry experience in machine learning research"**; balancing research and engineering; enjoying pair programming; code quality and testing; systems design.
  - Strong candidates may have: LLM architecture and training familiarity; RL techniques and environments; sandboxed code execution; Kubernetes; distributed/HPC; Rust/C++.
  - **"Strong Candidates Need Not Have: Formal certifications or education credentials; Academic research experience or publication history."** Bachelor's "in a related field or equivalent experience."
  - Salary £260k–£630k. — [Accel job board mirror](https://jobs.accel.com/companies/anthropic/jobs/69411297-research-engineer-machine-learning-reinforcement-learning)
- **Research Engineer, RL Scaling Science**, London (current Greenhouse posting):
  - Responsibilities: design, run, and interpret large-scale RL experiments; study how RL improves with horizon, compute, and model size; build long-horizon RL benchmarks; move findings into production recipes; debug failures that appear only at scale.
  - Minimum qualifications: strong empirical research skills in RL or large-scale ML training; **"a record of owning large experiments end to end"**; Python plus distributed ML systems; comfort at the research/systems boundary.
  - Preferred: published or shipped long-horizon RL work; frontier-scale runs.
  - Education: bachelor's "or an equivalent combination of education, training, and/or experience."
  - Salary £375k–£640k; at least 25% in office. — [Anthropic Greenhouse](https://job-boards.greenhouse.io/anthropic/jobs/5264619008)
- "Research Engineer, Performance RL" (Code RL team, June 2026) lists USD 350k–850k, per an aggregator. The RL team postings describe focus areas such as computer use and code generation through RL. — [Accel job board](https://jobs.accel.com/companies/anthropic/jobs/82650916-research-engineer-performance-rl-reinforcement-learning)
- Sholto Douglas: "what people are looking for are two things. One is agency and putting yourself out there… [and] the ability to do something at a world-class level." Also: "Demonstrate how much you care and the work you're willing to put in," and caring "an unbelievable amount" means "you check all the details." He adds that there is "surprising alpha" in going to the office every day. — [Dwarkesh transcript, 2024-03-28](https://www.dwarkesh.com/p/sholto-douglas-trenton-bricken)
- Trenton Bricken: "the system is not your friend… you almost have to just charge at certain things"; "if you just go ham, then you can get really far, pretty fast"; "Strong ideas loosely held"; "Go all the way down" when blocked. — [Dwarkesh transcript](https://www.dwarkesh.com/p/sholto-douglas-trenton-bricken)
- Dwarkesh suggests a screening heuristic: can the candidate write "an interesting technical blog post about their research"? — [Dwarkesh transcript](https://www.dwarkesh.com/p/sholto-douglas-trenton-bricken)
- A 36Kr headline about a profile of Anthropic's ~1,680-person engineering team characterizes it as "谷歌系、12年经验、本硕为主" (Google alumni, ~12 years' experience, mostly bachelor's/master's). The body could not be retrieved (security interstitial), so the methodology is unknown. — [36Kr](https://36kr.com/p/3854154166359047)

### Inferences
- **"No credentials needed" is not "no experience needed."** The RL Scaling Science role wants "a record of owning large experiments end to end" and distributed-systems experience. A self-taught candidate has to produce a *substitute* for that record, such as public large-ish experiments, speedrun records, or meaningful merged PRs to RL frameworks.
- If the 36Kr headline is accurate, the typical Anthropic engineer is an experienced big-tech engineer, and young no-degree hires are rare exceptions (see Q5).
- A teenager is unlikely to be hired straight into a scaling-RL research role without first having shipped at a lab. Chen reportedly had ~11 months at Moonshot working on K3 pretraining architecture and kernels, which works as the "industry ML research experience" the postings ask for.

### Gaps
- No official Anthropic statement was found on minimum age, or on how often non-degree or teenage candidates are hired.
- The full 36Kr team-composition article was not retrievable.
- No Trenton Bricken or Sholto Douglas statements from 2025–2026 specifically on hiring were retrieved (only the 2024 episode).

---

## Q3. Best current learning resources (verified to exist as of 2025–2026)

### Takeaway
A strong, free, current stack exists:
- **Karpathy's Zero to Hero** for fundamentals
- **nanoGPT/llm.c → nanochat** for a full LLM pipeline
- **Stanford CS336 (Spring 2026, all materials public)** for tokenizer → Transformer → Triton/FlashAttention → scaling laws → data → SFT/RL on math
- **"How to Scale Your Model"** for parallelism and systems
- **GPU MODE** for kernels
- **Prime Intellect's verifiers/prime-rl and Environments Hub** for RL environments and RL training

CS336 alone covers most of what an architecture/RL-scaling researcher must be able to build.

### Cited Findings
- **Karpathy "Neural Networks: Zero to Hero"**: 8 lectures, from micrograd/backprop through makemore (MLP, BatchNorm, "backprop ninja", WaveNet) to "Let's build GPT" and "Let's build the GPT Tokenizer". Stated prerequisites: "solid programming (Python), intro-level math (e.g. derivative, gaussian)". The micrograd lecture assumes "a vague recollection of calculus from high school." — [karpathy.ai/zero-to-hero](https://karpathy.ai/zero-to-hero.html)
- **nanochat** (Karpathy, released Oct 2025):
  - A full-stack ChatGPT-style pipeline (tokenizer → pretraining → finetuning → web UI) in about 8,000 lines, driven by one `speedrun.sh`.
  - The "$100 tier" runs ~4 hours on one 8×H100 node; a ~$1,000 / ~42-hour tier is more capable.
  - It reportedly passed 4,200 GitHub stars within ~12 hours.
  - One source states a 1.9B-param / 38B-token model for the $100 tier, which may conflate tiers. Check the repo. — [Analytics Vidhya, Oct 2025](https://www.analyticsvidhya.com/blog/2025/10/andrej-karpathys-nanochat/); [Substack](https://exploringartificialintelligence.substack.com/p/nanochat-a-chatgpt-clone-for-just); [36Kr](https://eu.36kr.com/en/p/3508416123657096)
- **Stanford CS336 "Language Modeling from Scratch", Spring 2026** (Hashimoto and Liang). Five assignments:
  - (1) Basics: tokenizer, Transformer, optimizer, train a minimal LM.
  - (2) Systems: profiling, **Triton FlashAttention-2**, memory-efficient distributed training.
  - (3) Scaling: component analysis, **fit a scaling law** via a training API.
  - (4) Data: Common Crawl → filtered, deduplicated pretraining data.
  - (5) Alignment and reasoning RL: **SFT + RL to solve math problems**, with optional DPO.
  - Lecture videos are on public YouTube, and handouts are public. — [cs336.stanford.edu](https://cs336.stanford.edu/)
- **"How to Scale Your Model: A Systems View of LLMs on TPUs"** (Austin, **Sholto Douglas**, Frostig, Levskaya, …, Reiner Pope), published 2025-02-04. Chapters cover rooflines, TPUs, sharded matmuls, "All the Transformer Math You Need to Know", parallelizing training, training and serving LLaMA 3, profiling, JAX, and a GPU chapter. Free online at GitHub Pages. — [jax-ml.github.io/scaling-book](https://jax-ml.github.io/scaling-book/)
- **GPU MODE**: a community with weekly lectures on YouTube and slides/code in the `gpu-mode/lectures` repo (Apache-2.0). Topics run from CUDA basics to FlashAttention, CUTLASS/CuTe, NCCL, and tensor cores. It runs **kernel competitions and leaderboards** (`kernelbot`, `reference-kernels`), such as the NVIDIA Blackwell NVFP4 kernel hackathon and the AMD × GPU MODE E2E model speedrun. — [GPU MODE GitHub](https://github.com/gpu-mode); [NVIDIA dev blog](https://developer.nvidia.com/blog/topping-the-gpu-mode-kernel-leaderboard-with-nvidia-cuda-compute); [Luma, NVFP4 hackathon](https://luma.com/9n27uem4)
- **Prime Intellect RL stack**:
  - **prime-rl** is an async RL framework that scales from one node to thousands of GPUs. It was used to train INTELLECT-3, a 100B+ MoE, on 512 H200s.
  - **verifiers** is a library for RL environments (dataset + harness + reward/rubric), originally by Will Brown. It is actively maintained (v0.1.14, 2026-05-07).
  - The **Environments Hub** hosts hundreds of open-source RL environments that anyone can contribute to. — [INTELLECT-3 blog](https://www.primeintellect.ai/blog/intellect-3); [verifiers GitHub](https://github.com/PrimeIntellect-ai/verifiers); [Prime Intellect](https://primeintellect.ai/)
- **modded-nanogpt speedrun**: train a 124M GPT-2-scale model to **3.28 val loss on FineWeb on 8×H100**. The record went from **45 min (llm.c baseline, 2024-05-28)** to **0.665 min (record #92, 2026-08-30, @DevenPzak)**. Submission rules include statistical significance at p<0.01, no data-pipeline changes, and a PR with logs. — [modded-nanogpt](https://github.com/KellerJordan/modded-nanogpt)

### Inferences — suggested resource stack by area
- **Fundamentals:** Zero to Hero, then nanoGPT/llm.c GPT-2 reproduction, then nanochat end to end.
- **LLM systems and architecture:** CS336 A1–A4, "How to Scale Your Model", modded-nanogpt source (it is a dense catalogue of modern architecture/optimizer tricks with ablation evidence).
- **RL for LLMs:** CS336 A5 → implement GRPO/PPO from scratch on a small model → verifiers environments + prime-rl. Other frameworks named in the brief (TRL, OpenRLHF, veRL) are long-standing projects but were **not verified this session**.
- **GPU programming:** CS336 A2 (Triton FlashAttention-2) → GPU MODE lectures → GPU MODE competition submissions.
- **Math and theory:** see Q6. The resources named in the brief (3Blue1Brown, MIT 18.06, Sutton & Barto, OpenAI Spinning Up, fast.ai, CS224N) are well known, but their current availability was **not verified this session**.

### Gaps
- The status and currency of fast.ai, CS224N, Sutton & Barto (2nd ed. free PDF), OpenAI Spinning Up, TRL, OpenRLHF, veRL, 3Blue1Brown, and MIT 18.06 OCW were not checked in this session.
- The exact nanochat model sizes per tier conflict across secondary sources.
- A 36Kr headline claimed "Andrej Karpathy官宣加入Anthropic" (Karpathy announced joining Anthropic) ([36Kr](https://www.36kr.com/p/3816814284145798)). It was **not verified** and should not be stated as fact without checking.

---

## Q4. A concrete project ladder that signals ability (and a staged roadmap)

### Takeaway
The signals that verifiably led to hires are:
- **records on public leaderboards** (modded-nanogpt, CIFAR-10 speedruns, GPU MODE)
- **reference-quality technical blog posts** (CUDA matmul, Muon)
- **small-scale scaling-law studies** (Andy Jones)
- **merged contributions to frontier-relevant open-source projects** (FLA for Chen)

A realistic ladder goes from reproduction → speedrun/kernel contributions → original small-scale architecture or RL-scaling experiments with clean public write-ups → outreach and a residency or startup internship.

### Cited Findings
- Sholto names public artifacts that get people hired: Andy Jones's board-game scaling-laws paper ("incredible understanding of the most topical problem of the time") and Simon Boehm's CUDA matmul post ("world-class reference example… an immediate" hire). — [Dwarkesh transcript](https://www.dwarkesh.com/p/sholto-douglas-trenton-bricken)
- Chen's entry point was the **Flash Linear Attention open-source project** on GitHub. — [QbitAI](https://www.qbitai.com/2026/03/388493.html); [Lessie profile (aggregator)](https://profile.lessie.ai/guangyu-chen)
- Keller Jordan's entry was a blog post on an optimizer, validated by **speedrun records**. — [Muon post](https://kellerjordan.github.io/posts/muon/); [36Kr](https://www.36kr.com/p/3338821439222025)
- The speedrun is open to anyone with access to 8×H100, and records are credited publicly by handle. Record holders include many non-lab individuals and, from 2026, teams using AI research systems (e.g., "Locus AI system", "Aster AI system", "Station AI system", "Recursive AI system"). Maintainers "will repost well-documented records." — [modded-nanogpt](https://github.com/KellerJordan/modded-nanogpt)
- Architecture-relevant speedrun records include: ReLU², QK-norm (#5); U-net skip connections (#11); value embeddings (#15); multi-token prediction (#53); **partitioned hyperconnections (#73)**; paired-head Muon (#80); **MUDD skip connections (#81)**; FP8 MLP (#89, #92). — [modded-nanogpt](https://github.com/KellerJordan/modded-nanogpt)
- CS336 assignments map directly onto frontier skills: scaling-law fitting (A3) and SFT + RL for math (A5). — [cs336.stanford.edu](https://cs336.stanford.edu/)
- The Prime Intellect Environments Hub accepts community-contributed RL environments as standalone Python packages. — [verifiers GitHub](https://github.com/PrimeIntellect-ai/verifiers)
- GPU MODE competitions score submissions on absolute runtime and speedup against reference kernels, which gives an objective public signal. — [Luma NVFP4 hackathon](https://luma.com/9n27uem4); [GPU MODE GitHub](https://github.com/gpu-mode)

### Inferences — a staged roadmap (the stage durations are the researcher's judgment, not sourced; assumes ~25–40 hrs/week)

**Stage 0 — Foundations (≈1–3 months)**
- Solid Python, numpy, and PyTorch.
- Linear algebra (matrix calculus, SVD and orthogonalization; Muon relies on Newton–Schulz orthogonalization), probability, and basic optimization.
- Zero to Hero lectures 1–8, implementing everything yourself, including "backprop ninja."

**Stage 1 — Reproduce a full LLM (≈2–3 months)**
- Reproduce GPT-2 124M with nanoGPT/llm.c on rented GPUs.
- Run nanochat end to end.
- Complete CS336 A1 without looking at solutions.
- Deliverable: a public repo plus a write-up with loss curves.

**Stage 2 — Systems and kernels (≈2–4 months)**
- CS336 A2 (Triton FlashAttention-2, distributed training).
- Read "How to Scale Your Model" and work its exercises.
- Follow GPU MODE lectures and submit to at least one GPU MODE leaderboard.
- Deliverable: a kernel blog post in the Boehm style, profiling a fused op and explaining the roofline.

**Stage 3 — Architecture research at small scale (≈3–6 months)**
- Clone modded-nanogpt and reproduce the current record.
- Attempt a record, or failing that, a rigorous ablation of a residual/depth-aggregation idea (hyperconnections, MUDD, Attention Residuals/Block AttnRes) at 124M–350M scale, with seeds and p-values as the speedrun requires.
- Do CS336 A3: fit scaling laws to see whether the gain holds across sizes.
- Deliverable: a speedrun PR or a public negative-result report.

**Stage 4 — RL for LLMs and RL scaling (≈3–6 months, can overlap Stage 3)**
- CS336 A5 (SFT + RL on math).
- Implement GRPO from scratch on a ~0.5–1.5B open model.
- Build and publish verifiers environments to the Environments Hub, and contribute fixes/features to prime-rl (or veRL/OpenRLHF/TRL).
- Run a small "RL scaling" study: how reward or pass@k scales with RL compute, rollout count, and horizon, mirroring the Anthropic RL Scaling Science job description.
- Deliverable: a write-up with plots.

**Stage 5 — Visibility and entry points (continuous)**
- Post results on X and a blog; reply substantively to researchers' posts (Chen's X reply drew a CEO's attention).
- Email authors whose work you extended.
- Apply to Anthropic Fellows (incl. its RL and ML-systems tracks), the OpenAI Residency, startup research internships, and Chinese lab internships (DeepSeek and ByteDance Seed accept interns).

**Overall:** roughly 12–24 months of near-full-time work to reach "credible candidate for a startup/residency"; "frontier-lab RL scaling researcher" is a further step (see Q5).

### Gaps
- No source quantifies which artifact types convert to offers most often.
- The stage durations above are judgment, not evidence.
- Compute cost was not sourced in detail (beyond nanochat's ~$100 and ~$1,000 tiers on 8×H100). This is a real barrier for minors and people outside the US.

---

## Q5. Timelines, success rates, intermediate outcomes, and survivorship bias

### Takeaway
The headline cases moved fast: Sholto was hired within ~1.5 years of entering the field, Chen took ~9 months from hackathon to Moonshot, and Keller Jordan was hired ~2 months after Muon. But they are **selected survivors with unusual enablers**. Structured on-ramps have published base rates. The **Anthropic Fellows Program** reports **>35% of fellows later joining Anthropic full-time** (from an already highly selected pool). **MATS** data show only a small single-digit-to-low-double-digit share of alumni in capabilities roles, ~6 people at frontier companies in capabilities. No base rate exists for self-taught people who attempt this path and fail.

### Cited Findings
- **Chen's timeline** (QbitAI / BlockBeats): Feb 2025 hackathon → summer 2025 SF internship → Nov 2025 Moonshot (age 16) → Mar 2026 Attention Residuals → left Kimi in under a year. — [QbitAI](https://www.qbitai.com/2026/03/388493.html); [BlockBeats](https://www.theblockbeats.info/flash/371927)
- **Sholto**: "only been in the field for 1.5 years" at the March 2024 recording. — [Dwarkesh transcript](https://www.dwarkesh.com/p/sholto-douglas-trenton-bricken)
- **Keller Jordan**: Muon introduced in the speedrun Oct 2024, blog post Dec 8 2024, reportedly joined OpenAI Dec 2024. — [modded-nanogpt](https://github.com/KellerJordan/modded-nanogpt); [Muon post](https://kellerjordan.github.io/posts/muon/); [36Kr](https://www.36kr.com/p/3338821439222025)
- **Anthropic Fellows Program** (official Alignment blog page):
  - "No PhD, prior ML experience, or published papers are required." Past fellows came from physics, math, CS, cybersecurity, and other fields.
  - 4 months, ~$15k/month compute.
  - **>65% of fellows published work; >35% later joined Anthropic full-time; >200 fellows since early 2025.**
  - Rolling admissions, with "apply by October 18" for the January cohort.
  - Workstreams listed on that page are safety-focused (scalable oversight, robustness/control, model organisms, interpretability, security, welfare). — [Anthropic Alignment blog](https://alignment.anthropic.com/2025/anthropic-fellows-program-2026/)
- Earlier Fellows postings cite **first-cohort** stats of >80% producing papers and >40% joining Anthropic full-time, plus a weekly stipend of $3,850. — [Accel job board, Anthropic Fellows Program](https://jobs.accel.com/companies/anthropic/jobs/74068663-anthropic-fellows-program); [Opportunity Desk, 2026-04-15](https://opportunitydesk.org/2026/04/15/anthropic-fellows-program-2026/)
- Separate Fellows postings exist for **"Anthropic Fellows Program — Reinforcement Learning"** and **"Anthropic Fellows Program — ML Systems & Performance"**, which suggests non-safety technical tracks now exist. Seen via aggregators; details not retrieved. — [Runway listing (RL)](https://app.joinrunway.io/explore/job/cmnsbkif20030la04ox9ayel8); [The Rundown listing (ML Systems)](https://jobs.therundown.ai/jobs/440813757-anthropic-fellows-program-ml-systems-performance)
- **OpenAI Residency**: a 6-month program for "talented builders and early researchers from any domain". The **2026 cohort applications are closed**. Postings say OpenAI is open to "self-taught engineers and independent builders". Residents are full-time employees embedded in research teams. Pay figures conflict across aggregators ($18.3k/month vs. a $210k package). — [openai.com/residency](https://openai.com/residency); [The Rundown listing](https://jobs.therundown.ai/jobs/181883472-residency-2026)
- **MATS outcomes**:
  - 2024 survey (72 respondents, first four cohorts): ~1% "working/interning on AI capabilities" (lab safety-team roles were counted as alignment). — [LessWrong, MATS Alumni Impact Analysis](https://www.lesswrong.com/posts/jeBkx6agMuBCQW94C/mats-alumni-impact-analysis)
  - Ryan Kidd (pre-2025 alumni, from LinkedIn): 80% still in AI safety; 10% in capabilities, with only ~6 at frontier companies; 27% of safety-working alumni at for-profits (Anthropic, GDM, OpenAI, Goodfire, Meta, etc.). — [Ryan Kidd shortform](https://www.greaterwrong.com/posts/tPjAgWpsQrveFECWP/ryan-kidd-s-shortform)
- **Chinese lab on-ramps**: DeepSeek (Feb 2025 and Jun 2026) opened roles to fresh grads and interns. ByteDance Seed targets graduating students and interns (2027 cohort ~100 hires). — [TechNews.tw](https://technews.tw/2025/02/05/deepseek-annual-salary/); [36Kr (DE)](https://eu.36kr.com/de/p/3869415015404551); [Sina](https://finance.sina.com.cn/tech/discovery/2026-04-01/doc-inhsysmc5063415.shtml)
- The speedrun has 92 records since May 2024, credited to dozens of handles. Only Keller Jordan (the maintainer) has a well-documented lab hire tied to it in the sources found. — [modded-nanogpt](https://github.com/KellerJordan/modded-nanogpt)

### Inferences — honest base-rate / survivorship assessment
- **Survivorship bias is severe.** We hear about Chen, Sholto, Jordan, and Olah because they succeeded. No denominator exists for teens or self-learners who did similar work and were never noticed. The evidence supports "this path is *possible* and labs *will* hire without credentials". It does not support "this path is *likely* to work".
- **Each success had non-replicable components:**
  - Chen: elite mentor access (MiraclePlus youth program, a DeepSeek researcher's guidance), a well-funded SF startup that gave a 16-year-old 144 H100s, a Moonshot team (Su Jianlin, Zhang Yu) whose ideas he extended, and global media amplification (Musk).
  - Sholto: a TPU grant and Bradbury's attention.
  - Olah: the Thiel Fellowship.
  - Jordan: perfect timing, since optimizer research became hot and Muon was later adopted widely.
- **Co-authorship with senior researchers matters for attribution.** In Attention Residuals the core idea is credited to Su Jianlin, and Chen and Zhang Yu proposed the Block variant. A report should not overstate a teenager's solo contribution.
- **Realistic intermediate outcomes are more likely than a direct frontier-lab research role:** open-source recognition, startup research internships, Chinese lab internships, Anthropic Fellows / OpenAI Residency, or research-engineer roles at smaller labs (e.g., Prime Intellect-style open labs). Among structured programs, Anthropic Fellows has the best published conversion (>35% to Anthropic), but admission is itself highly competitive. No admit rate was found.
- **Time horizon:** the documented fast cases took ~6–18 months of intense, full-time-equivalent effort *after* they already had strong programming ability. For most motivated self-learners, 2–4 years to a frontier research role (if it happens at all) seems more realistic. This is judgment, not sourced.
- **The bar is rising in 2026.** Speedrun records are now partly set with AI research systems, and the record has dropped to ~40 seconds. Low-hanging fruit is gone, so marginal records are harder, and "I used AI tools well" is itself a skill the postings ask for (Fellows: "ability to use AI tools").

### Gaps
- No admission rates were found for the Anthropic Fellows Program or the OpenAI Residency.
- No data was found on what fraction of Anthropic/OpenAI/GDM research staff lack degrees or were hired under 20.
- There is no systematic study of self-taught ML researchers' outcomes.
- It is unknown how many modded-nanogpt or GPU MODE contributors were later hired by labs.

---

## Q6. How much math is actually needed (vs. olympiad-level problem-solving)?

### Takeaway
The verified course prerequisites call for **undergraduate-level calculus, linear algebra, probability, and statistics, not olympiad problem-solving**. Neither Chen (per QbitAI) nor Sholto, Olah, or Jordan is documented as an olympiad medalist. What the hiring stories and postings stress instead is **engineering skill, empirical rigor, and agency**. Optimizer and architecture research does reward fluency in numerical linear algebra.

### Cited Findings
- CS336 prerequisites: "College calculus and linear algebra", "Basic probability and statistics", ML coursework, and strong Python and systems skills. — [cs336.stanford.edu](https://cs336.stanford.edu/)
- Zero to Hero prerequisites: "intro-level math (e.g. derivative, gaussian)". Micrograd assumes "a vague recollection of calculus from high school." — [karpathy.ai/zero-to-hero](https://karpathy.ai/zero-to-hero.html)
- Chen is not described as an olympiad medalist. IOI gold medalists appear only as peers. — [QbitAI](https://www.qbitai.com/2026/03/388493.html)
- Anthropic Fellows: "No PhD, prior ML experience, or published papers are required." The qualifications sought are strong coding, making concrete progress on ambiguous problems, and learning quickly and debugging. — [Anthropic Alignment blog](https://alignment.anthropic.com/2025/anthropic-fellows-program-2026/)
- Anthropic RL postings list Python, async programming, ML frameworks, distributed systems, and empirical research skill, with no math-competition or theory requirement. — [Accel mirror](https://jobs.accel.com/companies/anthropic/jobs/69411297-research-engineer-machine-learning-reinforcement-learning); [Greenhouse RL Scaling Science](https://job-boards.greenhouse.io/anthropic/jobs/5264619008)
- Muon's core is SGD-momentum plus **Newton–Schulz orthogonalization** of 2D updates, i.e., applied numerical linear algebra. — [Muon post](https://kellerjordan.github.io/posts/muon/)
- "How to Scale Your Model" includes "All the Transformer Math You Need to Know" and roofline analysis. These are arithmetic-intensity, FLOPs, and memory calculations, not proofs. — [scaling-book](https://jax-ml.github.io/scaling-book/)
- ByteDance Top Seed said "不限专业背景" (any academic background) and valued research potential, though it targeted PhDs. — [Huxiu](https://www.huxiu.com/article/4288637.html); [Top Seed page](https://seed.bytedance.com/zh/topseed)

### Inferences
- **Required math:**
  - linear algebra (matrix calculus, eigen/SVD, orthogonalization, norms; essential for optimizers like Muon and for parallelism/sharding math)
  - probability and statistics (to read loss curves, run significance tests as the speedrun requires, and understand RL policy-gradient estimators and variance)
  - multivariable calculus and backprop
  - basic optimization
  - "back-of-envelope" FLOPs/bytes arithmetic (rooflines)
- **Not required:** olympiad-style contest problem-solving. It correlates with general ability and is a common selection signal (e.g., Chinese youth programs), but no posting or hiring story here requires it.
- For **RL scaling** specifically, empirical methodology (experimental design, seeds and variance, scaling-law fitting as in CS336 A3) is probably more decisive than theory.

### Gaps
- No primary statement was found from Anthropic, OpenAI, or Moonshot researchers on how much math they use day to day.
- Sutton & Barto and Spinning Up (the classic RL-theory references) were not verified this session.
