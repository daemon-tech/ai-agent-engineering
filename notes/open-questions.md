# Research Agenda: Open Questions

*AAE Research Notebook v0.1, 2026-10-14.*

Each question records **what is known** (with evidence classes), **what is uncertain**, **why it matters**, and **what evidence would resolve it**. Questions are numbered for reference from other files; numbering does not indicate priority. To propose a new question, use the [research-question issue template](../.github/ISSUE_TEMPLATE/research-question.md).

---

## Q1. How valid are repository-level benchmarks as measures of software engineering capability?

- **Known.** Instance-level problems are well documented for SWE-bench: underspecified issues and over-specific tests [@chowdhury2024sweverified] **[VC]**, solution leakage and weak tests [@aleithan2024swebenchplus] **[PP]**, and memorisation signals [@liang2025illusion] **[PP]**. Successor benchmarks have themselves needed audits [@zheng2026sweproverified] **[PP]**.
- **Uncertain.** How much these problems bias *rankings* between systems, as opposed to absolute scores. Whether hidden-test pass rates predict human reviewers' acceptance of the same patches.
- **Why it matters.** Benchmark scores drive research directions, product claims, and risk assessments.
- **Resolving evidence.** A study that has expert reviewers judge a stratified sample of benchmark-"resolved" and "unresolved" patches from several systems, then reports agreement with test verdicts and whether system rankings change; plus a longitudinal analysis of how quickly new benchmarks show contamination signals.

## Q2. How reliable are agent evaluation harnesses themselves?

- **Known.** Oracle defects can change measured success dramatically (94.3% → 65.5% in one audited benchmark) [@chen2026oracle] **[PP]**. Re-execution can also leave decisions unchanged, with small verdict drift (0.83% of majority verdicts under rebuilt images) [@ding2026reexec] **[PP]**. OpenAI built a containerised harness for SWE-bench to improve reliability [@chowdhury2024sweverified] **[VC]**.
- **Uncertain.** How common grader defects are across benchmarks, and which classes of defects matter most.
- **Why it matters.** If the instrument is broken, every comparison built on it is unreliable.
- **Resolving evidence.** Applying a common oracle-audit protocol (fault injection plus known-answer controls) to several widely used agent benchmarks, with results published per benchmark and defect class.

## Q3. How much does the quality of the task specification and done predicate determine agent outcomes?

- **Known.** 38.3% of sampled SWE-bench tasks were flagged as underspecified [@chowdhury2024sweverified] **[VC]**. Practitioner guidance treats a checkable finish condition as the central habit [@tan2026pstack] **[EE]**. Interactive clarification for repository-level tasks is being studied (seen in our October 2026 scan, not yet reviewed; see the research log).
- **Uncertain.** The effect size of specification quality relative to model and harness choices, and whether agents can reliably detect underspecification and ask.
- **Why it matters.** If specification dominates, effort should go into specification tooling and human training rather than agent capability. **[OP]** We hypothesise this (Chapter 01, §3.2).
- **Resolving evidence.** A factorial experiment that varies specification quality (vague, precise, precise plus executable done predicate) × model × harness on matched tasks, reporting variance decomposition.

## Q4. Where does best-of-n selection saturate, and what sets the ceiling?

- **Known.** Sampling multiple candidates and selecting with tests or learned verifiers improves open-weight agent results [@pan2025swegym] **[PR]**. Agentless uses validation-based selection [@xia2025agentless] **[PR]**. Search over intermediate thoughts helps on puzzles [@yao2023tree] **[PR]**.
- **Uncertain.** Whether the gain from more samples is bounded by verifier precision, as we hypothesise **[OP]**, and how weak tests interact with selection pressure.
- **Why it matters.** Inference-time compute is a main lever for deployed agents; if the verifier is the bottleneck, investment should shift to verification.
- **Resolving evidence.** Curves of accuracy versus *n*, measured against both the selection verifier and an independent expert or stronger oracle, on tasks where verifier false-positive rates are known.

## Q5. Do interface and harness effects persist as models improve?

- **Known.** Interface design changed SWE-bench Lite resolve rates substantially for GPT-4 Turbo [@yang2024sweagent] **[PR]**. Scaffolds produced a 10× range for one model on SWE-bench Lite [@chowdhury2024sweverified] **[VC]**. One preprint found that harness additions helped a weaker model but "added little" for a stronger one in its setting [@giampieri2026cortex] **[PP]**.
- **Uncertain.** Whether harness effects shrink, persist, or change character (e.g., from capability support to reliability and safety) with newer models.
- **Why it matters.** It decides whether AAE is a lasting discipline or a temporary workaround for weak models (Chapter 01, falsifiability condition F4).
- **Resolving evidence.** Re-running published interface ablations (e.g., SWE-agent's Table 3) with several model generations under a fixed protocol, reporting the interaction between model and interface.

## Q6. When do multi-agent setups outperform a single agent with the same compute budget?

- **Known.** Role-based multi-agent systems generated more coherent solutions than earlier chat-based systems on their benchmarks [@hong2024metagpt] **[PR]**, [@qian2024chatdev] **[PR]**. Vendors recommend orchestrator-workers designs for unpredictable subtasks [@anthropic2024effective] **[VC]**. Practitioners use parallel workers and multi-model review [@tan2026pstack] **[EE]**.
- **Uncertain.** Which mechanism produces the benefit (context isolation, diversity, extra compute, process structure; Chapter 03 §6.2), and whether benefits hold for repository-scale maintenance.
- **Why it matters.** Multi-agent systems multiply cost and failure surfaces. Their use should be justified by evidence.
- **Resolving evidence.** Compute-matched comparisons with ablations that separate each mechanism, on repository-level tasks, with reliability (pass^k) as well as mean success.

## Q7. Does separating author and verifier agents reduce escaped defects?

- **Known.** Practitioner workflows require that "the agent that judges a change is never the one that wrote it" [@tan2026pstack] **[EE]**. Agents make unsupported completion claims [@wang2026agentswe] **[PP]**. Agentic verifiers are used as benchmark graders [@yao2026sweeper] **[PP]**.
- **Uncertain.** Whether an independent verifier catches more defects than self-verification at equal cost, whether model-family diversity matters, and what the verifier's own false-positive and false-negative rates are.
- **Why it matters.** It is a cheap, widely applicable design choice whose effect is unknown.
- **Resolving evidence.** A controlled study on tasks with seeded or known defects comparing self-check, same-model independent check, and different-model independent check, measuring defect detection and false alarms.

## Q8. What are the cumulative effects of agent-written changes on codebases?

- **Known.** Starting from agent-written history lowered later-task resolution by 5.6 points on average in one study; the effect was driven by inherited test failures [@pan2026maintain] **[PP]**. Time horizons of tasks agents complete are growing [@kwa2025horizon] **[PR]**.
- **Uncertain.** Effects over longer histories, in other languages, on non-functional qualities (readability, architecture), and on human maintainers.
- **Why it matters.** As agents take on longer-horizon work, small per-change costs could compound.
- **Resolving evidence.** Longitudinal studies of repositories with substantial agent contributions, compared with matched human-only histories, measuring defect rates, change effort, and test health over time.

## Q9. What evidence lets a human reviewer trust an agent's change quickly and correctly?

- **Known.** Practitioners hand over artefacts (failing then passing tests, videos, traces, decision logs) [@tan2026pstack] **[EE]**. Hassan et al. propose "Merge-Readiness Packs" [@hassan2025agenticse] **[PP]**. Developers' perceptions of AI speed-ups can be wrong in sign [@becker2025uplift] **[PP]**.
- **Uncertain.** Which kinds of evidence improve reviewer accuracy and speed, and which create false confidence.
- **Why it matters.** Human review is the main safety gate in ASE and a main cost. Better hand-off evidence is the key to scaling oversight.
- **Resolving evidence.** Reviewer experiments where the same agent changes (some with seeded defects) are presented with different evidence bundles, measuring detection rate, false acceptance, and time.

## Q10. Is the proposed AAE taxonomy usable and reliable?

- **Known.** Nothing yet. The taxonomy is our proposal **[OP]** (Chapter 01). Related frameworks exist: CoALA [@sumers2024coala] **[PR]**, harness-engineering reviews [@zhou2026externalization] **[PP]**, and failure taxonomies [@li2026workflowfail] **[PP]**.
- **Uncertain.** Whether independent raters can classify papers and systems into layers and activities consistently, and whether the taxonomy reveals gaps that other framings miss.
- **Why it matters.** A taxonomy that cannot be applied reliably is not useful for organising a field.
- **Resolving evidence.** A systematic mapping study: sample agent papers, have at least two raters classify them, report inter-rater agreement (e.g., Cohen's κ), and revise the scheme.

## Q11. How should agent permissions and approvals be designed?

- **Known.** MCP requires explicit user consent before tool invocation and treats tool descriptions as untrusted unless from a trusted server [@mcp2026spec] **[VC]**. Practitioner policies allow reversible actions without asking and pause for irreversible ones [@tan2026pstack] **[EE]**. Benchmarks document frequent boundary violations by open-source agents [@trong2026misbehavior] **[PP]**.
- **Uncertain.** Where the line between "reversible" and "irreversible" lies in practice, how approval fatigue affects safety, and which policies minimise harm at acceptable cost in human attention.
- **Why it matters.** Approval policies trade safety against the efficiency that motivates agents in the first place.
- **Resolving evidence.** Field or simulation studies comparing approval policies on matched workloads, measuring harmful actions, human interruptions, and task completion.

## Q12. How should persistent agent artefacts (memory, skills, instruction files) be secured and tested?

- **Known.** Persistent artefacts enable cross-session attacks with high success rates against tested agents [@liao2026skillrelay] **[PP]**. Instruction-file changes can be measured and pruned [@giampieri2026cortex] **[PP]**. Memory architectures are diverse [@park2023generative] **[PR]**, [@packer2023memgpt] **[PP]**.
- **Uncertain.** Provenance models for agent-written artefacts; regression testing of harness text; and how to detect harmful, as opposed to merely unused, instructions.
- **Why it matters.** Practitioners increasingly shape agents through such artefacts, and they persist across sessions and teams.
- **Resolving evidence.** Benchmarks combining utility and adversarial cases for memory and skill systems, and empirical studies of how instruction files change over time in real repositories.

## Q13. Does reasoning-trace interleaving (ReAct-style) still matter with models that reason internally?

- **Known.** ReAct's benefit was task-dependent, and hybrids with CoT-SC performed best [@yao2023react] **[PR]**.
- **Uncertain.** Whether explicit interleaved thoughts add value, cost, or interpretability, or none of these, for models trained to reason before acting.
- **Why it matters.** It determines loop design and what humans can audit.
- **Resolving evidence.** Ablations of explicit thought steps on agentic SE tasks across model families, measuring success, cost, and the usefulness of traces for human diagnosis.
