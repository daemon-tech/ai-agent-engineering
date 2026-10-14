# Case Study: pstack (Lauren Tan)

*AAE Research Notebook v0.1, 2026-10-14. Not peer reviewed.*

> **Evidence class: [EE] engineering experience.** pstack is a practitioner's workflow package. Its documentation describes practices and the author's reasons for them. It reports **no controlled evaluation** of its effects, and we did not run one. Nothing in this case study should be read as validated science. pstack is **one case study among many** and is not a foundation of this notebook.

## 1. Source and provenance

| Field | Value |
|---|---|
| Name | pstack (Cursor plugin) |
| Author | Lauren Tan ("poteto"), per `plugin.json` and the README |
| Official source | https://github.com/cursor/plugins/tree/main/pstack |
| Version studied | 0.15.24, read from the official repository at commit `1e5c90a4b6f249917bd21fe361b3a2a7deb741b8` (committed 2026-10-14 00:04 PDT / 09:04 CEST) |
| Local copy | A cached copy on the research machine was version 0.15.23 and differed in several files. **We used the official repository as the primary source** and the local copy only as a cross-check. |
| License | MIT |
| Size | 54 skill directories (24 of them principle skills), 23 playbooks in the `poteto-mode` skill, a 10-page guide (about 11,300 words), a dormant automation pack ("benny") |
| BibTeX key | `tan2026pstack` |

The README describes the author's background: "i've worked with millions of lines of code at Meta, Netflix, and Cursor", and membership of the React core team. We report this as the author's self-description; it is not relevant evidence for the effectiveness of the practices.

## 2. What pstack is

pstack is a set of instruction files ("skills") for the Cursor coding agent. They encode one engineer's way of working. The entry point, `/poteto-mode`, reads the user's request, matches it to one of 23 playbooks (investigation, bug fix, perf, feature, refactoring, prototype, eval, babysit, shipping, autonomous run, orchestrate, and others), copies the playbook's steps into a to-do list, and calls other skills as steps require. The stated aim is quality over volume: "pstack helps you write less, but higher quality code" (README).

In the terms of Chapter 01, pstack is an artefact of **layer L2 (harness, specifically procedural memory in the form of instruction files)**, **L3 (coordination: sub-agents, swarms, multi-model review)**, and **L4 (oversight: finish conditions, decision logs, pause rules)**.

## 3. Practices

We group the practices by the lifecycle activities of Chapter 01 §3.2. Quotations are brief and taken from the official repository.

### 3.1 Specification: finish conditions

- The guide's central instruction: "Give the agent a goal and a way to check it" (guide README).
- A finish condition must be checkable: "a duration is not a finish condition … Give `/loop` a predicate that can pass or fail" (guide 07).
- For overnight runs, the guide prescribes an "overnight contract": goal, finish condition, permissions, and an escape hatch (guide 07).

*AAE reading [OP]:* this is the **done predicate** $D$ of Chapter 03 §1.1, made a user-facing habit. It corresponds to our untested hypothesis that done-predicate quality strongly affects outcomes (agenda Q3).

### 3.2 Design: prototypes and parallel exploration

- "Exhaust the Design Space": build "two or three competing prototypes when there's no precedent" (guide 08).
- Forks that can be settled by observation are not to be asked of the human: "If the answer is a fact you could observe by running something … it is not the human's to answer. Sketch it via the Prototype playbook" (`poteto-mode/SKILL.md`).
- Skills `architect` (parallel design exploration), `arena` (bake-offs with grafting), and `swarm` (fan-out of parallel workers) implement this.
- An explicit design stance against upfront planning: "personally, i don't believe in planning. the best spec is code" (README).

### 3.3 Construction: subtraction and structure

- Core principles prefer deletion and minimal change ("Laziness Protocol", "Subtract Before You Add"), choosing data structures first ("Foundational Thinking"), and encoding repeated rules in one structure ("Model the Domain").
- "Encode Lessons in Structure": turn a correction given twice "into a lint, check, or script" rather than more text (guide 08). The `/correct` skill applies this repository-wide.

### 3.4 Verification

Verification is the most developed part of pstack. Its components:

1. **Verify the real artefact.** The principle "Prove It Works": "Verify every task output by checking the real thing directly. Do not infer from proxies, self-reports, or 'it compiles.'" It adds: "When verification fails, suspect the observation method before suspecting the system" (`principle-prove-it-works`).
2. **Match the check to the change** (guide 06): a CLI change runs the real command; a UI change walks the flow in the running app; a parser replays saved input; a perf change compares profiles; a storage change reads back the written value.
3. **Inconclusive is a valid result.** "If a check couldn't run, a good reply says 'inconclusive', and you should treat a confident reply without evidence as a red flag" (guide 06).
4. **Vet numbers.** `/benchmark-checklist` asks seven questions before a measured number is reported, among them what limits the number, whether both sides ran tuned like production, whether the result breaks a physical limit, whether it reproduces over alternating runs with a median and range, and whether the work happened inside the timed region (guide 06).
5. **Project verification skills.** `/create-verification-skill` generates a repository-specific skill with Launch, Doctor, Drive, Evidence, and Cleanup sections plus a feature map, and must prove itself once end to end before use. `/maintain-verification-skill` audits it on a schedule, ending in exactly one of `clean`, `changed`, or `blocked` (guide 06).
6. **Separation of author and judge.** In the Shipping playbook, "One fresh agent per PR proves the behavior live, and the agent that judges a change is never the one that wrote it", and only "the contiguous verified run from the bottom" of a PR stack is landed (guide 06).
7. **Multi-model adversarial review.** `/interrogate` spawns one reviewer per configured model; "The adversarial signal comes from model diversity, not assigned personas" (`interrogate/SKILL.md`).
8. **Tests that test behaviour.** "If the test would still pass when every imported function returns `undefined`, rewrite the assertion or delete the test" (`principle-test-behavior-not-implementation`).

### 3.5 Evaluation of the harness itself

The `eval` playbook describes how to test a change to a skill or prompt: blinded candidates on different models, a sanitised environment with no words like "eval" or "benchmark" visible to the candidate, a held-back rubric, a blinded judge from a different model family, and grading "chain-following from the files it really read plus the shape of the code, never from the candidate's own claims" (`playbooks/eval.md`).

*AAE reading [OP]:* this is a small-scale, blinded A/B protocol for the harness. It is methodologically more careful than most published practitioner advice. It also has small samples by design, and the judge is itself a model. Its results are not published, so we cannot assess them.

### 3.6 Operation and oversight

- **Autonomy policy:** "Reversible work and external actions … proceed without asking", while the agent must "Always pause for irreversible writes: force-push to shared branches, deploys, data deletion, customer messages" (`poteto-mode/SKILL.md`).
- **"Never Block on the Human":** proceed on reversible work and present the result; reserve confirmation for irreversible actions (guide 08).
- **Decision logs:** `/show-me-your-work` keeps a TSV with time, phase, decision, reason, evidence pointer, and result. Before summarising, a reviewer from a different model family reads the trail and lists what deserves scrutiny (guide 07).
- **Earning trust before loops:** run a task by hand or watch an agent do it first; make sure the agent has your tools and signals; make every stage able to "stop the line"; turn repeated failures into tools (guide 07).
- **Context hygiene:** "Guard the Context Window": route bulk work to sub-agents and keep summaries in the main thread (README principles table).

## 4. Principles

pstack ships 24 named principles in five groups (guide 08):

| Group | Principles |
|---|---|
| Core | Laziness Protocol; Foundational Thinking; Redesign from First Principles; Attack the Premise; Subtract Before You Add; Minimize Reader Load; Outcome-Oriented Execution; Experience First; Exhaust the Design Space; Build the Lever |
| Architecture | Model the Domain; Boundary Discipline; Type System Discipline; Make Operations Idempotent; Migrate Callers Then Delete Legacy APIs; Separate Before Serializing Shared State |
| Verification | Prove It Works; Fix Root Causes; Sequence Work into Verifiable Units; Test Behavior, Not Implementation; Explain the Number |
| Delegation | Guard the Context Window; Never Block on the Human |
| Meta | Encode Lessons in Structure |

A distinctive mechanism is using principle *names* to steer: "one phrase redirects the work more precisely than a paragraph of instructions", with the requirement that the agent state which decision each cited principle changed, because "A principle citation with no decision behind it is the tell that it name-dropped instead of applying" (guide 08).

Many principles restate long-standing software engineering advice (root-cause analysis, idempotency, validating at boundaries, making illegal states unrepresentable). What is new is packaging them as agent-readable, individually loadable instructions with explicit triggers.

## 5. Documented outcomes

We searched the official repository (README, guide, playbooks, and principle skills at the commit above) for reported outcomes.

| Claimed outcome | Where | Type | Our assessment |
|---|---|---|---|
| "these are the same skills i use everyday to ship high quality code at Cursor" | README | Author's self-report of use | **[EE]** No data on code quality, defect rates, or review outcomes is provided. |
| "pstack helps you write less, but higher quality code" | README, `plugin.json` | Design goal / claim | **[EE]** Unmeasured in the repository. |
| "fearless parallelism … trust that they'll apply rigorous engineering principles" | README | Claim about agent behaviour | **[EE]** Unmeasured. |
| `/poteto-mode` with `/loop` lets Cursor "work for many hours without sacrificing rigor" | README | Claim | **[EE]** Unmeasured. |
| Worked pitfalls, e.g. "Parallel agents in one worktree … overwrite each other" | Guide 10 | Reported failure patterns | **[EE]** Plausible and consistent with general SE knowledge about shared state. Frequencies are not reported. |

**Finding:** the repository documents *practices and rationales*, not *measured outcomes*. There are no reported success rates, before-and-after comparisons, user studies, or eval results. This is normal for practitioner tooling, and it means pstack is a source of **hypotheses**, not evidence.

## 6. Relation to research evidence

Where pstack's practices touch questions the literature has studied, the evidence is mixed in strength:

| pstack practice | Closest research evidence | Relationship |
|---|---|---|
| Verify the real artefact, not the build | Weak tests let invalid patches pass on SWE-bench [@aleithan2024swebenchplus] **[PP]**; agents make "unsupported claims of completion" [@wang2026agentswe] **[PP]**; user-observable verification in SWEeper-Bench [@yao2026sweeper] **[PP]** | Consistent: these studies document the failure the practice targets. None tests the practice itself. |
| Careful tool and interface design; small composable CLIs with machine-readable output | ACI ablations [@yang2024sweagent] **[PR]**; vendor tool-design experience [@anthropic2024effective] **[VC]** | Consistent in spirit. pstack's specific CLI traits are untested. |
| Guard the context window via sub-agents | Position effects in long contexts [@liu2024lost] **[PR]**; history collapsing helped in SWE-agent [@yang2024sweagent] **[PR]** | Indirect support. No direct test of sub-agent summarisation in ASE. |
| Author–judge separation; model diversity in review | Learned verifiers for patch selection [@pan2025swegym] **[PR]** | Related but different mechanism. The diversity claim is untested. |
| Vet measured numbers (benchmark checklist) | Benchmark and oracle audits [@chen2026oracle] **[PP]**, [@ding2026reexec] **[PP]** | Same epistemic concern, applied at different scales. |
| Encode lessons in structure; test harness changes blind | Cortex: keep instruction-file changes only if repeated runs show net gain [@giampieri2026cortex] **[PP]** | Very close in intent. Cortex adds automated measurement gating. |
| Preserve earlier behaviour; small verifiable units | Inherited test failures drive downstream cost of agent changes [@pan2026maintain] **[PP]** | Consistent. |
| Pause for irreversible actions | Boundary-violation benchmark [@trong2026misbehavior] **[PP]**; MCP consent requirements [@mcp2026spec] **[VC]** | Consistent. pstack's "proceed without asking" for reversible and external actions is more permissive than MCP's guidance that hosts obtain consent before invoking any tool. The two operate at different layers, but the tension is worth noting. |

## 7. Limitations of this case study

1. **No outcome data** (§5). We could not assess effectiveness.
2. **Single author, single tool.** Practices are tuned to one engineer's style and to Cursor's agent features (custom modes, `/loop`, cloud sub-agents). The README is explicit that "`poteto-mode` is my style" and provides `/automate-me` to derive a personal variant.
3. **Fast-moving source.** Version 0.15.24 was committed on the day we read it, and the local cached copy (0.15.23) already differed. Statements here may be outdated quickly.
4. **Model-specific defaults.** Defaults name specific vendor models for roles. This is configurable, but it means behaviour depends on which models a user has.
5. **Security surface.** As a set of skills that agents load and that can write artefacts reused later, pstack belongs to the class of systems studied for cross-session skill attacks [@liao2026skillrelay] **[PP]**. We did not audit it.
6. **Our position.** The notebook's maintainer is a user of agentic coding tools, and the draft was produced with agent assistance. That could bias the reading in pstack's favour. We have tried to counter it by reporting the absence of outcome data plainly.

## 8. What would turn these practices into evidence? [OP]

- A **within-subject study**: the same engineers on matched tasks, with and without the verification practices (finish conditions, real-artefact checks, author–judge separation), measuring escaped defects and reviewer time.
- **Ablations of the harness**: remove one principle or skill at a time and measure, using a protocol like pstack's own `eval` playbook or Cortex's measurement gating, with enough runs to estimate variance.
- **Log analysis** of decision logs (`decisions.tsv`) across many runs: how often did "inconclusive" occur, and how often did a reviewer catch a problem the author agent missed?

These are recorded as agenda items Q3, Q7, and Q9.

## References

`tan2026pstack`, `aleithan2024swebenchplus`, `wang2026agentswe`, `yao2026sweeper`, `yang2024sweagent`, `anthropic2024effective`, `liu2024lost`, `pan2025swegym`, `chen2026oracle`, `ding2026reexec`, `giampieri2026cortex`, `pan2026maintain`, `trong2026misbehavior`, `mcp2026spec`, `liao2026skillrelay` (see [`references.bib`](../references.bib)).
