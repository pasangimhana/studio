# Chen Guangyu (陈广宇 / Guangyu Chen, "Nathan Chen", X: @nathancgy4): Papers, Technical Contributions, and Required Skill Set

Research date: 2026-10-15. Scope is professional/public work only. He is a minor, so personal, family and school details are deliberately left out.

Identity anchor used for verification: arXiv name "Guangyu Chen" + Kimi Team/Moonshot AI author lists (2026), GitHub `Nathancgy`, X `@nathancgy4`, personal site `nathanchen.me`. These are linked to each other by: the GitHub bio ("ML research at Kimi, prev at Tilde"), the X bio ("member of technical staff @kimi_moonshot, prev @tilderesearch"), the personal site's blog list, which includes the AttnRes paper and the Tilde MoMoE post, and BlockBeats, which ties his Oct-2026 departure post to x.com/nathancgy4. Sources: [GitHub](https://github.com/Nathancgy), [X profile via search index](https://x.com/nathancgy4), [nathanchen.me blog list](https://nathanchen.me/public/blog.html), [BlockBeats](https://www.theblockbeats.info/flash/371927).

---

## Q1. The "Attention Residuals" paper: bibliographic facts, his role, core idea, results, public reaction

### Takeaway
"Attention Residuals" (arXiv:2603.15031, v1 2026-03-16, Kimi Team, 37 named authors) lists Guangyu Chen first among three equal-contribution first authors (with Yu Zhang and Jianlin Su). The paper replaces the fixed, unit-weight residual sum in PreNorm Transformers with softmax attention over earlier layers' outputs ("attention over depth"). Its scalable variant, Block AttnRes, matches a baseline trained with about 1.25x more compute, has under 2% inference-latency overhead, and was validated on a 48B-total/3B-active Kimi Linear MoE trained on about 1.4T tokens. Several outlets report that Su Jianlin proposed the original idea and that Chen and Yu Zhang scaled it up and co-proposed Block AttnRes.

### Cited Findings
**Bibliographic facts**
- Title "Attention Residuals". Report header: "Technical Report of Attention Residuals", Kimi Team, with code at github.com/MoonshotAI/Attention-Residuals. arXiv:2603.15031 [cs.CL], v1 submitted Mon 16 Mar 2026 09:32 UTC, single version, comment field "attnres tech report". — [arXiv abs](https://arxiv.org/abs/2603.15031); [arXiv PDF v1](https://arxiv.org/pdf/2603.15031v1)
- Full author list in order: Kimi Team; Guangyu Chen, Yu Zhang, Jianlin Su, Weixin Xu, Siyuan Pan, Yaoyu Wang, Yucheng Wang, Guanduo Chen, Bohong Yin, Yutian Chen, Junjie Yan, Ming Wei, Y. Zhang, Fanqing Meng, Chao Hong, Xiaotong Xie, Shaowei Liu, Enzhe Lu, Yunpeng Tai, Yanru Chen, Xin Men, Haiqing Guo, Y. Charles, Haoyu Lu, Lin Sui, Jinguo Zhu, Zaida Zhou, Weiran He, Weixiao Huang, Xinran Xu, Yuzhi Wang, Guokun Lai, Yulun Du, Yuxin Wu, Zhilin Yang, Xinyu Zhou. — [arXiv abs](https://arxiv.org/abs/2603.15031)
- Appendix A "Contributions": "The authors are listed in order of the significance of their contributions, with those in project leadership roles appearing last." Guangyu Chen*, Yu Zhang* and Jianlin Su* are marked "* Equal contribution". The abs page and the GitHub citation block carry no equal-contribution marker; it appears only in the PDF appendix. — [arXiv PDF v1, Appendix A](https://arxiv.org/pdf/2603.15031v1); [GitHub README](https://github.com/MoonshotAI/Attention-Residuals)
- The repo had about 3.5k stars and 205 forks when captured on 2026-10-15. — [GitHub](https://github.com/MoonshotAI/Attention-Residuals)

**His specific role, as reported**
- Su Jianlin's account, relayed by 36Kr/投资界 (2026-03-25): the team first built a simpler version that clearly beat standard residuals. Chen and Zhang Yu then joined, verified it on a larger model, and helped propose Block AttnRes to cut the extra cost. — [36Kr EU](https://eu.36kr.com/en/p/3737678705967369)
- 中国新闻周刊 via ifeng (2026-08-07): per Su Jianlin, Chen and Zhang Yu proposed the Block Attention Residuals design, which groups layers into blocks and compresses block information to reduce compute and communication. — [ifeng](https://tech.ifeng.com/c/8vOAQCPnjzP)
- BlockBeats (2026-10-15): Su first proposed replacing residuals with attention. Chen and Zhang then proposed Block AttnRes so that it could be used in large-scale training, and it was later adopted in Kimi K3. — [BlockBeats](https://www.theblockbeats.info/flash/371927)
- He took part as a Kimi intern/researcher who joined in Nov 2025. He has publicly asked media not to "造神" (deify) him and has said the work was a team achievement. — [HK01, 2026-03-19](https://global.hk01.com/大国小事/60332002/马斯克激赞-深圳17岁高中生扬威ai界-领衔创-注意力残差-技术); [36Kr EU](https://eu.36kr.com/en/p/3737678705967369)
- The paper itself has no per-author contribution breakdown beyond the ordering rule and equal-contribution marks. — [arXiv PDF v1](https://arxiv.org/pdf/2603.15031v1)

**Problem addressed**
- With PreNorm, standard residuals add every layer's output with a fixed weight of 1. Hidden-state magnitude therefore grows as O(L) with depth and "progressively dilut[es] each layer's relative contribution" ("PreNorm dilution"). Later layers learn ever-larger outputs to gain influence, which can destabilize training. Each layer sees only one compressed state h_{l-1}, so there is no selective access (attention and MLP layers get the same mix), and information lost in the sum cannot be recovered later. — [arXiv PDF v1, §1–2](https://arxiv.org/pdf/2603.15031v1)
- The paper frames the problem as a "duality of time and depth": the residual stream behaves like an RNN over depth, compressing all prior information into one state. Transformers replaced RNN recurrence over time with attention, and AttnRes applies the same move to depth. Depth is small (L < 1000), so O(L²) attention over depth is affordable. — [arXiv PDF v1, §3](https://arxiv.org/pdf/2603.15031v1)

**Method (Full AttnRes)**
- h_l = Σ_{i=0}^{l-1} α_{i→l} · v_i, where v_0 = h_1 (the token embedding) and v_i = f_i(h_i) (layer outputs). The weights are a softmax over sources of φ(q_l, k_i) = exp(q_lᵀ RMSNorm(k_i)) with k_i = v_i. The query q_l = w_l is a single learnable "pseudo-query" vector per layer, so the weights depend on the input through the keys. The RMSNorm stops large-magnitude layers from dominating. Cost: O(L²d) arithmetic and O(Ld) memory per token. — [arXiv PDF v1, §3.1](https://arxiv.org/pdf/2603.15031v1)
- All pseudo-queries must be initialized to zero. AttnRes then starts as a uniform average, which "prevents training volatility". The method adds only one RMSNorm and one d-dim vector per layer. — [arXiv PDF v1, §5](https://arxiv.org/pdf/2603.15031v1)

**Method (Block AttnRes + systems work)**
- Layers are split into N blocks. Inside a block, outputs are summed as in a normal residual. Across blocks, each layer attends over the N block representations, the embedding, and the current intra-block partial sum. Memory and communication fall from O(Ld) to O(Nd), and about 8 blocks recovers most of Full AttnRes's gain. The README provides PyTorch-style `block_attn_res` pseudocode, applied before both the attention and the MLP sublayers. — [GitHub README](https://github.com/MoonshotAI/Attention-Residuals); [arXiv PDF v1, §3.2](https://arxiv.org/pdf/2603.15031v1)
- Infrastructure: (a) cross-stage caching for interleaved pipeline parallelism, which sends only incremental blocks between virtual stages so each block is stored once; (b) a two-phase computation in which Phase 1 runs batched inter-block attention for all layers of a block against cached block representations and Phase 2 folds in the intra-block part with an online-softmax merge, which allows kernel fusion; (c) memory-efficient prefilling. Training overhead is negligible without pipeline parallelism and under 4% end-to-end with it. Inference latency overhead is under 2% on typical workloads. — [arXiv PDF v1, §4](https://arxiv.org/pdf/2603.15031v1)

**Experiments and results**
- Scaling-law sweep: five MoE sizes from 194M to 528M activated parameters, 38.7B to 119B tokens, 8K context. Each size trains a PreNorm baseline, Block AttnRes (N=8), Full AttnRes and mHC(-lite), with hyperparameters tuned for the baseline. Fitted curves: Baseline 1.891·C^-0.057, Full 1.865·C^-0.057, Block 1.870·C^-0.058. At the largest size Block reaches loss 1.692 vs the baseline's 1.714, "equivalent to a 1.25× compute advantage". The Full–Block gap shrinks to 0.001. — [arXiv PDF v1, §5.1, Table 2](https://arxiv.org/pdf/2603.15031v1)
- Main model: the Kimi Linear 48B configuration, with 27 blocks (54 layers), KDA:MLA at 3:1, 8 of 256 routed experts plus 1 shared, and 48B total / 3B active. It uses Block AttnRes with 6 layers per block (9 blocks + embedding = 10 sources), the Muon optimizer, a WSD schedule and an 8M-token batch. Training was 1T tokens of pretraining, then about 400B tokens of mid-training, then extension to 32K context. The NoPE MLA meant no YaRN was needed. — [arXiv PDF v1, §5.2](https://arxiv.org/pdf/2603.15031v1)
- Downstream results (baseline → AttnRes): MMLU 73.5→74.6; GPQA-Diamond 36.9→44.4 (+7.5); BBH 76.3→78.0; TriviaQA 69.9→71.8; Math 53.5→57.1; HumanEval 59.1→62.2; MBPP 72.0→73.9; CMMLU 82.0→82.9; C-Eval 79.6→82.5. Block AttnRes "matches or outperforms the baseline on all benchmarks". — [GitHub README](https://github.com/MoonshotAI/Attention-Residuals); [arXiv PDF v1, §5.2](https://arxiv.org/pdf/2603.15031v1)
- Ablations on the 436M model, by validation loss: PreNorm baseline 1.766; DenseFormer (fixed scalar cross-layer weights) 1.767, i.e. no gain; mHC 1.747; sliding-window aggregation over the last 8 layers 1.764; Full AttnRes 1.737; Block AttnRes (S=4) 1.746. Block sizes S=2, 4 and 8 all land near 1.746, while S=16 and S=32 drift back toward the baseline. — [arXiv PDF v1, §5.3](https://arxiv.org/pdf/2603.15031v1)
- Training dynamics: AttnRes keeps per-block output magnitudes bounded and spreads gradient norms more evenly across layers. — [arXiv PDF v1, §5.2](https://arxiv.org/pdf/2603.15031v1); [GitHub README](https://github.com/MoonshotAI/Attention-Residuals)

**Public reaction**
- Elon Musk reposted or commented on the paper around 2026-03-16/17, calling it impressive. The Chinese rendering is "Kimi的工作令人印象深刻"; I did not retrieve the exact English text. — [HK01](https://global.hk01.com/大国小事/60332002/马斯克激赞-深圳17岁高中生扬威ai界-领衔创-注意力残差-技术); [36Kr EU](https://eu.36kr.com/en/p/3737678705967369); [深圳新闻网 2026-03-19](https://www.sznews.com/news/content/2026-03/19/content_31982765.htm)
- Kimi's official Weibo reportedly replied with a joke ("你的火箭造得也不错!", "your rockets are pretty good too"). Andrej Karpathy was reported as saying something like "We haven't really taken the title 'Attention is All You Need' seriously". Jerry Tworek (formerly OpenAI) reportedly called it "deep learning 2.0". All three come from secondary-outlet summaries; I did not see the original posts. — [IT之家](https://www.ithome.com/0/929/820.htm); [ifanr](https://www.ifanr.com/1658668); [36Kr EU](https://eu.36kr.com/en/p/3730463373476105)
- Chen's own X post about the paper: "It works on a frontier scale and is elegant, both in terms of the formula and the paper itself :)". — [X @nathancgy4](https://x.com/nathancgy4/status/2033390157102244098)
- Follow-up work cites and extends it, for example "Role-Decoupled Attention Residuals" (arXiv 2608.01075, Aug 2026), and Sebastian Raschka's LLM Architecture Gallery has an AttnRes entry. — [arXiv 2608.01075](https://arxiv.org/pdf/2608.01075); [Raschka gallery](https://sebastianraschka.com/llm-architecture-gallery/attention-residuals/)

### Inferences
- The ordering rule (most significant contribution first, leadership last) puts Chen first among equals, which supports a hands-on "made it work at scale" role (scaling verification plus the Block AttnRes design and infrastructure) rather than originating the idea. Media consistently credit the idea to Su Jianlin.
- Media figures such as "25% training efficiency" and "1.25x" both come from the paper's compute-equivalent claim at the largest small-scale sweep point. That claim is measured at ≤528M activated parameters, and the 48B run compares benchmarks, not compute multipliers.

### Gaps
- I could not see the verbatim Musk and Karpathy posts, so the wording comes from media.
- There is no per-person contribution statement in the paper. Role attribution relies on Su Jianlin's account as relayed by media.

---

## Q2. Complete verified list of his papers, tech reports and technical artifacts (and identity-confusion check)

### Takeaway
Only two arXiv papers can be confidently attributed to him: **Attention Residuals** (2603.15031, co-first author) and **Kimi K3: Open Frontier Intelligence** (2607.24653, one of about 400 alphabetically listed contributors). His other verifiable technical artifacts are blog-style or open-source: Tilde's **MoMoE** (Jul 2025, co-author as "Nathan Chen"), a Tilde vignette **"Gram-Space Manifold Muon"** (Oct 2025, listed on his site), several **Triton/TileLang kernel tutorials**, an **optimizer derivation post ("Tauon")**, and the **Co-ALIBI** Triton kernel repo. He is **not** on Kimi k1.5, Kimi-VL, Kimi K2, Kimi Linear (KDA), Kimi K2.5, Moonlight/Muon or MoBA. Many other 2025–2026 arXiv papers by a "Guangyu Chen" (robotics, navigation, MT, TTS) are almost certainly by different people.

### Cited Findings
**Confirmed (affiliation Kimi/Moonshot, 2026)**
1. **Attention Residuals**, arXiv:2603.15031, 2026-03-16. Co-first author (equal contribution, listed first). — [arXiv](https://arxiv.org/abs/2603.15031); [PDF Appendix A](https://arxiv.org/pdf/2603.15031v1)
2. **Kimi K3: Open Frontier Intelligence**, arXiv:2607.24653, v1 2026-07-27 (now v2), Kimi Team, 402 author entries including "Kimi Team". Appendix A "Contributions" says "The listing of contributors is in alphabetical order based on their last names", and "Guangyu Chen" appears between Guanduo Chen and Guanzheng Chen. No per-person roles are given. — [arXiv 2607.24653](https://arxiv.org/abs/2607.24653) (author list and appendix checked via arXiv API and arXiv HTML on 2026-10-15)

**Checked and NOT authored by him** (exact-name match of "Guangyu Chen" against arXiv author lists, done 2026-10-15 via the arXiv API)
- Kimi K2.5: Visual Agentic Intelligence (2602.02276, 2026-02-02, 337 authors): not listed.
- Kimi Linear: An Expressive, Efficient Attention Architecture (2510.26692, 2025-10-30, 60 authors; this is the KDA paper): not listed.
- Kimi K2: Open Agentic Intelligence (2507.20534): not listed.
- Kimi-VL Technical Report (2504.07491): not listed.
- Kimi k1.5: Scaling RL with LLMs (2501.12599): not listed.
- Moonlight/Muon and MoBA (Feb 2025) do not appear in arXiv's au:"Guangyu Chen" results. — [arXiv API query au:"Kimi Team"](https://export.arxiv.org/api/query?search_query=au:%22Kimi%20Team%22&max_results=60&sortBy=submittedDate&sortOrder=descending); [arXiv API query au:"Guangyu Chen"](https://export.arxiv.org/api/query?search_query=au:%22Guangyu%20Chen%22&max_results=80&sortBy=submittedDate&sortOrder=descending)

**Pre-Moonshot and side technical artifacts (as "Nathan Chen")**
3. **MoMoE: Memory-optimized Mixture of Experts**, Tilde Research blog, 2025-07-25. Credited authors: Bobby Costin, Timor Averbuch, Dhruv Pai, Nathan Chen, Ben Keigwin (per the SonicMoE paper's reference list). It is an MoE implementation with fused Triton kernels, optimized memory packing and a configurable backward pass for memory/compute trade-offs. The authors claim it outperforms baselines such as NVIDIA TE-Grouped and ScatterMoE, with code at Tilde's GitHub (`momoe-release`). SonicMoE (arXiv 2512.14080, ICLR 2026, Tri Dao, Ion Stoica et al.) cites it as prior work. — [Tilde blog (blocked, 402)](https://blog.tilderesearch.com/blog/momoe); [SonicMoE arXiv](https://arxiv.org/html/2512.14080); [nathanchen.me blog list](https://nathanchen.me/public/blog.html); [Alexandru Costin on X](https://x.com/acostin/status/2001846235985314034?lang=en)
   - ifeng (2026-08-07) says he worked on MoMoE during a seven-week Tilde internship in July 2025 and had already written custom Triton training kernels before applying. — [ifeng](https://tech.ifeng.com/c/8vOAQCPnjzP)
4. **Gram-Space Manifold Muon**, Tilde Research "vignette", 2025-10-13, listed on his blog page. It appears to be a Muon/manifold-optimizer variant. I could not fetch it to confirm the author list or content. — [nathanchen.me blog list](https://nathanchen.me/public/blog.html)
5. Kernel tutorials on his blog: "Triton Flash Attention Kernel Walkthrough: The Forward Pass" (2025-09-24); "Triton's make_block_ptr Explained: A Visual Guide" (2025-09-22); "Implementing Flash Attention in TileLang (1.3x Faster Than FA-2): Part 1" (2025-07-19); "Implementing Matrix Multiplication in Triton with L2 Cache Optimization" (2025-05-11). — [nathanchen.me blog list](https://nathanchen.me/public/blog.html)
   - His X post claims fewer than 100 lines of TileLang reached about 630 TFLOPS for softmax attention forward, about 1.3x FlashAttention-2. — [X @nathancgy4](https://x.com/nathancgy4/status/1972613835598299245)
6. "Deriving and Implementing an Optimizer under the Nuclear Norm" ("Tauon" optimizer), 2025-05-04. — [nathanchen.me blog list](https://nathanchen.me/public/blog.html)
7. "Next-token-prediction-based Self-reflection" (experiment post), 2025-01-15; "Going Down the AI Alignment Rabbit Hole" (Substack), 2025-02-08. — [nathanchen.me blog list](https://nathanchen.me/public/blog.html)
8. **Co-ALIBI**: a GitHub repo of "hardware-aligned Triton kernels for Co-ALIBI (contextual attention with linear biases)" (9 stars). **gestureX** (OpenTeens org): a hand-gesture recognition project using simple MLPs (39 stars). — [GitHub Nathancgy](https://github.com/Nathancgy)
9. **flash-linear-attention (fla-org)** is pinned on his GitHub. A third-party profile calls him a "core contributor", but I could not verify this; the GitHub contributor API was not accessible from this session. — [GitHub Nathancgy](https://github.com/Nathancgy); [Lessie profile (aggregator, low reliability)](https://profile.lessie.ai/guangyu-chen)
10. A May 2025 technical analysis of DeltaNet/linear attention, posted on X according to ifeng, reportedly drew a reply from Songlin Yang (DeltaNet/FLA). I could not locate the original. — [ifeng](https://tech.ifeng.com/c/8vOAQCPnjzP)
11. Talk: on 2026-04-11 he gave a Tsinghua Yao Class lecture on LLM pretraining and architecture, described as a researcher on Kimi's "Scaling Team". — [Baidu Baike EN](https://baike.baidu.com/en/item/Chen%20Guangyu/3397209)

**Same-name papers that are almost certainly not him** (arXiv, 2025–2026)
- Robotics and embodied AI: MM-ABC (2609.35652), MoPA (2609.12081, first author "Guangyu Chen"), Learning Human-Intention Priors (2604.24681), RoboStereo (2603.12639), Master Micro Residual Correction (2603.15152), XPolicyLab (2608.09892), Trustworthy Embodied Intelligence (2607.26121), Universal Visuo-Tactile Video Understanding (2505.22566), VOTE VLA (2507.05116).
- Visual navigation: 2603.26741, 2510.08713, 2508.09547, and the anti-UAV survey 2504.11967.
- Machine translation: "Quit While You're Ahead" (2609.00588, first author "Guangyu Chen", with Kamigaito).
- Speech: GLM-TTS Technical Report (2512.14291, Zhipu).
- Biology: Cell Behavior Video Classification Challenge (2601.10250). — [arXiv API query au:"Guangyu Chen"](https://export.arxiv.org/api/query?search_query=au:%22Guangyu%20Chen%22&max_results=80&sortBy=submittedDate&sortOrder=descending)

### Inferences
- These same-name papers involve different co-author networks and fields (robotics, MT, TTS), and none carries a Moonshot/Kimi link or mentions it in media coverage. Anyone attributing them to him (for example, via an auto-merged Google Scholar or Semantic Scholar profile) is probably making an identity error. The Semantic Scholar author search returned 40 "Guangyu Chen" profiles, and none clearly matched the Kimi papers by keyword (2026-10-15).
- His "publication record" is therefore thin in count but high in impact: one first-author architecture paper, one frontier-model tech report credit, and a strong public trail of kernel and optimizer engineering writing.

### Gaps
- Google Scholar, DBLP and OpenReview pages were not checked directly (time budget). The Semantic Scholar API search gave no clear match.
- The MoMoE and Gram-Space Manifold Muon author lists could not be read from the Tilde site (HTTP 402). The MoMoE authorship comes from the SonicMoE reference list.
- No modded-nanogpt speedrun records or Kaggle work were found. His GitHub doesn't list modded-nanogpt.

---

## Q3. What his Kimi K3 architecture work involved (as publicly described)

### Takeaway
K3 (2.8T total / 104B active MoE, 1M context; announced around 2026-07-17, tech report on arXiv 2026-07-27) is built on Kimi Delta Attention and Attention Residuals. Chen's documented K3-relevant contributions are: (1) Block AttnRes, which went into K3's depth-wise information flow and its memory-efficient training and inference implementation; (2) work with Yu Zhang on accelerating KDA GPU kernels; (3) optimizer research; and (4) launch showcase examples. These come from media and his own site. The K3 report itself credits contributors alphabetically, with no roles.

### Cited Findings
- K3 abstract: a "2.8T parameter Mixture-of-Experts model with 104 billion activated parameters, native vision capabilities, and a 1-million-token context window... built on Kimi Delta Attention and Attention Residuals". With Stable LatentMoE (16 of 896 routed experts per token) and refined recipes, it claims "approximately 2.5x improvement in overall scaling efficiency over Kimi K2". The infrastructure includes "algorithm-system co-design for KDA" and "million-token agentic RL with persistent rollout and sandbox states". — [arXiv 2607.24653](https://arxiv.org/abs/2607.24653)
- Architecture details (third-party reading of the report): 93 layers, each block has three KDA layers and one Gated MLA layer (69 KDA + 24 MLA); KDA head dim 128 with a 128×128 recurrent state per head and per-channel decay; MLA kv_lora_rank 512. MoE: 896 routed + 2 shared experts, 16 active; Quantile Balancing for routing; SiTU-GLU; FlashKDA CUTLASS kernels (SM90+); MoonEP expert parallelism; AgentENV Firecracker sandboxes. — [Code Pointer, 2026-07-30](https://codepointer.dev/p/how-kimi-k3-engineered-its-way-to)
- In K3, AttnRes "enable[s] each module to selectively retrieve representations from the embedding, the current block, and preceding blocks". The report has sections on Full and Block AttnRes. Training uses a "memory-efficient attention residual": block representations are made once at block boundaries, the AttnRes computation is wrapped in checkpointing so per-layer saved activations match a standard residual, and AttnRes's cache-based pipeline communication is reused. Inference uses dedicated Block AttnRes kernels: sequence parallelism, so block representations are materialized on one TP rank, a side-stream inter-block kernel during decode, and the intra-block merge plus RMSNorm fused into the TP all-reduce. The MTP speculative-decoding draft model takes features from the 1st, 4th and final AttnRes blocks. — [arXiv 2607.24653 (HTML §2.2, §5, §5.4.2)](https://arxiv.org/abs/2607.24653)
- The report also covers Per-Head Muon (§2.5), a dedicated scaling-law study that retunes batch size, LR, tokens-per-parameter and model shape (cosine decay was preferred over WSD), and RL via partial rollouts with per-token regularization for stale off-policy data, following the K2.5 algorithm, plus reasoning-effort budget control and multi-teacher on-policy distillation. — [arXiv 2607.24653](https://arxiv.org/abs/2607.24653); [Code Pointer](https://codepointer.dev/p/how-kimi-k3-engineered-its-way-to)
- In the report's kernel case study, K3 itself optimized an AttnRes kernel from 283.6 ms to 114.4 ms latency. The nano-KPU chip demo uses "Block AttnRes with a block size of two". — [arXiv 2607.24653](https://arxiv.org/abs/2607.24653)
- Contributor list: alphabetical, with no roles. — [arXiv 2607.24653 Appendix A](https://arxiv.org/abs/2607.24653)
- Media accounts of his K3 role: K3's two core architectures are AttnRes and KDA, and early at Kimi he "worked on accelerating the KDA compute kernels" ([ifeng / 中国新闻周刊, 2026-08-07](https://tech.ifeng.com/c/8vOAQCPnjzP)). BlockBeats adds that he optimized KDA GPU kernels with Zhang Yu, researched training optimizers, and helped make showcase examples for the K3 launch ([BlockBeats, 2026-10-15](https://www.theblockbeats.info/flash/371927)). His site says he "works on LLM scaling and pretraining, including Kimi K3" ([nathanchen.me](https://nathanchen.me)). Baidu Baike places him on Kimi's "Scaling Team" in 2026 ([Baidu Baike EN](https://baike.baidu.com/en/item/Chen%20Guangyu/3397209)).
- Release timing: CNBC reported the unveiling on 2026-07-17 ([CNBC](https://www.cnbc.com/2026/07/17/moonshot-ai-kimi-k3-model-openai-anthropic-china.html)), while the arXiv tech report v1 is dated 2026-07-27 ([arXiv](https://arxiv.org/abs/2607.24653)).

### Inferences
- "Contributed to K3's foundational architecture" is best supported in a specific sense: Block AttnRes, which he co-designed, is one of K3's two headline architectural components, and he reportedly worked on KDA kernel performance. Claims that he "led" or "designed" K3 have no support.
- His K3 work sits in pretraining architecture, kernels and scaling, not post-training RL. That makes an RL-scaling role a shift in focus, though it draws on the same large-scale experimentation and systems skills.

### Gaps
- There is no primary source (report or Moonshot statement) on his exact K3 tasks. The media accounts are secondary and partly based on his own posts.

---

## Q4. Pre-Moonshot work, and the reported move to Anthropic ("Scaling RL MTS") and what that role means

### Takeaway
Before Moonshot he built a public trail of kernel and optimizer write-ups (Triton/TileLang FlashAttention, matmul, nuclear-norm optimizer, DeltaNet analysis) and did a summer-2025 Tilde Research internship (MoMoE). He joined Kimi in Nov 2025. On **2026-10-15 he announced on X that he has left Moonshot**, without naming his next employer. **I found no reliable source confirming that he joined Anthropic, or the title "Scaling RL Member of Technical Staff"**; the only hint is forum speculation. Anthropic does run "RL Scaling Science" and "RL Frontiers" research-engineering teams focused on how RL behaves as model size, compute and task horizon scale.

### Cited Findings
**Pre-Moonshot timeline (professional)**
- About Feb 2025 he presented a "ThirdArm" project at a student hackathon in Beijing, which led to mentorship and selection for a future-leaders program associated with 奇绩创坛 (Miracle Plus) figure 董科含. Accounts differ: ifeng says a Beijing student hackathon, 36Kr says a high-school hackathon, and a search summary says a Moonshot-hosted secondary-school AI hackathon. — [ifeng](https://tech.ifeng.com/c/8vOAQCPnjzP); [36Kr EU](https://eu.36kr.com/en/p/3737678705967369)
- He self-studied ML from about early 2025 by reading papers and following GitHub open-source projects. His X technical posts drew a Silicon Valley startup CEO's attention, which led to a seven-week US internship. — [HK01](https://global.hk01.com/大国小事/60332002/马斯克激赞-深圳17岁高中生扬威ai界-领衔创-注意力残差-技术)
- His learning method, quoted from a July 2025 post: "我没有系统地学习Triton……更有效的方法是：找到一篇相关的论文，理解它的算法，阅读FLA上的Triton代码。" ("I didn't study Triton systematically… the more effective way is to find a relevant paper, understand its algorithm, then read the Triton code in FLA.") — [ifeng](https://tech.ifeng.com/c/8vOAQCPnjzP)
- Tilde Research (Palo Alto), July 2025: a seven-week internship on MoMoE. His X and GitHub bios say "prev @tilderesearch", and his site says "applied interpretability research" at Tilde. — [ifeng](https://tech.ifeng.com/c/8vOAQCPnjzP); [GitHub](https://github.com/Nathancgy); [nathanchen.me](https://nathanchen.me)
- An aggregator claims he "managed a project using 144 H100 GPUs" during the internship. This is unverified. — [Lessie (aggregator)](https://profile.lessie.ai/guangyu-chen)
- Competitive programming: USACO Platinum division ([Baidu Baike EN](https://baike.baidu.com/en/item/Chen%20Guangyu/3397209)). An X post claims Codeforces Candidate Master, rated 2000+, but this is unverified ([X @silverfang88](https://x.com/silverfang88/status/2033740106297667878)). He blogged Codeforces analyses in 2024–2025 ([nathanchen.me blog](https://nathanchen.me/public/blog.html)). He won Kimi's internal 48-hour hackathon ([Baidu Baike EN](https://baike.baidu.com/en/item/Chen%20Guangyu/3397209)).
- Joined Kimi in Nov 2025, first as an intern according to HK01 and as an "ML researcher" according to other sources. — [HK01](https://global.hk01.com/大国小事/60332002/马斯克激赞-深圳17岁高中生扬威ai界-领衔创-注意力残差-技术); [36Kr EU](https://eu.36kr.com/en/p/3737678705967369)
- Note: some write-ups describe his Silicon Valley internship as being at "a startup with deep ties to OpenAI and Anthropic". That is not employment at Anthropic.

**Departure from Moonshot (2026-10-15)**
- On 2026-10-15 he posted on social media that he had "recently" left Moonshot: "过去一年在Kimi的工作是我迄今为止最美好的时光" ("the past year at Kimi has been the best time of my life so far"). He did not disclose a reason or a destination. 扬子晚报 speculated he may be leaving for university. — [扬子晚报/yzwb, 2026-10-15](https://www.yzwb.net/news/txs/202610/t20261015_402791.html); [BlockBeats](https://www.theblockbeats.info/flash/371927) (links the original post at x.com/nathancgy4/status/2110522061953327565, which I could not fetch: HTTP 402)
- Baidu Baike (EN) records "October 2026: Left Moonshot AI" with no destination. — [Baidu Baike EN](https://baike.baidu.com/en/item/Chen%20Guangyu/3397209)
- Forum commenters guessed "A/" (Anthropic) because the screenshot showed San Francisco. This is speculation only. — [locdd forum thread 100607](https://www.locdd.com/t/topic/100607); [locdd thread 100431](https://www.locdd.com/t/topic/100431)
- Targeted searches (EN and ZH) for "Guangyu Chen" / "陈广宇" with "Anthropic", "Member of Technical Staff" or "Scaling RL" returned nothing linking him to Anthropic as of 2026-10-15.
- Context that makes the claim notable and unverified: in Sept 2026 Anthropic published a threat-intelligence report accusing Moonshot of silently routing Kimi user requests to Claude ([X @CausMoney summary](https://x.com/CausMoney/status/2098496988413120769)). A White House OSTP director alleged Moonshot distilled Anthropic's model for K3 ([Techmeme 2026-07-22](https://www.techmeme.com/260722/p32)). Both are secondary summaries. A Moonshot→Anthropic hire would likely draw coverage, and none was found.
- Possible source of the "MTS" title: his X bio already read "member of technical staff @kimi_moonshot". — [X profile via search](https://x.com/nathancgy4)

**What "Scaling RL" means at Anthropic (job postings)**
- "Research Engineer, RL Scaling Science" (London, hybrid ≥25% in office; posted 2026-06-26; now closed; £375k–£640k). The team "studies how reinforcement learning behaves as we scale it" across model size, compute and task horizon, and turns findings into training recipes for frontier models, "at the boundary between research and engineering". Responsibilities: design, run and interpret large-scale RL experiments; study how RL improves with horizon, compute and model size; build reproducible long-horizon RL benchmarks; turn validated findings into production recipes; debug failures that only appear at scale. Minimum qualifications: strong empirical research skills in RL or large-scale training, owning large experiments end to end, Python, distributed ML systems, comfort debugging at the research/systems boundary. Preferred: published or shipped long-horizon RL work, frontier-scale training runs with long trajectories. Example projects: a long-horizon RL benchmark suite that separates real gains from eval artifacts; stress-testing a finding across scales; tracing an unexpected RL scaling trend to its root cause across algorithm, data and infrastructure. — [General Catalyst job board copy](https://jobs.generalcatalyst.com/companies/anthropic/jobs/84256372-research-engineer-rl-scaling-science)
- "Research Engineer / Research Scientist, RL Frontiers": per a search summary, it studies how RL scales, including what happens to throughput, stability and learning efficiency as models grow, rollouts lengthen and compute increases by orders of magnitude. — [General Catalyst listing](https://jobs.generalcatalyst.com/companies/anthropic/jobs/95309553-research-engineer-research-scientist-rl-frontiers) (not fetched directly)
- Anthropic uses "Member of Technical Staff" as a generic title across research and engineering. — e.g. [Processing Foundation bio](https://processingfoundation.org/people/chan-jun-shern/)

### Inferences
- The defensible statement as of 2026-10-15 is: he left Moonshot (self-announced on 2026-10-15) and his destination is unconfirmed, with forum speculation pointing to Anthropic or a San Francisco employer. Any write-up should say "reportedly" and not state the Anthropic role as fact.
- If the Anthropic move is true, a Scaling-RL role would build on his demonstrated strengths: scaling-law methodology, large-run debugging, and kernel and systems efficiency. RL-specific expertise (policy optimization, long-horizon rollouts, reward design) is not visible in his public record, and K3's RL work is credited only at team level.

### Gaps
- I could not read the original departure post or any confirmation (LinkedIn or Anthropic) of the new role, team or start date.

---

## Q5. Concrete technical skill set implied by this body of work (for a learning roadmap)

### Takeaway
His work spans five layers: (1) **Transformer internals**, especially the residual stream, normalization and attention variants (softmax, MLA, linear/delta-rule attention); (2) **optimizers and scaling-law methodology** (Muon family, LR schedules, compute-equivalent comparisons); (3) **GPU kernel engineering** (Triton, TileLang, CUTLASS-level ideas, FlashAttention-style online softmax, memory-bound optimization); (4) **large-scale distributed training and inference systems** (pipeline, tensor, sequence and expert parallelism, checkpointing, KV and prefix caching, speculative decoding); and (5) for Scaling RL, **RL for LLMs at scale** (policy optimization under off-policy staleness, partial rollouts, long-horizon agentic RL, reward design, RL scaling experiments). His own learning path ran from paper to algorithm to reading production Triton code (FLA), with public write-ups along the way.

### Cited Findings (each skill tied to the source that requires it)
1. **Residual stream, normalization and gradient flow.** PreNorm vs PostNorm, RMSNorm, why PreNorm hidden states grow O(L), the Jacobian product view of residual gradients, Highway gating, DenseFormer, Hyper-Connections/mHC. — [AttnRes PDF §2, §5.3](https://arxiv.org/pdf/2603.15031v1)
2. **Attention mechanics and variants.** Softmax attention as a kernel φ(q,k), online softmax (the FlashAttention trick, used in AttnRes's two-phase merge), the KV cache, MLA with NoPE, and linear attention: DeltaNet, Gated DeltaNet and KDA with its chunkwise-parallel form, per-channel decay and fixed recurrent state. — [AttnRes PDF §3–4](https://arxiv.org/pdf/2603.15031v1); [K3 report §2.1](https://arxiv.org/abs/2607.24653); [DeltaNet paper 2406.06484](https://arxiv.org/html/2406.06484v2); [Songlin Yang "DeltaNet Explained"](https://sustcsonglin.github.io/blog/2024/deltanet-2/)
3. **Mixture-of-Experts.** Routing, shared experts, load balancing (Quantile Balancing), grouped GEMM, MoE memory and backward trade-offs (MoMoE), expert parallelism (MoonEP). — [K3 report §2.3](https://arxiv.org/abs/2607.24653); [SonicMoE (cites MoMoE)](https://arxiv.org/html/2512.14080); [Code Pointer](https://codepointer.dev/p/how-kimi-k3-engineered-its-way-to)
4. **Optimizers and schedules.** Muon (orthogonalized updates), Per-Head Muon, manifold Muon variants, nuclear-norm steepest descent ("Tauon"), WSD vs cosine decay. — [AttnRes PDF §5.2 (Muon, WSD)](https://arxiv.org/pdf/2603.15031v1); [K3 report §2.5, §3.2](https://arxiv.org/abs/2607.24653); [nathanchen.me blog list](https://nathanchen.me/public/blog.html)
5. **Scaling-law experimentation.** Sweeping model sizes and tokens, fitting L = A·C^-α, comparing variants at matched compute ("1.25× compute advantage"), giving all variants the baseline's tuned hyperparameters, architecture-shape sweeps at fixed FLOPs, retuning batch size, LR and tokens-per-parameter for a new family. — [AttnRes PDF §5.1, Fig. 7](https://arxiv.org/pdf/2603.15031v1); [K3 report §3.2](https://arxiv.org/abs/2607.24653)
6. **Training-dynamics diagnostics.** Per-layer output-magnitude and gradient-norm analysis, zero-init tricks for stability. — [AttnRes PDF §5](https://arxiv.org/pdf/2603.15031v1)
7. **GPU kernel engineering.** Triton (block pointers, L2-cache-aware tile ordering for matmul, FlashAttention forward), TileLang, CUTLASS kernels (FlashKDA on SM90+), roofline and memory-traffic reasoning, kernel fusion, side-stream overlap. — [nathanchen.me blog list](https://nathanchen.me/public/blog.html); [K3 report §5.4.2](https://arxiv.org/abs/2607.24653); [ifeng quote on learning Triton via FLA](https://tech.ifeng.com/c/8vOAQCPnjzP)
8. **Distributed training.** Interleaved 1F1B pipeline parallelism with virtual stages, cross-stage caching, activation checkpointing and recomputation, tensor parallelism with sequence parallelism (reduce-scatter/all-gather), expert parallelism, memory balancing across PP ranks. — [AttnRes PDF §4](https://arxiv.org/pdf/2603.15031v1); [K3 report §5](https://arxiv.org/abs/2607.24653)
9. **Inference systems.** Paged KV and prefix caching for hybrid KDA+MLA, prefill/decode disaggregation, MTP-based speculative decoding, quantization-aware post-training (MXFP4), inference-latency budgeting (AttnRes under 2%). — [K3 report §4.1.4, §5.4](https://arxiv.org/abs/2607.24653); [AttnRes PDF §4](https://arxiv.org/pdf/2603.15031v1)
10. **RL for LLMs at scale (the target role).** Policy-gradient methods with per-token regularization for stale off-policy data, partial rollouts, sandboxed agentic RL (Firecracker microVMs, pause/fork/resume), generative reward models, reasoning-effort/token-budget control, multi-teacher on-policy distillation. The Anthropic role adds long-horizon RL benchmark design, RL scaling-trend analysis across size, compute and horizon, and debugging at the research/infrastructure boundary. — [K3 report §4.1.2–4.1.3, §5.3](https://arxiv.org/abs/2607.24653); [Code Pointer](https://codepointer.dev/p/how-kimi-k3-engineered-its-way-to); [Anthropic RL Scaling Science posting](https://jobs.generalcatalyst.com/companies/anthropic/jobs/84256372-research-engineer-rl-scaling-science); [Kimi k1.5 (2501.12599), Moonshot's earlier RL-scaling report](https://arxiv.org/abs/2501.12599)
11. **Foundations.** Algorithms and competitive programming (USACO Platinum, Codeforces), Python and PyTorch fluency, reading open-source research code (FLA). — [Baidu Baike EN](https://baike.baidu.com/en/item/Chen%20Guangyu/3397209); [GitHub Nathancgy](https://github.com/Nathancgy); [ifeng](https://tech.ifeng.com/c/8vOAQCPnjzP)
12. **Career-building behavior.** Public technical writing and X threads (kernel tutorials, a DeltaNet analysis) led directly to the Tilde internship, and through it to Kimi. — [HK01](https://global.hk01.com/大国小事/60332002/马斯克激赞-深圳17岁高中生扬威ai界-领衔创-注意力残差-技术); [ifeng](https://tech.ifeng.com/c/8vOAQCPnjzP)

### Inferences
Suggested roadmap ordering, derived from the dependencies above:
1. **Foundations.** Python, PyTorch, linear algebra, probability, algorithms; implement a GPT from scratch (nanoGPT-style).
2. **Transformer internals.** Residuals, PreNorm and RMSNorm; reproduce the AttnRes idea at small scale (the README pseudocode is a good exercise); then study MLA and NoPE.
3. **Efficient attention.** FlashAttention (online softmax), then the linear-attention lineage: linear attention, DeltaNet, Gated DeltaNet, KDA. Read the FLA code.
4. **Kernels.** Triton matmul, then FlashAttention forward in Triton, then TileLang/CUTLASS, with roofline analysis. Reproduce his blog exercises.
5. **Optimizers and scaling laws.** Muon, then manifold and per-head variants. Run a small scaling sweep and fit power laws, with compute-matched comparisons.
6. **MoE and distributed systems.** Routing and load balancing, grouped GEMM; pipeline, tensor, sequence and expert parallelism; activation checkpointing (Megatron/DeepSpeed-level understanding).
7. **RL for LLMs.** Policy gradients (PPO/GRPO), off-policy corrections, verifiable rewards, agentic and sandboxed RL, long-horizon credit assignment; read the Kimi k1.5, K2, K2.5 and K3 post-training sections. Run RL scaling experiments (performance vs compute and horizon) and practice benchmark hygiene.
8. **Public output.** Blog or replicate each step publicly, as he did.

The gap between his public record and the reported Scaling-RL role is RL-specific depth. A roadmap aimed at a similar role should weight item 7 more heavily than his own path did.

### Gaps
- No public source details his personal RL experience. The RL skill list is derived from K3's team-level post-training section and Anthropic's job posting, not from his own work.
- The Anthropic "Scaling RL MTS" posting itself (as opposed to "Research Engineer, RL Scaling Science") was not found under that exact title.
