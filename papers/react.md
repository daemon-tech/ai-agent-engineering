# ReAct: Synergizing Reasoning and Acting in Language Models

## 1. Bibliographic record

| Field | Value |
|---|---|
| Title | ReAct: Synergizing Reasoning and Acting in Language Models |
| Authors | Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao |
| First public version | arXiv 2210.03629v1, 2022-10-06 |
| Version read | 2210.03629v3 (the authors' comment: "v3 is the ICLR camera ready version") |
| Venue | International Conference on Learning Representations (ICLR) 2023 |
| URL / identifier | https://arxiv.org/abs/2210.03629 ; ICLR 2023 poster page https://iclr.cc/virtual/2023/poster/11003 |
| DOI | None found (ICLR does not issue DOIs) |
| BibTeX key | `yao2023react` |
| Evidence class | **[PR]** peer-reviewed |
| Verified via | arXiv API metadata and PDF (2026-10-14); ICLR 2023 virtual-conference paper listing (2026-10-14). OpenReview blocked automated access on that date. |

## 2. Research question

Can a language model that *interleaves* reasoning traces with task-specific actions outperform models that only reason (chain-of-thought) or only act (action generation), on both knowledge-intensive reasoning and interactive decision-making tasks?

## 3. Method

- **Prompting**, with few-shot in-context trajectories of the form *Thought → Action → Observation*, repeated. Thoughts do not affect the environment; actions do.
- **Environments:** a simple Wikipedia API (search, lookup, finish) for HotpotQA (multi-hop QA) and Fever (fact verification); the text-based game ALFWorld; the WebShop online shopping environment.
- **Model:** PaLM-540B for the main results; GPT-3 results in an appendix; fine-tuning experiments with smaller PaLM models on HotpotQA.
- **Baselines:** standard prompting, chain-of-thought (CoT), CoT with self-consistency (CoT-SC), acting only ("Act"), and imitation/RL methods for ALFWorld and WebShop.
- **Hybrid strategies:** switch from ReAct to CoT-SC when ReAct fails to answer within a step limit, and from CoT-SC to ReAct when self-consistency votes are not decisive.

## 4. Key findings (from the paper)

- On ALFWorld and WebShop, ReAct "outperforms imitation and reinforcement learning methods by an absolute success rate of 34% and 10% respectively, while being prompted with only one or two in-context examples" (abstract).
- PaLM-540B prompting on HotpotQA (EM) / Fever (accuracy): Standard 28.7 / 57.1; CoT 29.4 / 56.3; CoT-SC 33.4 / 60.4; Act 25.7 / 58.9; ReAct 27.4 / 60.9; CoT-SC→ReAct 34.2 / 64.6; ReAct→CoT-SC 35.1 / 62.0 (Table 1).
- So **ReAct alone slightly trailed CoT on HotpotQA** (27.4 vs. 29.4) and beat it on Fever (60.9 vs. 56.3). The best results combined internal reasoning and external acting.
- Manual error analysis of 200 HotpotQA trajectories (50 correct and 50 incorrect, each for ReAct and CoT): hallucination was the dominant failure for CoT (56% of its failures), whereas ReAct was more grounded but had more reasoning errors, including a characteristic loop of repeating prior thoughts and actions; non-informative search results accounted for 23% of ReAct's error cases (Table 2 and §3.3).
- Fine-tuning: with ReAct-format trajectories, PaLM-8B fine-tuned on ReAct outperformed all PaLM-62B prompting methods (§3.3, Figure 3).

## 5. Setup and benchmark limitations

- **Models and access:** results rest mainly on PaLM-540B, which is not publicly available, so exact replication is limited.
- **Toy action spaces:** the Wikipedia API has three actions; real agent environments are far richer.
- **Short horizons:** tasks require few steps compared to repository-level software work.
- **Prompt sensitivity:** few-shot exemplars were hand-written. How much of the benefit comes from the interleaved reasoning itself, as opposed to the similarity between exemplars and queries, is not isolated in the paper. We have not yet verified follow-up work on this question; it is listed as an open question below.
- **Metrics:** exact match on HotpotQA under-credits correct but differently phrased answers. The authors note "label ambiguity" as a success/failure category.

## 6. Novelty

- **Claimed:** combining reasoning and acting in one prompted loop, rather than studying them separately.
- **Our assessment [OP]:** the lasting contribution is the *trajectory format* itself: explicit, interleaved, human-readable thought/action/observation steps. It became the default skeleton of agent harnesses, and its interpretability supports human oversight.

## 7. Connections

- Builds on chain-of-thought [@wei2022chain] **[PR]**.
- Extended by Reflexion's cross-trial reflection [@shinn2023reflexion] **[PR]** and contrasted with search-based Tree of Thoughts [@yao2023tree] **[PR]**.
- The SWE-agent loop is a ReAct-style loop with an engineered action space [@yang2024sweagent] **[PR]**; see [swe-agent.md](swe-agent.md).
- Organised within CoALA's decision-procedure framing [@sumers2024coala] **[PR]**.

## 8. Open questions

1. How much of the benefit of interleaved thoughts survives with models trained to reason internally? (See agenda Q5.)
2. What prevents and recovers from the repetitive-loop failure mode in long-horizon settings?
3. When is it better to back off to pure reasoning versus to more acting? ReAct's hybrid heuristics are hand-set.

## 9. Implications for AAE [OP]

- The **loop is the unit of engineering**. Many harness design questions (context, termination, error feedback) only arise once reasoning and acting are interleaved.
- **"ReAct beats CoT" is not what the paper shows.** It shows task-dependent trade-offs and that hybrids win. Engineering guidance that cites ReAct as universal support for agent loops overstates it.
- The **failure analysis** (grounding vs. reasoning errors, uninformative tool results) is an early, reusable template for diagnosing agent trajectories.

## References

`yao2023react`, `wei2022chain`, `shinn2023reflexion`, `yao2023tree`, `yang2024sweagent`, `sumers2024coala` (see [`references.bib`](../references.bib)).
