# SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

## 1. Bibliographic record

| Field | Value |
|---|---|
| Title | SWE-bench: Can Language Models Resolve Real-World GitHub Issues? (proceedings capitalisation: "Real-world Github Issues") |
| Authors | Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan |
| First public version | arXiv 2310.06770v1, 2023-10-10 |
| Version read | 2310.06770v3 (PDF header: "Published as a conference paper at ICLR 2024") |
| Venue | International Conference on Learning Representations (ICLR) 2024 |
| URL | https://proceedings.iclr.cc/paper_files/paper/2024/hash/edac78c3e300629acfe6cbe9ca88fb84-Abstract-Conference.html ; https://arxiv.org/abs/2310.06770 ; data and leaderboard https://www.swebench.com |
| DOI | None found |
| BibTeX key | `jimenez2024swebench` |
| Evidence class | **[PR]** peer-reviewed |
| Verified via | arXiv API and PDF; ICLR 2024 proceedings index on proceedings.iclr.cc (2026-10-14) |

## 2. Research question

Can language models resolve real software issues in real repositories, a task that requires understanding large codebases, coordinating multi-file edits, and producing changes validated by execution? And can such a task serve as a durable, hard benchmark?

## 3. Method

- **Construction pipeline** (§2.1): (I) about 90,000 pull requests scraped from 12 popular Python repositories; (II) keep merged PRs that resolve an issue and change test files; (III) execution-based filtering that keeps only instances with at least one *fail-to-pass* test and without installation or runtime errors. Result: **2,294 task instances**.
- **Task formulation** (§2.2): input = issue text plus full codebase; output = a patch; success = the patch applies and the associated tests pass. The metric is the **percentage of instances resolved**.
- **Training data:** SWE-bench-train, about 19,000 issue-PR pairs from repositories *disjoint* from the evaluation set, used to fine-tune **SWE-Llama 7b and 13b** from CodeLlama.
- **Retrieval settings:** BM25 retrieval of files under several context limits, and an "oracle" setting using the files edited by the reference patch (for analysis only).
- **SWE-bench Lite:** a 300-instance subset "sampled to be more self-contained, with a focus on evaluating functional bug fixes", covering 11 of the 12 repositories (§2, Appendix A.7 of v3).

## 4. Key findings (from the paper)

- "The best-performing model, Claude 2, is able to solve a mere 1.96% of the issues" with BM25 retrieval (abstract, §1).
- **GPT-4 was evaluated only on a 25% random subset** of SWE-bench "due to budget constraints" (Table footnote and Appendix), which complicates direct comparison.
- BM25 retrieval is a bottleneck: at a 27,000-token limit, BM25 retrieved a superset of the oracle files in about 40% of instances, but in almost half of instances it retrieved none of them (§4).
- Task properties (§2.3): issue descriptions average 195 words; every instance has at least one fail-to-pass test and 40% have at least two; a median of 51 additional tests checks that existing behaviour is preserved.

## 5. Setup and benchmark limitations

Limitations stated by the authors, plus limitations documented later by others:

| Limitation | Source |
|---|---|
| Python only; 12 repositories; popular projects with good tests | Paper (§2) |
| Non-interactive baselines: models produce a patch in one pass, with no execution feedback | Paper (§4); motivates SWE-agent [@yang2024sweagent] **[PR]** |
| Underspecified issues and over-specific tests in many instances (38.3% and 61.1% of 1,699 sampled tasks flagged; 68.3% filtered out overall) | [@chowdhury2024sweverified] **[VC]** |
| Solution leakage and weak tests among "resolved" patches | [@aleithan2024swebenchplus] **[PP]** |
| Possible memorisation: buggy-file identification from issue text alone up to 76% on SWE-bench Verified | [@liang2025illusion] **[PP]** |
| No visual or non-Python tasks | [@yang2025swebenchmm] **[PR]** |
| Mostly short tasks (77.8% estimated under one hour for an experienced engineer) | [@chowdhury2024sweverified] **[VC]** |

The paper anticipated contamination and proposed a remedy: the collection process is "continually updatable", allowing evaluation on issues created after a model's training date (§2.3). Whether that remedy is used consistently by later evaluations is a separate question.

## 6. Novelty

- **Claimed:** real-world, execution-validated, repository-scale tasks with long inputs, a training set, and an updatable collection process.
- **Our assessment [OP]:** SWE-bench turned "can a model fix a real issue?" into a reproducible measurement and so set the agenda for ASE. Its most durable contribution may be the *construction method* (execution-filtered fail-to-pass tasks from real PRs), which successors reuse (SWE-bench Verified, Multimodal, Pro, SWE-Gym).

## 7. Connections

- SWE-agent was designed and evaluated on it [@yang2024sweagent] **[PR]**; see [swe-agent.md](swe-agent.md).
- Agentless [@xia2025agentless] **[PR]** and AutoCodeRover [@zhang2024autocoderover] **[PR]** report results on SWE-bench Lite.
- SWE-bench Verified [@chowdhury2024sweverified] **[VC]** was developed with the SWE-bench authors; SWE-bench Multimodal [@yang2025swebenchmm] **[PR]** extends it to visual JavaScript tasks.
- SWE-Gym reuses the construction idea for training environments [@pan2025swegym] **[PR]**.
- Later audits and successors: SWE-Bench+ [@aleithan2024swebenchplus], SWE-Bench Pro [@deng2025swebenchpro], SWE-Bench Pro Verified [@zheng2026sweproverified] (all **[PP]**).

## 8. Open questions

1. How should benchmark scores be adjusted, or reported, for known instance-level validity problems?
2. What is the useful lifetime of a public, static repository benchmark under contamination pressure?
3. Do hidden-test pass rates predict the quality judgements of human reviewers on the same patches?
4. How do results on Python issue resolution transfer to other languages, larger changes, or feature work?

## 9. Implications for AAE [OP]

- **A benchmark is an instrument, not ground truth.** Its validity has to be audited like any measuring device. ASE research should report instance-level validity issues alongside scores.
- **Fail-to-pass tests are a verification signal with known false positives and false negatives.** Agents optimised against such signals can learn to exploit their weaknesses. Benchmark designers and harness designers face the same problem.
- **Construction methods outlive datasets.** AAE should treat benchmark *pipelines*, including their filtering criteria, as first-class research objects.

## References

`jimenez2024swebench`, `yang2024sweagent`, `chowdhury2024sweverified`, `aleithan2024swebenchplus`, `liang2025illusion`, `yang2025swebenchmm`, `xia2025agentless`, `zhang2024autocoderover`, `pan2025swegym`, `deng2025swebenchpro`, `zheng2026sweproverified` (see [`references.bib`](../references.bib)).
