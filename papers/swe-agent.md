# SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

## 1. Bibliographic record

| Field | Value |
|---|---|
| Title | SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering |
| Authors | John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press |
| First public version | arXiv 2405.15793v1, 2024-05-06 (arXiv "published" date) |
| Version read | 2405.15793v3 |
| Venue | Advances in Neural Information Processing Systems (NeurIPS) 2024 |
| URL | https://proceedings.neurips.cc/paper_files/paper/2024/hash/5a7c947568c1b1328ccc5230172e1e7c-Abstract-Conference.html ; https://arxiv.org/abs/2405.15793 ; code https://swe-agent.com |
| DOI | None found |
| BibTeX key | `yang2024sweagent` |
| Evidence class | **[PR]** peer-reviewed |
| Verified via | NeurIPS 2024 proceedings page (fetched 2026-10-14); arXiv API and PDF |

## 2. Research question

Language-model agents are "a new category of end users with their own needs and abilities". Does designing the *interface* between an LM agent and the computer, which the authors call the agent-computer interface (ACI), improve agent performance on software engineering tasks, without changing the model's weights?

## 3. Method

- **The ACI** (§2–3): a small set of LM-oriented commands.
  - *Search:* `find_file`, `search_file`, and `search_dir`, which return a summary of matches rather than paging through them.
  - *File viewer:* `open`, `scroll_up`, `scroll_down`, and `goto`, showing a window of at most 100 lines with line numbers and an indication of omitted lines.
  - *Editor:* a single `edit` command replacing a line range, integrated with a linter that rejects edits introducing syntax errors and shows the error.
  - *Context management:* observations before the last five are collapsed to a single line each.
- **Loop:** a ReAct-style thought-and-action loop [@yao2023react] **[PR]**.
- **Models:** GPT-4 Turbo (`gpt-4-1106-preview`) and Claude 3 Opus (`claude-3-opus-20240229`).
- **Budget:** $4 per instance.
- **Benchmarks:** full SWE-bench test set (2,294), SWE-bench Lite (300) for ablations, and HumanEvalFix.
- **Baselines:** a shell-only agent and non-interactive retrieval-augmented generation (RAG).

## 4. Key findings (from the paper)

- **Main result:** SWE-agent with GPT-4 Turbo resolved **12.47% (286/2,294)** of the full SWE-bench test set and **18.00% (54/300)** of SWE-bench Lite. The previous best non-interactive, retrieval-augmented system resolved 3.8% (§1, §4, Table 1).
- **Interface vs. shell:** on Lite, SWE-agent solved 10.7 percentage points more instances than the shell-only baseline (§1).
- **Portability:** with Claude 3 Opus, 10.46% on full SWE-bench (Table 1).
- **HumanEvalFix:** 87.7% pass@1 (abstract).
- **Ablations on Lite with GPT-4 Turbo** (Table 3): no edit command 10.3%; edit without linting 15.0%; iterative search 12.0%; no search 15.7%; 30-line viewer 14.3%; full-file viewer 12.7%; full history 15.0%; without demonstration 16.3%; full configuration 18.0%.
- **Behavioural analyses:** iterative search led agents to exhaustively page through results, exhausting budget or context. Guardrails helped agents recover from their own editing errors (§4–5).

## 5. Setup and benchmark limitations

- **Benchmark validity.** The results inherit SWE-bench's issues (see [swe-bench.md](swe-bench.md)). SWE-Bench+ manually screened SWE-agent + GPT-4 successes and reports that filtering problematic instances lowered its resolve rate from 12.47% to 3.97% [@aleithan2024swebenchplus] **[PP]**. That re-analysis is itself an unreviewed preprint.
- **Single-run and budget effects.** Results depend on the $4 cap and on sampling settings, so cost-normalised comparison with cheaper pipelines matters. Agentless reported higher Lite results at lower cost shortly afterwards [@xia2025agentless] **[PR]**.
- **Interface tuned on one model.** The ACI was developed for GPT-4 Turbo. Portability was shown for one other model.
- **Python only**, with mostly short tasks. The later SWE-bench Multimodal work by an overlapping team shows lower results on visual JavaScript tasks (SWE-agent 12% vs. 6% for the next best) [@yang2025swebenchmm] **[PR]**.
- **Ablations on Lite only,** so differences of a few points correspond to a handful of instances out of 300.

## 6. Novelty

- **Claimed:** introducing the ACI concept and showing that interface design substantially changes agent performance without modifying weights; an open-source agent.
- **Our assessment [OP]:** SWE-agent moved the unit of innovation from the model to the **interface**, and it backed that move with ablations. This is the empirical basis for treating the harness as an engineering object (Chapter 01, layer L2).

## 7. Connections

- A ReAct-style loop [@yao2023react] **[PR]**, evaluated on SWE-bench [@jimenez2024swebench] **[PR]**.
- Contrasted with pipeline approaches: Agentless [@xia2025agentless] **[PR]** and AutoCodeRover [@zhang2024autocoderover] **[PR]**.
- Related interface arguments: executable code actions [@wang2024codeact] **[PR]**; vendor tool-design experience [@anthropic2024effective] **[VC]**.
- Extended to multimodal tasks [@yang2025swebenchmm] **[PR]**; related open platform OpenHands [@wang2025openhands] **[PR]**.

## 8. Open questions

1. Do ACI design principles (compact, summarised outputs; guardrails with specific feedback; bounded views) remain beneficial for later, stronger models?
2. Can good interfaces be found automatically, by search or learning, rather than by hand?
3. How do ACI choices interact with context-window size and history policies?
4. What is the equivalent of a "linter guardrail" for semantic errors that do not fail syntax checks?

## 9. Implications for AAE [OP]

- **Report the interface.** A model's score on an agent benchmark is a property of a model-interface pair. Our reporting checklist (Chapter 01, §4) follows from this.
- **Fewer, better actions beat more actions.** Iterative search underperforming *no* search is a strong caution against exposing every available tool.
- **Guardrails are verification at the action level.** They are the cheapest point at which to catch errors, and the cheapest place to give corrective feedback.

## References

`yang2024sweagent`, `yao2023react`, `jimenez2024swebench`, `aleithan2024swebenchplus`, `xia2025agentless`, `zhang2024autocoderover`, `wang2024codeact`, `anthropic2024effective`, `yang2025swebenchmm`, `wang2025openhands` (see [`references.bib`](../references.bib)).
