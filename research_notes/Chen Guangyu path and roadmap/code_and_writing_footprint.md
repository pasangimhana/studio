# Chen Guangyu (陈广宇 / "Nathan Chen"): Public Code and Writing Footprint

Research date: 2026-10-15. Scope: professional, public-facing work only. Because he is a minor, these notes leave out school names, location details, contact emails (one appears in a git commit), family information and photos.

Handle summary (all verified unless marked otherwise):
- GitHub: **Nathancgy** (display name "Nathan Chen"). Verified.
- X/Twitter: **@nathancgy4**. Verified: linked from both his GitHub profile and his personal site.
- Personal site and blog: **nathanchen.me**. Verified.
- Substack: **nathancgy.substack.com** ("Third Arm"). Verified: linked from his blog index.
- Codeforces: **Nathan4**. Verified: linked from his GitHub profile.
- LinkedIn: linkedin.com/in/guangyu-chen. Linked from his site; not opened.
- Not found or not his: Hugging Face (no user "Nathancgy"), Zhihu, Bilibili, Weibo, Gitee, Google Scholar, Kaggle, LeetCode/AtCoder.

---

## Which public profiles verifiably belong to him, and does anything confirm the reported Anthropic move?

### Takeaway
His professional identity online is "Nathan Chen". The GitHub user **Nathancgy** links to Kimi, pins the MoonshotAI/Attention-Residuals repo and committed to it, and the same profile links to nathanchen.me, X @nathancgy4 and Codeforces "Nathan4", so the identity is solid. **I found no public source confirming that he joined Anthropic (Scaling RL).** As of 2026-10-15, reports say only that he left Kimi, with his next step undisclosed.

### Cited Findings
- GitHub profile "Nathancgy" (display name Nathan Chen) gives Company "Kimi" and a README saying "I'm currently working on ML research at Kimi" and "prev at Tilde". Stated interests are "efficient attention and hardware-aligned ML algorithms", plus occasional competitive programming. It links to nathanchen.me, x.com/nathancgy4 and codeforces.com/profile/Nathan4. As of 2026-10-15 it showed 489 followers, 62 repositories and a GitHub Pro badge. — [GitHub: Nathancgy](https://github.com/Nathancgy)
- Pinned repos on that profile: MoonshotAI/Attention-Residuals (about 3.5k stars), fla-org/flash-linear-attention (about 5.9k stars), Nathancgy/Co-ALIBI and OpenTeens/gestureX. — [GitHub: Nathancgy](https://github.com/Nathancgy)
- The MoonshotAI/Attention-Residuals git history has a commit by author "Nathancgy" dated 2026-03-17 ("update logo"), the day after the paper went up. This links the GitHub handle to the paper. — [MoonshotAI/Attention-Residuals](https://github.com/MoonshotAI/Attention-Residuals) (from git log of the public repo)
- The paper "Attention Residuals" (arXiv:2603.15031, v1 submitted 16 Mar 2026, author "Kimi Team") lists Guangyu Chen first, then Yu Zhang and Jianlin Su. Its comment field reads "attnres tech report". — [arXiv 2603.15031](https://arxiv.org/abs/2603.15031)
- Media report that the paper's appendix marks Guangyu Chen, Yu Zhang (张宇) and Jianlin Su (苏剑林) as equal-contribution co-first authors. — [InfoQ](https://www.infoq.cn/article/CI5daAFmzhA1IWN2Z6zD)
- His site nathanchen.me (fetched 2026-10-15) says he does "ML research at Kimi" on "LLM scaling and pretraining" including "kimi k3". It lists model architectures, optimizers and hardware-aligned algorithms/kernels as focus areas, describes earlier "applied interpretability research at Tilde Research", and links to Kimi's AttnRes announcement on X. It does **not** mention Anthropic. — [nathanchen.me](https://nathanchen.me/)
- Departure: BlockBeats (around 2026-10-15) says Chen Guangyu (Nathan Chen) announced he had recently left Moonshot's Kimi team after less than a year, having joined in Nov 2025 at 16. It calls the year "the best experience" he has had and says he "did not disclose the reason for leaving or his next destination". — [BlockBeats](https://www.theblockbeats.info/flash/371927)
- A LINUX DO thread dated 2026-10-15 reports the departure. One commenter notes the announcement was posted on X in English. No destination is named. — [LINUX DO](https://linux.do/t/topic/3026762)
- Baidu Baike (English mirror) says he was a Machine Learning Researcher on the Kimi team from November 2025 and left in October 2026, without naming a new employer. — [Baidu Baike EN](https://baike.baidu.com/en/item/Chen%20Guangyu/3397209)
- A Hugging Face lookup for "Nathancgy" returns "This user does not exist", and no models are listed under that author. — [Hugging Face](https://huggingface.co/Nathancgy)

### Inferences
- "cgy" in Nathancgy most likely stands for Chen GuangYu, and "Nathan4" on Codeforces follows the same pattern. The ownership itself does not depend on this guess; the cross-links above establish it.
- The Anthropic (Scaling RL) claim is **unverified**. Every source dated around 2026-10-15 says the destination was undisclosed, and his own site still showed Kimi when fetched. The report writer should present it as reported or rumored unless the coordinator has a primary source such as his own X post.

### Gaps
- I could not read X directly, so I don't have his farewell post text, follower count or join date. Indirectly: his blog says he started tweeting in April 2025 and had about 1.5k followers by October 2025.
- LinkedIn not opened. Gitee probe failed (connection error), so presence there is unconfirmed. Google Scholar not checked directly. No Zhihu, Bilibili or Weibo account of his own turned up in searches; only third-party Zhihu articles about him.

---

## What is his GitHub username, and what repositories and contributions does it show (2023, 2024, 2025)? Was there a viral repo or post that got Moonshot's attention?

### Takeaway
His GitHub (**Nathancgy**) shows a clear path. In 2023 there are web, app and C++ learning repos and LLM-eval forks. In 2024 come applied computer vision and bio-ML projects plus Codeforces tooling. In 2025 his work turns sharply to GPU kernels (Triton/TileLang), attention variants and optimizers, ending in **merged upstream PRs to fla-org/flash-linear-attention**: a full DeltaFormer model in Sept 2025, then Kimi Delta Attention (KDA) kernel work in Dec 2025, plus a TileLang bugfix. Reporting says Kimi recruited him **from the FLA open-source community**. The DeltaFormer merge and a burst of viral Triton tutorials on X in September 2025 came about two months before he joined Kimi in November 2025.

### Cited Findings
**Upstream open-source contributions (from public git history)**
- **fla-org/flash-linear-attention**, 4 commits by "Nathan Chen" (Nathancgy):
  - PR #585 "[DeltaFormer] Add Model", merged 2025-09-22. 15 files, about 1,918 lines added: layer, HF-style model/config, Triton ops `fla/ops/deltaformer/parallel.py` (~991 lines), naive reference and tests. Co-authored with Yu Zhang (yzhangcs), who later became his AttnRes co-first author. — [FLA PR #585](https://github.com/fla-org/flash-linear-attention/pull/585)
  - PR #602 "[DeltaFormer] Fixed testing ops error", 2025-10-17: varlen ops tests and an fp16 test. — [FLA PR #602](https://github.com/fla-org/flash-linear-attention/pull/602)
  - PR #679 "[KDA] Changed all exp to exp2", 2025-12-09: touches KDA/GLA chunk kernels. — [FLA PR #679](https://github.com/fla-org/flash-linear-attention/pull/679)
  - PR #688 "[KDA] fused bwd kernels inter and prepare wy", 2025-12-19: backward-kernel fusion in `fla/ops/kda/chunk_bwd.py`. — [FLA PR #688](https://github.com/fla-org/flash-linear-attention/pull/688)
- **tile-ai/tilelang**, PR #604 "[Bugfix] Fixed mha_bwd shape inconsistency error", 2025-06-29. A 2-line fix in `examples/flash_attention/example_mha_bwd.py`. — [TileLang PR #604](https://github.com/tile-ai/tilelang/pull/604)
- **MoonshotAI/Attention-Residuals**: commit dated 2026-03-17. — [Attention-Residuals](https://github.com/MoonshotAI/Attention-Residuals)
- No commits by him in KellerJordan/modded-nanogpt or MoonshotAI/Kimi-Linear git history (checked 2026-10-15). He only has a modded-nanogpt fork (Jul 2025). — [GitHub repos tab](https://github.com/Nathancgy?tab=repositories)

**Original repositories (stars as of 2026-10-15)**
- **Co-ALIBI** (9 stars; 31 commits, 2025-05-19 to 2025-06-28): "Hardware-aligned Triton kernels of Co-ALIBI (Contextual Attention with Linear Biases)". Forward and backward Triton kernels; README claims about 180 TFLOPS/s forward and about 80 TFLOPS/s backward on H100. — [Nathancgy/Co-ALIBI](https://github.com/Nathancgy/Co-ALIBI)
- **tauon-optimizer** (1 star; 2025-04-30 to 2025-05-03): NanoGPT trained with a low-rank nuclear-norm "Tauon" optimizer versus Muon and AdamW. This was a startup take-home assignment (see the blog section). — [Nathancgy/tauon-optimizer](https://github.com/Nathancgy/tauon-optimizer)
- **linear-attn-variant** (2025-06-21): framework for comparing diagonal SSM "D matrices" in a Mamba-like architecture against linear attention baselines. — [Nathancgy/linear-attn-variant](https://github.com/Nathancgy/linear-attn-variant)
- **learn-triton** (Jupyter, 2025-05-14), no description. — [GitHub repos tab](https://github.com/Nathancgy?tab=repositories)
- **Figart-AI** (31 stars; 2025-03-01 to 03-05; TypeScript/Next.js): AI-guided photography learning app. README: "product for Moonshot 48 hackathon (March 2025, Beijing)". — [Nathancgy/Figart-AI](https://github.com/Nathancgy/Figart-AI)
- **Encoded_reasoning_CoT** and **Rate_picture_aesthetics** (both 2025-03-01, no descriptions). — [GitHub repos tab](https://github.com/Nathancgy?tab=repositories)
- **RT-DETR-SEA** (22 stars; 2024-09-30): small-object-enhanced RT-DETR encoder (SPDConv + CSPOmniKernel) for detecting beach debris in drone imagery. — [Nathancgy/RT-DETR-SEA](https://github.com/Nathancgy/RT-DETR-SEA)
- **cf_yearly_review** (4 stars; 2024-12-01 to 12-13): JS web app giving personalized "Codeforces Year in Review" reports from the Codeforces API, hosted on nathanchen.me. — [Nathancgy/cf_yearly_review](https://github.com/Nathancgy/cf_yearly_review)
- **single_cell_perturbation** (3 stars; Sep 2024): deep learning for single-cell perturbation prediction, plus a fork of a "1st-place-solution-single-cell-pbs" repo (Jul 2024). — [GitHub repos tab](https://github.com/Nathancgy?tab=repositories)
- **Shrimp_food_detection** (3 stars; May 2024): computer vision for detecting leftover feed in shrimp ponds. **damping-oscillation** (Jun 2024). **CF_fun_stuffs** (Oct 2024). — [GitHub repos tab p2](https://github.com/Nathancgy?page=2&tab=repositories)
- 2023 originals: **LandMark_App_Swift** (SwiftUI, Sep 2023), **Grayscale_image_processing** (OpenCV histogram equalization/Canny, Sep 2023), **login_server** (Nov 2023), **Encryption-Decryption_Tool**, **Learning_Web_Development** (Dec 2023), **SimpleDBCpp** (C++, Dec 2023). Plus **Cpp_notebook** (Mar 2024). — [GitHub repos tab p2](https://github.com/Nathancgy?page=2&tab=repositories)

**Forks, which show what he was studying (dated by last update)**
- 2023: hkust-nlp/ceval (Jul), MMCU eval (Aug), bqi343/cp-notebook (Nov), microsoft/ML-For-Beginners (Nov). — [GitHub repos tab p2](https://github.com/Nathancgy?page=2&tab=repositories)
- 2024: TencentQQGYLab/AppAgent and Hannibal046/Awesome-LLM (Mar), karpathy/llm.c (Apr), THU-MIG/yolov10 (Jun), NVIDIA/ngpt (Nov), facebookresearch/memory (memory layers, Dec), ARENA-education/ARENA_materials ("ARENA_3.0", Dec). — [GitHub repos tab](https://github.com/Nathancgy?tab=repositories); [p2](https://github.com/Nathancgy?page=2&tab=repositories)
- 2025: HazyResearch/ThunderKittens (Apr), zhixuan-lin/forgetting-transformer (May), tile-ai/tilelang (Jul), shawntan/stickbreaking-attention (Jul), KellerJordan/modded-nanogpt (Jul), tilde-research/momoe-release as "MoMoE-impl" (Jul 25), fla-org/flash-linear-attention (Dec). — [GitHub repos tab](https://github.com/Nathancgy?tab=repositories)

**Community and organizations**
- OpenTeens organization repos he is attached to: gestureX (pinned; 39 stars; "extensible multi-function hand gesture project using simple MLPs"), WeatherApp (Dec 2023), scgame (Jul 2024), openteens website (May 2024), and an OpenTeensCore/backend fork (Feb 2024). — [GitHub: Nathancgy](https://github.com/Nathancgy); [repos p2](https://github.com/Nathancgy?page=2&tab=repositories)
- Media report that he said he once "organized a youth open-source community" (组织青少年开源社区). — [经济参考报 / jjckb](https://www.jjckb.cn/20260725/f1f27b8b4f9c40f3a4aa344a29e132bd/c.html)

**How Kimi found him**
- Kimi reportedly recruited him from the FLA open-source community ("据此前媒体报道，Kimi从FLA开源社区招募了他"). — [jjckb](https://www.jjckb.cn/20260725/f1f27b8b4f9c40f3a4aa344a29e132bd/c.html)
- QbitAI says the GitHub FLA project drew him into papers, source code, Triton kernels and attention rewriting and acceleration, and that this is what drew him to Kimi's long-running efficient-attention work. — [QbitAI 量子位](https://www.qbitai.com/2026/03/388493.html)
- A Zhihu answer (seen only as a search snippet; not opened) says Kimi recruited the active FLA contributors Zhang Yu and Chen Guangyu from the FLA community started by Songlin Yang. — [Zhihu question](https://www.zhihu.com/question/2035402623944238504)
- His own September 2025 X activity, as he lists it in a blog post: "Merged DeltaFormer into FLA repo" (38k views, 89 likes); "A thread (and blogpost) on GPU data access in Triton" (23k views, 456 likes); "Story on making contribution to FLA" (28k views, 269 likes); "Another thread on Triton programming tutorial" (99k views, 1k likes); "Sharing the gated attention paper and takeaways" (65k views, 522 likes). "A thousand" of his roughly 1.5k followers came "from a single week in September". — [Blog: Twitter is Awesome, but Don't Optimize for Virality](https://nathanchen.me/public/Twitter%20is%20Awesome,%20but%20Don't%20Optimize%20for%20Virality.html)
- At Kimi he reportedly worked with Zhang Yu on GPU kernels for Kimi Delta Attention, studied training optimizers, and helped build demo cases for the K3 launch. — [BlockBeats](https://www.theblockbeats.info/flash/371927)

### Inferences
- 2023: a general student programmer (web, iOS, C++, OpenCV) with early interest in LLM evaluation (C-Eval/MMCU forks) and competitive programming tooling. No deep-ML work yet.
- 2024: applied ML projects (YOLO/RT-DETR detection, single-cell perturbation, shrimp-feed CV) and AI-safety/interpretability curiosity (ARENA fork). There are early signs of interest in architecture (nGPT, memory-layer, llm.c forks), but no kernel work.
- 2025 is the turning point. Within about four months (Apr–Jul 2025) he went from "day 3 of learning Triton" (May 11) to H100 Triton kernels for a custom attention variant (Co-ALIBI) and a TileLang FlashAttention he claims beats FA-2. By September he had merged a full model (DeltaFormer) into FLA.
- Likely trigger for Moonshot's attention: the DeltaFormer PR co-authored with Yu Zhang (Kimi Linear first author and FLA co-maintainer) and the viral Triton/FLA threads in September 2025, roughly two months before the November 2025 start. This is consistent with the media line that Kimi recruited him from FLA. No source directly says "this PR got him hired", so this is inference.
- The Tilde internship (summer 2025) came first and was set off by social posting (see next sections). The "viral" moment that preceded Kimi was technical tutorials plus real upstream code, not a standalone viral repo. None of his own repos has more than 39 stars.

### Gaps
- Exact PR discussion text, review comments and line-level authorship within co-authored PRs were not reviewed. The GitHub API was not available in this session; data comes from public git clones.
- Some of the 62 repos (beyond those listed on two pages) may be hidden or private. I did not determine whether "Encoded_reasoning_CoT" or "learn-triton" have meaningful content.
- I did not confirm whether he contributed code to Tilde's MoMoE release; only his fork is visible.

---

## Does he have a Zhihu account or personal blog with technical writing? What topics, and do any posts describe how he learned?

### Takeaway
He has **no Zhihu account that I could find**. His writing is in English on **nathanchen.me** (about 22 posts, Feb 2024 to Mar 2026), plus one Substack essay and about 11 Codeforces blog posts. The technical posts (May–Sept 2025) are hands-on GPU-kernel tutorials (Triton matmul with L2-cache tiling, `make_block_ptr`, a FlashAttention forward walkthrough using FLA's kernel, FlashAttention in TileLang) and an optimizer derivation (nuclear-norm "Tauon"). He also links two Tilde Research blog posts (MoMoE in Jul 2025; Gram-Space Manifold Muon in Oct 2025). The reflective posts give explicit accounts of how he learned.

### Cited Findings
**Blog index at nathanchen.me/public/blog.html (dates as shown on the index)** — [Blog index](https://nathanchen.me/public/blog.html)
- 3-16-2026 "Attention Residuals" (links to the arXiv paper)
- 10-13-2025 "Gram-Space Manifold Muon" (links to Tilde Research blog)
- 10-07-2025 "Twitter is Awesome, but Don't Optimize for Virality"
- 09-24-2025 "Triton Flash Attention Kernel Walkthrough: The Forward Pass"
- 09-22-2025 "Triton's make_block_ptr Explained: A Visual Guide"
- 09-13-2025 "Why 'Be Yourself' Is Incomplete Advice"
- 07-25-2025 "MoMoE: Memory-optimized Mixture of Experts" (links to Tilde Research blog)
- 07-19-2025 "Implementing Flash Attention in TileLang (1.3x Faster Than FA-2): Part 1"
- 05-11-2025 "Implementing Matrix Multiplication in Triton with L2 Cache Optimization"
- 05-04-2025 "Deriving and Implementing an Optimizer under the Nuclear Norm"
- 02-20-2025 "Cryptoforces?" (Codeforces cross-post)
- 02-08-2025 "Going Down the AI Alignment Rabbit Hole" (Substack)
- 01-15-2025 "Next-token-prediction-based Self-reflection"
- 12-10-2024 "[Project] What Did 2024 Look Like for You on Codeforces?"
- 2024 personal and CP posts: "Words Unwritten", "Practice Appreciation", "Why do I journal", "Beyond the wildest dreams of our ancestors", "It is true that we are having fewer contests", "I tried different warm-ups before competitive programming competitions...", "August To-Dos", "Insomnia, Snoring, and Decision Tree" (02-20-2024, the earliest)

**Technical post contents**
- Tauon optimizer (05-04-2025): "A day ago I was given a take-home assignment by an exciting startup working on applied interpretability... I need to derive and implement an optimizer that minimizes the approximation error under the nuclear norm. Then, I need to train a NanoGPT scale model." He calls the result "bad" (loss above 3 versus below 0.15 for the baseline), blames a sign error ("I optimized the nuclear norm in the opposite direction") and too low a rank, and says: "This was not a research-level project, but simply an experiment in which I learn by doing." — [Tauon post](https://nathanchen.me/public/Tauon-Optimizer.html)
- Triton matmul (05-11-2025): "Right now when I'm typing these letters down, I'm also just on day 3 of learning Triton from scratch!"; "When I was learning on my own, I turned to a great amount of tutorials and q&as with gpt." — [Triton matmul post](https://nathanchen.me/public/Triton-Matrix-Multiplication.html)
- FlashAttention in TileLang (07-19-2025): claims his TileLang kernel "achieves >1.3x speedup over FlashAttention-2, reaching 630 TFLOPS/s for 4K sequence lengths on NVIDIA H100 GPUs". Self-reported; not independently verified. — [TileLang FA post](https://nathanchen.me/public/Flash-Attention-Tilelang.html)
- `make_block_ptr` guide (09-22-2025) and FlashAttention walkthrough (09-24-2025): both teach with FLA's real kernels ("a Triton implementation of FLA's highly-optimized attention mechanism"), ending with "every ML algorithms should be hardware-aligned!" — [make_block_ptr post](https://nathanchen.me/public/Triton-make-block-ptr-Guide.html); [FA walkthrough](https://nathanchen.me/public/Triton-Flash-Attention-Kernel-Walkthrough.html)
- Substack "Going Down the AI Alignment Rabbit Hole" (Feb 8, 2025) covers outer alignment, human values (Shard Theory) and interpretability. It says it was written as the personal project for a five-day BlueDot "Writing Intensive" course. Sources cited include AI Safety Fundamentals, DeepMind's specification-gaming post, LessWrong, Transformer Circuits, Neel Nanda's Mech Interp guide and 3Blue1Brown. — [Substack post](https://nathancgy.substack.com/p/going-down-the-ai-alignment-rabbit)

**Codeforces blog (handle Nathan4; 11 posts Aug 2024–Jul 2025)** — [Codeforces API: user.blogEntries](https://codeforces.com/api/user.blogEntries?handle=Nathan4)
- "What Did 2024 Look Like for You on Codeforces?" (2024-12-06, +357, his highest-rated post) announced the cf_yearly_review tool. — [CF entry 137016](https://codeforces.com/blog/entry/137016)
- "Cryptoforces?" (2025-02-19, +188): humorous technical-analysis "trend lines" on Codeforces rating graphs, with a companion tool. — [CF entry 139776](https://codeforces.com/blog/entry/139776)
- "This is what job hiring processes should be like" (2025-07-08, +212) praises a hiring challenge (a graph-theory problem) from an "applied interpretability" startup and links to tilderesearch.com/challenges. — [CF entry 144584](https://codeforces.com/blog/entry/144584)
- Others: "Stop saying learning cp is useless in the real world" (2024-10-07), "Why no more rated contests?", "Useful tip for the upcoming Hacker Cup", and similar. — [CF entry 134864](https://codeforces.com/blog/entry/134864)

### Inferences
- His technical writing follows a "learn it, then teach it in public" pattern: each post documents something he had just learned (often days earlier) and is built around real production kernels (FLA, TileLang) rather than toy code. This is likely how both Tilde and the FLA/Kimi community came to know his work.
- Dates on some individual pages disagree with the index. The "Twitter is Awesome" page header reads 10-15-2024, but it discusses the September 2025 DeltaFormer merge, so the index date (10-07-2025) is correct. The writer should use index dates.

### Gaps
- The Tilde Research blog (MoMoE, Gram-Space Manifold Muon) returned HTTP 402 / "DEPLOYMENT_DISABLED" on 2026-10-15, so I could not confirm his byline or role on those two posts. His blog lists them as his writing, and he has a MoMoE fork.
- No Zhihu, Bilibili or Chinese-language technical writing by him was found. Chinese coverage of him is third-party (InfoQ, QbitAI, 经济参考报, Zhihu articles).
- The blog index's "Attention Residuals" entry just links to arXiv. I found no separate long-form post by him on AttnRes.

---

## What has he said publicly about how he learned ML (courses, papers, reproductions, mentors)?

### Takeaway
By his own account he started serious AI study in **February 2025**, after a hackathon. He learned by reading classic papers with **Gemini** as a tutor (screenshotting confusing passages), reading GitHub code, blogs and researchers' websites, and **deliberately skipping long multi-year video course sequences** as too slow. Mentors include a startup investor he met as a hackathon judge (Dong Kehan) and DeepSeek researcher **Yuan Jingyang** (first author of Native Sparse Attention). Earlier inputs: an AI-safety book (April 2024), a 10-day AI and rationality camp in the UK (August 2024), BlueDot's AI-safety writing course (early 2025), and forks of ARENA, ML-For-Beginners and llm.c. **No evidence of CS231n, CS336 or Karpathy's Zero to Hero specifically.**

### Cited Findings
- First-person essay (originally published 2025-09-21; reposted 2026-03-18): he says he knew nothing about Transformers or ML papers at first. He started from a classic paper and spent hours a day with Gemini, screenshotting confusing parts and asking it to explain. He saved and iterated on prompts and studied GitHub projects, blogs and researchers' personal websites "to understand their research taste". He skipped older, multi-year video course sequences as too slow. Key lines: "In this era, AI is the best teacher"; "you don't need to wait until you're ready to start". — [China Research Collective essay](https://chinaresearchcollective.substack.com/p/nathan-chen-from-hackathon-to-silicon)
- The same essay: at a February middle-school hackathon in Beijing his team "Third Arm" presented. Judge Dong Kehan (MiraclePlus, formerly YC China) asked "Will you do this technology later?" and later mentored him. Through Dong he was introduced to DeepSeek researcher Yuan Jingyang (first author of "Native Sparse Attention"), whom he consulted on big decisions. — [China Research Collective essay](https://chinaresearchcollective.substack.com/p/nathan-chen-from-hackathon-to-silicon)
- 经济参考报: he began studying AI in Feb 2025 after a middle-school hackathon in Beijing, where a judge connected him to a then-DeepSeek researcher, and he started reading papers with AI tools. — [jjckb](https://www.jjckb.cn/20260725/f1f27b8b4f9c40f3a4aa344a29e132bd/c.html)
- QbitAI: he did not know Transformers at first. Guided by DeepSeek researcher 袁境阳 (Yuan Jingyang), he used Gemini to study classic papers and followed GitHub open-source projects. FLA pulled him into papers, source code, Triton kernels and attention rewriting and acceleration. Before that he had tried cross-border e-commerce and short-video operations and switched to "底层技术" (foundational tech) on his mentor's advice. — [QbitAI](https://www.qbitai.com/2026/03/388493.html)
- His site lists "asking llms first" among things he likes, jokes about "learning from my sensei gemini", and says "everything is figureoutable with friends." — [nathanchen.me](https://nathanchen.me/)
- "Why 'Be Yourself' Is Incomplete Advice" (09-13-2025): in April 2024 he dropped activities he didn't enjoy, read "a book about AI safety" and read widely. In August 2024 he attended a 10-day "camp about AI and rationality" in the UK with 25 participants, where he was the youngest, and afterwards dug into "forums, Twitter (the knowledgeable part of it), blog posts... AI alignment and Fermi estimation." His recommended learning list includes "Learn about linear algebra", "Read recent research in the field you're interested in", "Ask AI chatbots when you're stuck", "Start tiny projects — The best way of learning something is by doing it", "Write thoughtful blogs (high-leverage!)" and "Cold outreach". He adds: "I got my first internship because of a tweet followed by a virtual call!" — [Be Yourself post](https://nathanchen.me/public/Be%20Yourself.html)
- "Twitter is Awesome...": "It helped me find my first job through a tweet"; "I started tweeting in April" (2025, by context). He advises: "Don't be the tutorial guy. Optimize for conversations, not impressions. Post what you're actually curious about (and your original thoughts & research!)." — [Twitter post](https://nathanchen.me/public/Twitter%20is%20Awesome,%20but%20Don't%20Optimize%20for%20Virality.html)
- Route to Tilde: he posted a reflection on a blog and shared it on X, the blog's author replied, and the CEO of a Silicon Valley AI startup (founded end of the prior year, $8M seed) saw it and reached out through his personal website. He got a one-week take-home, finished it the next day with "mediocre" results, and still received an offer. — [China Research Collective essay](https://chinaresearchcollective.substack.com/p/nathan-chen-from-hackathon-to-silicon); QbitAI adds that his X reflection on a blog got the author's reply and drew the startup CEO's attention — [QbitAI](https://www.qbitai.com/2026/03/388493.html)
- Tilde internship (summer 2025, 7 weeks in San Francisco): a team of fewer than 10, including 5 interns. In his final two weeks he owned an exploratory project with 144 H100s. He also helped with recruiting and HackerNews posts and talked with investor Vinod Khosla. The essay does not name the company; his GitHub and site say "prev at Tilde" / "applied interpretability research at Tilde Research". — [China Research Collective essay](https://chinaresearchcollective.substack.com/p/nathan-chen-from-hackathon-to-silicon); [GitHub](https://github.com/Nathancgy); [nathanchen.me](https://nathanchen.me/)

### Inferences
- His "curriculum" was mostly self-directed and project-driven: papers explained by an LLM, then reading production code (FLA, TileLang, ThunderKittens, modded-nanogpt forks), then reimplementing (Co-ALIBI kernels, TileLang FA, a Tauon/Muon comparison on NanoGPT), then upstreaming (FLA DeltaFormer). The forks double as a reading list: llm.c (Apr 2024), nGPT and memory layers (late 2024), forgetting transformer and stick-breaking attention (mid-2025).
- The Tauon post (May 4, 2025) is almost certainly the Tilde take-home: same "applied interpretability" startup description, same "finished in a day" story, "mediocre" results. Tilde's public hiring challenge was a math puzzle (graph theory), which fits his competitive-programming background.
- Mentorship and network were a large factor: hackathon judge, then a DeepSeek researcher, then Twitter, then Tilde, then FLA maintainers, then Kimi.

### Gaps
- He does not name the "classic paper" he started with, the AI-safety book, or the UK camp's organizer.
- No statement that he took CS231n, CS336, Karpathy's Zero to Hero, fast.ai and so on. The only "course" artifacts are BlueDot's writing course, plus ARENA and ML-For-Beginners forks (it is unclear whether he completed either).

---

## Does he have competitive programming or olympiad records?

### Takeaway
Yes. **Codeforces "Nathan4" is verified**: Candidate Master, max rating **2026**, reached on **2025-02-18**, over 48 rated contests since July 2022. It is self-linked from his GitHub. Baidu Baike claims USACO Platinum participation, which I could not verify. I found **no NOI/IOI or Chinese provincial olympiad records**.

### Cited Findings
- Codeforces API, user "Nathan4": rank "candidate master", rating 2026, maxRating 2026, maxRank "candidate master", contribution 60, registered 2022-07-17 (Unix 1658067033), last online around 2026-01-06. — [Codeforces API user.info](https://codeforces.com/api/user.info?handles=Nathan4); [profile](https://codeforces.com/profile/Nathan4)
- Rating history (48 rated contests) — [Codeforces API user.rating](https://codeforces.com/api/user.rating?handle=Nathan4):
  - Jul–Aug 2022: 0 → 1390 (7 contests)
  - Feb–Apr 2023: about 1300 → 1646 (Round 865, Apr 9, 2023)
  - Jan–Apr 2024: 1600 → 1823 (Round 931, Mar 1, 2024, rank 206)
  - Jul–Dec 2024: 1690 → 1944 (Round 994, Dec 20, 2024, rank 229)
  - **Educational Round 174, Feb 18, 2025: rank 143, 1944 → 2026 (peak; last rated contest)**
- He links his Codeforces profile from GitHub and says he "occasionally compete[s] in competitive programming". — [GitHub](https://github.com/Nathancgy)
- Baidu Baike says he took part in the USACO Platinum Division. — [Baidu Baike EN](https://baike.baidu.com/en/item/Chen%20Guangyu/3397209)
- A widely shared X post says he reached Codeforces Candidate Master, rating 2000+, and won first place at a 48-hour hackathon in March 2025. The same post contains other errors, and Baike and other sources contradict its background details. — [X @silverfang88](https://x.com/silverfang88/status/2033740106297667878)
- Hackathons: Feb 2025 "Third Arm" team at a middle-school hackathon in Beijing — [essay](https://chinaresearchcollective.substack.com/p/nathan-chen-from-hackathon-to-silicon). March 2025 "Moonshot 48 hackathon" project Figart-AI — [Figart-AI README](https://github.com/Nathancgy/Figart-AI). Baidu Baike instead says he "won the championship in Kimi's internal 48-hour hackathon" — [Baidu Baike EN](https://baike.baidu.com/en/item/Chen%20Guangyu/3397209).

### Inferences
- He peaked at Candidate Master in Feb 2025, exactly when he pivoted to AI, and has not played a rated contest since. CP was his pre-AI foundation (2022–2024), not a 2025 focus.
- The "48-hour hackathon" claims probably refer to the March 2025 "Moonshot 48" hackathon, where he built Figart-AI. Baike's "Kimi's internal hackathon" may be a mix-up of "Moonshot 48" with Moonshot AI. I could not confirm the organizer or that he placed first.

### Gaps
- No USACO results page was checked, so the Platinum claim is unverified. No AtCoder or LeetCode account was found (LeetCode blocked by Cloudflare). No NOI/CSP records found. Absence is not proof.

---

## What do Moonshot colleagues and others say publicly about his work?

### Takeaway
Public commentary is mostly media summaries of team accounts rather than direct quotes from colleagues. Su Jianlin proposed the original AttnRes idea; **Chen and Zhang Yu scaled it up and jointly proposed Block AttnRes**, the practical variant used in Kimi Linear 48B and K3. Chen himself publicly pushed back on the "prodigy" framing ("不要造神", don't mythologize). Musk's praise was aimed at the paper. Some Chinese tech communities were openly skeptical of the hype.

### Cited Findings
- Su Jianlin's account, as relayed by 经济参考报: after the initial results, Chen and Zhang Yu became interested and ran larger-scale experiments, and the two jointly proposed Block Attention Residuals (grouping layers into blocks to cut compute and communication costs). — [jjckb](https://www.jjckb.cn/20260725/f1f27b8b4f9c40f3a4aa344a29e132bd/c.html)
- BlockBeats: Su Jianlin first proposed replacing residuals with attention. Chen and Zhang proposed Block AttnRes, which made large-scale training feasible and was adopted by Kimi K3. Chen also worked with Zhang Yu on KDA GPU kernels and on optimizer research. — [BlockBeats](https://www.theblockbeats.info/flash/371927)
- Kimi's official X announcement describes AttnRes, Block AttnRes, a 1.25x compute advantage and less than 2% inference latency overhead. — [Kimi.ai on X](https://x.com/Kimi_Moonshot/status/2033378587878072424)
- Chen's own statement: "不要造神，希望外界少写个人、多写技术和团队，这是大家共同完成的成果" (don't mythologize; write less about me and more about the tech and the team). He thanked his two co-first authors and the scaling and infra colleagues as "缺一不可" (each indispensable). The Kimi team said the paper was a whole-team effort. — [InfoQ](https://www.infoq.cn/article/CI5daAFmzhA1IWN2Z6zD)
- QbitAI reports Elon Musk called the work "impressive" (令人印象深刻), that Marc Andreessen follows Chen's X account, and relays a Karpathy remark about understanding of "Attention is All You Need". The Karpathy remark is about the field, not Chen specifically. — [QbitAI](https://www.qbitai.com/2026/03/388493.html)
- Gave a talk on LLM pretraining and architecture at a Tsinghua Yao Class lecture on April 11, 2026, per Baike. Not independently verified. — [Baidu Baike EN](https://baike.baidu.com/en/item/Chen%20Guangyu/3397209)
- Skeptical voices: LINUX DO commenters asked "他做出什么成果了吗" (what has he actually achieved?) and "网友和媒体喜欢造神" (netizens and media like to make idols). — [LINUX DO](https://linux.do/t/topic/3026762). An 80aj.com piece (2026-07-24) called the "17-year-old built K3's core architecture" story marketing-account hype. It says there is no public code or papers, which is factually wrong given the arXiv paper and FLA commits, so it is a low-quality source. — [80aj](https://www.80aj.com/2026/07/24/genius-teen-tech-hype/)

### Inferences
- The most credible description of his contribution: co-first author who, with Zhang Yu, turned Su Jianlin's idea into a scalable system design (Block AttnRes) and ran the scaling experiments, alongside kernel work on KDA. Media claims that he "built K3's core architecture" or "improved efficiency 25%" go beyond what primary sources support (Kimi's own figure is a 1.25x compute advantage).
- His working relationship with Yu Zhang (yzhangcs) is documented in git history from Sept 2025 (DeltaFormer PR co-author), before he joined Kimi. This is the clearest public trace of "how Moonshot noticed him".

### Gaps
- I could not access X, so I found no direct quotes from Zhang Yu, Su Jianlin, Songlin Yang or other Kimi staff about Chen. Su Jianlin's blog (kexue.fm) was not checked for an AttnRes write-up naming him.
- No primary source on his role in Kimi K3 beyond AttnRes and KDA kernels. Whether he is a K3 tech-report author (arXiv 2607.24653) was not checked.
- The Anthropic (Scaling RL) move remains unconfirmed by any source found as of 2026-10-15.
