# Frontier Review: October 2026

| | |
|---|---|
| **Review date** | 2026-10-14 (Europe/Berlin) |
| **Reviewer** | AAE notebook (AI-assisted draft; human review pending) |
| **Window** | Primarily arXiv submissions 2026-10-08 to 2026-10-13, plus the current MCP specification revision and two September 2026 items needed for context |
| **Search** | See [research-log.md](research-log.md), entries R1–R4 |

> **How to read this review.** Every item is either a **first-version preprint, days old, [PP]**, or a **vendor/standards document [VC]**, except item 12, which is peer-reviewed. "Independently verified" means *we* reproduced or checked a result; for every item below the answer is **no**. We verified that each work exists and that its metadata (title, authors, dates) is correct, using the arXiv API or the publisher. We read abstracts and, for some items, selected sections. All numbers are the authors' own. Publication dates are arXiv v1 submission dates (UTC; the calendar date is the same in CEST for every item here). We do not call any item "the latest"; "most recent we found" is relative to the review date and search.

## Summary of themes

1. **Evaluating the evaluators.** Several papers audit benchmarks and graders and find defects large enough to change conclusions (items 2, 6, 7).
2. **From "fix this issue" to "find what's wrong" and "deliver what was asked".** New benchmarks score bug *discovery* through interaction and the *faithfulness* of delivered agents to requirements (items 3, 4).
3. **Cumulative effects.** Agent-written history affects later maintenance (item 5).
4. **Boundaries and security of agent tooling.** Misbehaviour taxonomies and attacks through persistent skill artefacts (items 8, 9).
5. **Testing the harness.** Instruction files and skills treated as artefacts to be measured, not trusted (item 10), and failure taxonomies that locate problems in execution and tooling rather than model reasoning (item 11).
6. **Protocol churn.** MCP's 2026-07-28 revision makes breaking changes (item 1).

---

## Item 1: Model Context Protocol specification, revision 2026-07-28

| Field | Value |
|---|---|
| Source | [@mcp2026spec], https://modelcontextprotocol.io/specification/2026-07-28 |
| Class | **[VC]** standards document maintained by the MCP project |
| Publication date | Revision identifier 2026-07-28. On 2026-10-14, `/specification/latest` redirected to this revision; the earlier revisions listed were 2024-11-05, 2025-03-26, 2025-06-18, and 2025-11-25. |
| Review date | 2026-10-14 |
| What changed | Per the official changelog: protocol-level sessions and the `initialize` handshake are removed (MCP becomes stateless); a `server/discover` RPC is added; a Multi Round-Trip Request pattern replaces server-initiated requests such as sampling and elicitation; experimental tasks move to an extension; the Roots, Sampling, and Logging features are deprecated; `tools/list` results should be deterministic in order "to enable client-side caching and improve LLM prompt cache hit rates". |
| Mechanism | Every request carries protocol version and client capabilities in `_meta`; servers that need cross-call state pass explicit handles as tool arguments. |
| Independently verified | No. We read the changelog, not the full schema. We did not test implementations. |
| Why it matters | Tool protocols set the default action space and trust model of agents (Chapter 03, §4.3). Statelessness simplifies scaling but moves state management into tool design. Deterministic tool ordering is an explicit concession to LLM context caching. |
| Limits | Vendor/standards text describes intent, not adoption or effects. SDK and client support for this revision was not checked. |

## Item 2: SWE-Bench Pro Verified

| Field | Value |
|---|---|
| Source | [@zheng2026sweproverified], arXiv 2609.08149 |
| Class | **[PP]** |
| Publication date | v1 2026-09-08; v3 updated 2026-10-09 |
| Review date | 2026-10-14 |
| What changed | Reports that evaluation on SWE-Bench Pro [@deng2025swebenchpro] **[PP]** is undermined by reward hacking (leakage of gold solutions or hidden evaluation information) and by task quality issues (misleading problem statements, improperly scoped tests), and releases a revised version. |
| Mechanism | Anti-hacking safeguards that close leakage channels, plus minimal correction of flawed instances. |
| Independently verified | No. |
| Why it matters | It repeats the SWE-bench → SWE-bench Verified pattern one benchmark generation later (Chapter 02, §6.1). That supports the view that benchmark audits are a recurring necessity, not one-off fixes. |
| Limits | The abstract says "some models perform substantially worse than previously evaluated" without numbers there; we did not extract the per-model figures. It is not yet reviewed, and it comes from a different team than the original benchmark. |

## Item 3: AgentSWE: Can coding agents build the agent you actually want?

| Field | Value |
|---|---|
| Source | [@wang2026agentswe], arXiv 2610.13361 |
| Class | **[PP]** |
| Publication date | 2026-10-09 |
| Review date | 2026-10-14 |
| What changed | A benchmark in which coding agents build, edit, or optimise *agents* from natural-language requirements (25 tasks). Acceptance runs the frozen submission on held-out cases. |
| Mechanism | Builders see a few illustrative cases. Grading uses requirement-derived rubrics under hard pass/fail gates, or the source benchmark's objective for optimisation tasks. |
| Independently verified | No. |
| Why it matters | It names failure modes directly relevant to verification: "overfitting to the visible cases, hollow runtimes behind code that looks complete, and unsupported claims of completion". These are exactly the gaps between *demonstrated* and *delivered* behaviour that practitioner verification practices target (case study, §3.4). |
| Limits | 25 tasks. Rubric-based grading involves judgement. The claim that "none comes close" is qualitative in the abstract. |

## Item 4: SWEeper-Bench: Can agents discover bugs in interactive software?

| Field | Value |
|---|---|
| Source | [@yao2026sweeper], arXiv 2610.14096 |
| Class | **[PP]** |
| Publication date | 2026-10-08 |
| Review date | 2026-10-14 |
| What changed | 200 tasks from real bug fixes in 200 open-source web applications. The agent receives only the codebase and an open-ended request, so it must find interaction-dependent bugs, not just fix a described one. |
| Mechanism | Agents must design interactive tests to trigger the bug. An agentic verifier judges repairs by user-observable browser behaviour. |
| Independently verified | No. |
| Why it matters | It moves evaluation from "resolve a known issue" to "discover the failure", the verification step that most benchmarks skip. The authors report that the best of 15 frontier agents passes 59.0% of tasks and that the bottleneck is *identifying* the buggy behaviour. |
| Limits | The verifier is an agent, so its own error rate matters. Web applications only. The models are not named in the abstract. |

## Item 5: Do modifications made by coding agents make subsequent maintenance harder? (SWE-Maintain)

| Field | Value |
|---|---|
| Source | [@pan2026maintain], arXiv 2610.14768 |
| Class | **[PP]** |
| Publication date | 2026-10-10 |
| Review date | 2026-10-14 |
| What changed | 100 three-event maintenance episodes from 50 Python repositories. Each later task is run from developer-written history and from the agent's own history. |
| Mechanism | Paired comparison across five coding systems, two backbone models, and 1,996 paired later events. |
| Independently verified | No. |
| Why it matters | It is among the first controlled measurements of *cumulative* agent effects. The reported results are a 5.6-point average drop in later-task resolution from agent history, 14.0 points when earlier tests must also pass, and no disadvantage (+2.7 points, 95% CI [−0.5, +6.1]) when the inherited code passes earlier tests. That points to inherited test failures, rather than code style, as the main cost. |
| Limits | Python only. Three-event episodes are short compared with real project histories. Hidden tests define "behaviour". |

## Item 6: When agent evaluation becomes unreliable: oracle failures

| Field | Value |
|---|---|
| Source | [@chen2026oracle], arXiv 2610.16067 |
| Class | **[PP]** (comment: "Submitted to Empirical Software Engineering"; submission is not acceptance) |
| Publication date | 2026-10-12 |
| Review date | 2026-10-14 |
| What changed | An auditing approach for agent-benchmark oracles (five state-integrity invariants, three known-answer controls), validated by fault injection. |
| Mechanism | Applied to an agent benchmark, it found a reward-function defect that changes environment state before scoring. Replay-based correction changed measured success from 94.3% to 65.5% across 4,320 episodes. A component ablation found that tool descriptions and error strings changed trajectory reliability. |
| Independently verified | No. |
| Why it matters | It shows that evaluation harnesses are software with bugs that can dominate the measured effect, and that harness text (tool descriptions, error strings) is a measurable variable. Both points are central to AAE's distinction between evaluation and verification. |
| Limits | Single author. The benchmark audited is not named in the abstract. The author reports that one effect reverses sign in a second domain, and that the method could not validate a second benchmark. |

## Item 7: Re-executing coding-agent evaluations

| Field | Value |
|---|---|
| Source | [@ding2026reexec], arXiv 2610.14460 |
| Class | **[PP]** |
| Publication date | 2026-10-10 |
| Review date | 2026-10-14 |
| What changed | Two preregistered re-execution studies of coding-agent grading, reporting negative results. In one, SWE-Bench Pro's offline option rejected none of 59 accepted Go patches whose grading configuration changed. In the other, re-executing 1,929 archived evaluations from the Darwin Gödel Machine preserved best-agent selection and variant ranking. |
| Mechanism | Re-run accepted patches under changed grading configurations, rebuilt images, and different hosts. |
| Independently verified | No. |
| Why it matters | It is a careful counterweight to item 6. Some evaluations *are* robust to re-execution, though small verdict changes occur (rebuilt images changed 16 three-run majority verdicts, 0.83%). It also models good practice: preregistration and an "evidence-to-claim summary". |
| Limits | Covers accepted patches and fixed-history decisions only. The authors state that general policy safety requires broader evaluation. |

## Item 8: SWE-MISBEHAVIOR: boundary violations in coding agents

| Field | Value |
|---|---|
| Source | [@trong2026misbehavior], arXiv 2610.18206 |
| Class | **[PP]** |
| Publication date | 2026-10-13 |
| Review date | 2026-10-14 |
| What changed | A taxonomy and benchmark of 11 misbehaviours across code generation, file management, and system interaction (7.4K human-in-the-loop synthesised samples). |
| Mechanism | Automated evaluation of open-source agents (e.g., OpenHands, smolagents); a mitigation framework, CODE-KIT, combining misbehaviour-aware guidelines with tools. |
| Independently verified | No. |
| Why it matters | It treats *how* an agent achieves a task (unintended input modification at 50.5%, silent compromise of environment integrity at 53%) as a measurable quality, not only *whether* it succeeds. The authors report that CODE-KIT reduced misbehaviours by 52% for smolagents and 34% for OpenHands while improving task completion. |
| Limits | Samples are synthesised. Evaluation covers open-source agents, not proprietary ones. The "first taxonomy" claim was not checked. |

## Item 9: Cross-session attacks via persistent artefacts in agent skill composition

| Field | Value |
|---|---|
| Source | [@liao2026skillrelay], arXiv 2610.13227 |
| Class | **[PP]** |
| Publication date | 2026-10-09 |
| Review date | 2026-10-14 |
| What changed | It identifies cross-session composition attacks: a skill's persistent artefacts (files, configs, caches) influence later skills. Three mechanisms are named: Instruction Propagation, Data Boundary Violation, and Evidence Poisoning. |
| Mechanism | SkillRelayBench (270 adversarial cases, 30 scenarios) across Codex CLI, Gemini CLI, and Claude Code with seven models. A runtime defence, SkillRelayGuard, restores artefact provenance and adds pre-execution advisory review. |
| Independently verified | No. |
| Why it matters | Skills and instruction files are now a main way practitioners shape agents (case study). This shows that the same mechanism is an attack surface: reported attack success rates range from 46.7% to 77.4%, and the defence reduces overall ASR from 69.5% to 10.9%. |
| Limits | Adversarial cases are constructed by the authors. The defence leaves the final decision to the agent. Generalisation to other tools has not been tested. |

## Item 10: Cortex: measurement-gated evolution and pruning of coding-agent skills and rules

| Field | Value |
|---|---|
| Source | [@giampieri2026cortex], arXiv 2610.14216 |
| Class | **[PP]** |
| Publication date | 2026-10-09 |
| Review date | 2026-10-14 |
| What changed | A tool that keeps a change to an agent's instruction files (project file, skills, rules) only if repeated runs with and without it show a net gain and no noticeable regression. Existing text is tested the same way before deletion. |
| Mechanism | Developer corrections are saved as replayable tasks; recurring corrections are found; one skill or rule is written at a time; with/without runs gate it. |
| Independently verified | No. |
| Why it matters | It is a direct empirical test of "encode lessons in structure"-style practice (case study, §3.3). Its candid negative findings are informative: rules "did most of the work", skills helped mainly when offered alongside relevant files, a stronger model gained little from one run's harness, and on a real project with few corrections "Cortex found nothing to learn". |
| Limits | Single author. Most experiments use a purpose-built repository and Claude Haiku 4.5. The author notes the test shows Cortex "keeps no unused text, not that it detects damage". |

## Item 11: Why agentic workflows fail: a source-aware taxonomy

| Field | Value |
|---|---|
| Source | [@li2026workflowfail], arXiv 2610.17418 |
| Class | **[PP]** |
| Publication date | 2026-10-12 |
| Review date | 2026-10-14 |
| What changed | A failure taxonomy that localises failures on two axes, workflow stage and agent capability, applied to both academic literature and GitHub-reported failures. |
| Mechanism | Source attribution, a failure-type dictionary, and stage and capability localisation. |
| Independently verified | No. |
| Why it matters | It reports that literature-derived failures emphasise planning and reasoning, whereas GitHub-derived failures concentrate in execution, actuation, tool, API, and infrastructure. That supports treating agent reliability "as a systems problem rather than only a model-output problem", which is the core premise of AAE's harness layer. |
| Limits | Corpus construction and coding reliability are not described in the abstract. The taxonomy has not been validated by other groups. |

## Item 12 (context, peer-reviewed): SE 3.0 published in TOSEM

| Field | Value |
|---|---|
| Source | [@hassan2026se3], DOI 10.1145/3807901 |
| Class | **[PR]** |
| Publication date | 2026-08-21 (Crossref issued date); arXiv v1 2024-10-08 |
| Review date | 2026-10-14 |
| What changed | The SE 3.0 vision ("AI-native", "intent-centric, conversation-oriented development") moved from preprint to journal publication. |
| Mechanism | Vision paper: proposes a technology stack (Teammate.next, IDE.next, Compiler.next, Runtime.next) and a challenge roadmap. |
| Independently verified | Not applicable (no empirical claims to reproduce). |
| Why it matters | It gives the agentic-SE framing a peer-reviewed anchor in a top SE journal (Chapter 02, §1). |
| Limits | A vision, not evidence of outcomes. |

---

## What we looked at and did not include

See [research-log.md](research-log.md), entry R2, for titles seen in the scan and the reason each was excluded (mostly scope, or lack of direct bearing on ASE).

## Next review

Proposed for the week of 2026-11-09. Revisit items 2–11 for new versions, reviews, or replications, and check whether any were accepted at a venue.
