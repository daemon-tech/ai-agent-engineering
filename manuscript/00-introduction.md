# AI Agent Engineering: An Introductory Manuscript

*AAE Research Notebook v0.1. Draft of 2026-10-14. Not peer reviewed.*

## Abstract

Language-model agents, meaning systems in which a large language model repeatedly chooses actions, observes their effects, and continues until a goal is met, have moved from research prototypes to everyday software engineering tools within roughly four years. The research describing them is fragmented. Agent architectures appear at machine learning venues, coding agents and their benchmarks at both ML and software engineering venues, and much of the operational knowledge about building reliable agents exists only as vendor posts and practitioner tooling. This manuscript introduces the AAE Research Notebook, an open effort to consolidate that knowledge under explicit evidence standards. We (i) summarise the established research lineage from reasoning-and-acting prompting to repository-level software agents; (ii) set out the conceptual foundations we use (agent, environment, harness, verification signal); (iii) describe a sourcing method in which every claim carries one of five evidence classes; and (iv) identify challenges that cut across agent applications: benchmark validity, verification, context management, human oversight, and the security of agent tooling. We propose, as a hypothesis rather than a finding, that these recurring problems justify treating *AI Agent Engineering* (AAE) as an engineering discipline in its own right, and we start with Agentic Software Engineering, where verification signals are unusually strong. The contribution of v0.1 is a verified bibliography, a structured vocabulary, and a research agenda, not new empirical results.

## 1. Introduction

### 1.1 Motivation

In October 2023 the strongest system evaluated on SWE-bench, a benchmark of 2,294 real GitHub issues from 12 Python repositories, resolved 1.96% of them (Claude 2 with BM25 retrieval) [@jimenez2024swebench] **[PR]**. Seven months later, an agent that interacts with the repository through a purpose-built interface resolved 12.47% of the full test set with GPT-4 Turbo [@yang2024sweagent] **[PR]**. Since then, newer and harder benchmarks have appeared because the older ones were judged insufficient or compromised [@chowdhury2024sweverified] **[VC]**, [@deng2025swebenchpro] **[PP]**, [@zheng2026sweproverified] **[PP]**.

Benchmark numbers are not the only signal. A randomized controlled trial with 16 experienced open-source developers found that allowing early-2025 AI tools *increased* task completion time by 19%, although developers believed it had reduced it by 20% [@becker2025uplift] **[PP]**. That result does not generalise to every setting, and its authors discuss why. It is enough to show that capability on benchmarks, perceived productivity, and measured productivity can diverge, and that engineering practice around agents needs more careful study than it has received.

### 1.2 Problem statement

Practitioners building agents face recurring design questions: how to structure the control loop; which tools to expose and how; what to put in the model's context; when to split work across several agents; how to verify that an agent's output is correct; when a human must approve an action; and how to evaluate any of this. The literature offers partial and scattered answers, often under different names. Evidence quality varies widely: a NeurIPS paper with ablations, an arXiv preprint posted last week, a vendor's account of its own internal practice, and a practitioner's open-source workflow are frequently cited side by side as if they were equivalent.

### 1.3 Contributions of v0.1

1. A **verified bibliography** (52 entries), each checked against its primary record, with peer-reviewed status confirmed on the venue's own pages (`references.bib`, `references-verification.md`).
2. An **evidence-class system** applied to every substantive claim (METHODOLOGY.md).
3. A **proposed definition and taxonomy** of AAE, explicitly labelled as our proposal (Chapter 01).
4. An **introduction to Agentic Software Engineering** (Chapter 02) and a **technical chapter on agent architectures** (Chapter 03).
5. **Annotated entries** for ReAct, SWE-bench, and SWE-agent, a **case study** of one practitioner workflow (pstack), a **dated frontier review**, and a **research agenda** of open questions.

### 1.4 What we do not claim

We do not claim that AAE is an established discipline, that our taxonomy is complete, or that any practice described here causes better outcomes unless a cited study shows it. We report no new experiments.

## 2. Background

### 2.1 Agents before language models

The notion of an *agent* predates LLMs by decades. Wooldridge and Jennings's 1995 survey characterised agents by properties such as autonomy, social ability, reactivity, and pro-activeness, and distinguished agent theory, architectures, and languages [@wooldridge1995intelligent] **[PR]**. Two of their concerns carry over directly: the tension between deliberation and reaction, and the question of how an agent's internal state relates to its actions. Sumers et al. later explicitly connected LLM agents to the cognitive-architecture tradition in their CoALA framework, which organises language agents by memory, action space, and decision procedure [@sumers2024coala] **[PR]**.

### 2.2 From prompting to reasoning to acting

Three steps in the ML literature are foundational for what follows.

- **Intermediate reasoning.** Chain-of-thought prompting showed that eliciting intermediate reasoning steps improves performance on multi-step reasoning tasks for sufficiently large models [@wei2022chain] **[PR]**. Least-to-most prompting decomposes a problem into simpler subproblems solved in sequence [@zhou2023leasttomost] **[PR]**.
- **Interleaving reasoning with actions.** ReAct prompted models to alternate free-text "thoughts" with actions against an external environment (a Wikipedia API, a text game, a web shop) and to condition on the resulting observations [@yao2023react] **[PR]**. This is the template for most contemporary agent loops. See [papers/react.md](../papers/react.md).
- **Tool use.** Toolformer trained a model to decide when to call external APIs in a self-supervised way [@schick2023toolformer] **[PR]**. CodeAct argued for executable Python code as a unified action space and reported up to 20% higher success than text or JSON actions across the benchmarks it studied [@wang2024codeact] **[PR]**.

Additional lines address feedback and search. Reflexion stores verbal self-reflections in an episodic memory between trials [@shinn2023reflexion] **[PR]**; Self-Refine iterates generate-critique-revise with the same model [@madaan2023selfrefine] **[PR]**; Tree of Thoughts searches over intermediate "thoughts" with lookahead and backtracking [@yao2023tree] **[PR]**. Retrieval-augmented generation supplies external documents at generation time [@lewis2020rag] **[PR]**.

### 2.3 Agents for software engineering

Software engineering became a major testbed for agents because repositories provide executable feedback. SWE-bench framed the task as producing a patch that makes hidden fail-to-pass tests pass [@jimenez2024swebench] **[PR]**. SWE-agent introduced the *agent-computer interface* (ACI) and showed with ablations that interface design (search, file viewing, editing with a linter guardrail, history handling) changed resolve rates substantially [@yang2024sweagent] **[PR]**. AutoCodeRover combined LLMs with program-structure-aware code search [@zhang2024autocoderover] **[PR]**. OpenHands provided an open platform for software-developer agents [@wang2025openhands] **[PR]**. Agentless questioned whether autonomous agents are needed at all, using a fixed localise-repair-validate pipeline [@xia2025agentless] **[PR]**. Multi-agent "virtual software company" designs such as ChatDev and MetaGPT assigned roles to communicating agents [@qian2024chatdev] **[PR]**, [@hong2024metagpt] **[PR]**.

The software engineering community has begun to frame the agentic shift at the discipline level. Hassan et al. proposed "SE 3.0", an AI-native, intent-centric vision of software engineering [@hassan2026se3] **[PR]**, and a roadmap for *Agentic Software Engineering* that distinguishes "SE for Humans" from "SE for Agents" [@hassan2025agenticse] **[PP]**, also published as a two-page ICSE 2026 item [@hassan2026icse] **[PUB]**. Hou et al.'s systematic literature review maps LLM use across SE tasks more broadly [@hou2024llm4se] **[PR]**. Chapter 02 covers this in detail.

### 2.4 Practice ahead of evidence

A great deal of agent engineering knowledge is published by vendors and practitioners. Anthropic's "Building effective agents" distinguishes *workflows* (LLMs orchestrated through predefined code paths) from *agents* (LLMs that "dynamically direct their own processes and tool usage") and recommends starting from the simplest solution [@anthropic2024effective] **[VC]**. The Model Context Protocol standardises how applications expose tools and context to models; its most recent revision we found as of 2026-10-14 is dated 2026-07-28 [@mcp2026spec] **[VC]**. Practitioner workflows such as pstack encode verification and delegation practices as reusable instructions [@tan2026pstack] **[EE]**. These sources are useful and often precede research, but they are not controlled evidence, and we label them accordingly.

## 3. Conceptual foundations

This section fixes the vocabulary used throughout. Where a term is established we cite its source; where we sharpen or introduce a term, it is tagged **[OP]**. The full list is in [GLOSSARY.md](../GLOSSARY.md).

### 3.1 Agent

We use a functional definition consistent with the literature above: an **LLM agent** is a system in which a language model, at each step, selects an action conditioned on a goal and on the history of prior actions and observations, the action is executed against an environment, and the resulting observation is fed back, until a termination condition holds. Anthropic's workflow/agent distinction is a useful boundary marker: if the sequence of steps is fixed by code, the system is a *workflow*; if the model chooses the next step, it is an *agent* [@anthropic2024effective] **[VC]**. Real systems mix both.

### 3.2 Environment, action space, and interface

The **environment** is everything the agent acts upon: a repository, a shell, a browser, an issue tracker, other agents, a human. The **action space** is the set of actions the agent can emit. The **interface** maps actions to effects and effects to observations. SWE-agent's main finding is that this interface is itself an engineering object with measurable consequences [@yang2024sweagent] **[PR]**.

### 3.3 Harness

**[OP, building on recent usage.]** We use **harness** for the non-model software around an agent: the loop, the tool definitions and their implementations, context construction, memory stores, permission checks, sandboxes, logging, and verification hooks. The term is in active use. Recent reviews use "harness engineering" for exactly this layer [@zhou2026externalization] **[PP]**, [@guo2026harness] **[PP]**, and Cortex uses "harness" for the instruction files a coding agent follows [@giampieri2026cortex] **[PP]**. Usage is not yet settled, so we define our meaning explicitly. In our usage, instruction files are part of the harness, but the harness is broader.

### 3.4 Verification signal

**[OP.]** A **verification signal** is any observation that bears on whether the agent's output meets the goal: a test result, a type check, a reproduced bug, a screenshot, a human review. Signals differ in *strength* (how well they discriminate correct from incorrect outputs) and *availability* (whether the agent can obtain them itself). Benchmark studies show that even the signals used for scoring can be weak: SWE-Bench+ reported that 31.08% of the passed patches it examined were suspicious because of weak tests [@aleithan2024swebenchplus] **[PP]**, and OpenAI's annotation of SWE-bench flagged 61.1% of sampled tasks for unit tests that may unfairly reject valid solutions [@chowdhury2024sweverified] **[VC]**. Verification signal quality is therefore a central object of study, not a given.

### 3.5 Autonomy and oversight

**[OP.]** We describe the human's role along two axes: **delegation scope** (how much of the task the agent owns: a single edit, a pull request, a stack of changes, a standing project) and **oversight point** (where a human checks: before each action, before irreversible actions, at merge, or after the fact). These are independent. An agent can own a large scope with tight checkpoints, or a small scope with none.

## 4. Methodology of this notebook

The notebook is a structured narrative review, not a systematic review. Its method, given in full in [METHODOLOGY.md](../METHODOLOGY.md), rests on four rules:

1. **Primary-source verification.** Every bibliographic field comes from the primary record. Peer-reviewed status was confirmed on the venue's own proceedings page or the publisher DOI, not from author comments. On 2026-10-14, OpenReview blocked automated access, so ICLR acceptances were confirmed through `proceedings.iclr.cc` and `iclr.cc/virtual`.
2. **Evidence classes** [PR], [PUB], [PP], [VC], [EE], [OP] on every substantive claim.
3. **Numbers with setup.** Every quoted number gives at least the benchmark split and model.
4. **Dated frontier reviews.** Recent work is recorded with publication date, review date, mechanism, verification status, and limits ([notes/2026-10-frontier-review.md](../notes/2026-10-frontier-review.md)).

We do not claim completeness, and the frontier scan for v0.1 covers one week of arXiv `cs.SE` submissions.

## 5. Challenges

The following challenges recur across the literature we reviewed. Each is developed in later chapters and in the [research agenda](../notes/open-questions.md).

### 5.1 Benchmark validity

Repository-level benchmarks rely on tests written for human pull requests, on issue texts that may be underspecified, and on public repositories that models may have seen in training. Each of these has been documented as a threat: underspecified issues and over-specific tests [@chowdhury2024sweverified] **[VC]**; solution leakage in issue text and weak tests [@aleithan2024swebenchplus] **[PP]**; memorisation signals such as identifying buggy file paths from issue text alone with up to 76% accuracy on SWE-bench Verified versus up to 53% on repositories outside SWE-bench [@liang2025illusion] **[PP]**. Successor benchmarks have themselves been audited and revised [@zheng2026sweproverified] **[PP]**. Evaluation harnesses are software, and they can be buggy: one October 2026 audit reports a reward-function defect whose correction lowered a benchmark's measured success from 94.3% to 65.5% [@chen2026oracle] **[PP]**.

### 5.2 Verification beyond tests

Passing tests is not the same as being correct, and agents do not always produce the evidence that would show correctness. Recent benchmarks shift attention to agents *discovering* failures through interaction [@yao2026sweeper] **[PP]** and to the gap between what an agent demonstrates and what it delivers, including "unsupported claims of completion" [@wang2026agentswe] **[PP]**. Practitioner workflows put verification against "the real artifact" at the centre of their design [@tan2026pstack] **[EE]**.

### 5.3 Context and memory

Models do not use long contexts uniformly. Performance can degrade when relevant information sits in the middle of a long input [@liu2024lost] **[PR]**. Agent designs respond with retrieval, summarisation, history truncation, external memory, and sub-agent delegation [@yang2024sweagent] **[PR]**, [@packer2023memgpt] **[PP]**, [@park2023generative] **[PR]**. Which of these work, and when, is an open question.

### 5.4 Long-horizon work and maintenance

Benchmarks typically score single tasks. Real repositories accumulate the agent's own prior changes. A recent preprint reports that starting later tasks from agent-written history lowers later-task resolution by 5.6 percentage points on average, with the cost tied mainly to inherited test failures [@pan2026maintain] **[PP]**. Time-horizon measurements suggest the length of tasks agents can complete has grown quickly, with a doubling time of approximately seven months on the task suite studied [@kwa2025horizon] **[PR]**. Both results are bounded by their task suites.

### 5.5 Boundaries, permissions, and security

Agents act on real systems, so failures include unintended actions, not only wrong answers. A new benchmark taxonomises boundary-violating behaviours such as unintended modification of user inputs [@trong2026misbehavior] **[PP]**. Reusable skill packages create cross-session attack surfaces through persistent artifacts [@liao2026skillrelay] **[PP]**. The MCP specification itself states that tool descriptions "should be considered untrusted, unless obtained from a trusted server" [@mcp2026spec] **[VC]**.

### 5.6 Human factors and productivity

Measured productivity effects are mixed and setting-dependent [@becker2025uplift] **[PP]**. How to allocate human attention (review, approval, specification) across many concurrently running agents is mostly addressed in practitioner material, not in controlled studies [@tan2026pstack] **[EE]**, [@hassan2025agenticse] **[PP]**.

## 6. Discussion

### 6.1 Why a discipline-level framing? [OP]

Our working hypothesis is that the problems in Section 5 recur regardless of the application domain and require a shared body of engineering knowledge. That knowledge covers interface design, context construction, verification, evaluation methodology, oversight design, and agent-tooling security. Software engineering for agents is the most mature instance. A discipline-level framing would be justified if (a) the same design principles transfer across domains, (b) the field accumulates methods with known validity, and (c) practitioners can be trained in it. None of these is yet demonstrated. Chapter 01 proposes a definition and taxonomy so the hypothesis can be examined.

### 6.2 Relation to existing framings

AAE overlaps with several existing efforts. "Agentic Software Engineering" and "SE 3.0" come from the SE community [@hassan2025agenticse] **[PP]**, [@hassan2026se3] **[PR]**. "Harness engineering" is emerging in agent-systems reviews [@zhou2026externalization] **[PP]**. The phrase "agent engineering" also circulates in practitioner writing. We do not claim priority for any of these terms. The contribution we intend is methodological: an evidence-labelled synthesis that keeps findings, claims, experience, and proposals apart.

### 6.3 Limitations of this manuscript

The manuscript relies heavily on abstracts and selected sections for the frontier items, which are first-version preprints that are days old. It has not been externally reviewed. Its authors practise what it studies.

## 7. Conclusion

LLM agents are now ordinary software engineering tools, but the knowledge about how to engineer them well is uneven in quality and scattered across communities. This notebook starts a careful consolidation. It verifies its sources, labels every claim, keeps our proposals distinct from established research, and treats benchmark numbers as measurements with setups rather than as rankings. Version 0.1 lays the foundation; the [research agenda](../notes/open-questions.md) lists what would need to be learned for the AAE hypothesis to stand or fall.

## References

All keys resolve in [`references.bib`](../references.bib). Cited in this chapter:
`wooldridge1995intelligent`, `sumers2024coala`, `wei2022chain`, `zhou2023leasttomost`, `yao2023react`, `schick2023toolformer`, `wang2024codeact`, `shinn2023reflexion`, `madaan2023selfrefine`, `yao2023tree`, `lewis2020rag`, `jimenez2024swebench`, `yang2024sweagent`, `zhang2024autocoderover`, `wang2025openhands`, `xia2025agentless`, `qian2024chatdev`, `hong2024metagpt`, `hassan2026se3`, `hassan2025agenticse`, `hassan2026icse`, `hou2024llm4se`, `anthropic2024effective`, `mcp2026spec`, `tan2026pstack`, `chowdhury2024sweverified`, `deng2025swebenchpro`, `zheng2026sweproverified`, `becker2025uplift`, `zhou2026externalization`, `guo2026harness`, `giampieri2026cortex`, `aleithan2024swebenchplus`, `liang2025illusion`, `chen2026oracle`, `yao2026sweeper`, `wang2026agentswe`, `liu2024lost`, `packer2023memgpt`, `park2023generative`, `pan2026maintain`, `kwa2025horizon`, `trong2026misbehavior`, `liao2026skillrelay`.
