# Chapter 02: Agentic Software Engineering

*AAE Research Notebook v0.1, 2026-10-14. Not peer reviewed.*

## 1. Scope and terminology

**Agentic Software Engineering (ASE)** is the term we use for software engineering in which LLM agents carry out multi-step engineering tasks, such as localising a defect, editing code, running tests, and preparing a change for review, with some autonomy. Two things should be said at the outset.

1. **The term is not ours.** Hassan et al. use "Agentic Software Engineering" and equate it with "SE 3.0", describing "a new era where intelligent agents are tasked not with simple code generation, but with achieving complex, goal-oriented SE objectives" [@hassan2025agenticse] **[PP]**. A two-page version appears in the ICSE 2026 proceedings [@hassan2026icse] **[PUB]**. The broader SE 3.0 vision ("AI-native", "intent-centric, conversation-oriented development") is published in TOSEM [@hassan2026se3] **[PR]**. A 2026 International Workshop on Agentic Engineering has ACM-published proceedings, including, for example, a vision for agentic software project management [@assalaarachchi2026agenticpm] **[PUB]**; we did not verify its parent conference or review process.
2. **ASE has two faces.** Following Hassan et al.'s duality of "SE for Humans" and "SE for Agents" [@hassan2025agenticse] **[PP]**, ASE covers both (a) using agents to do software engineering and (b) re-engineering software engineering itself (its processes, tools, artefacts, and roles) so that agents can participate safely. The AAE notebook studies both, and frames (b) as layers L4–L5 of the taxonomy in Chapter 01 **[OP]**.

## 2. A short history of the task

The task of turning an issue description into a correct patch existed long before LLMs as *automated program repair*. LLM-era ASE changed three things: the input became natural-language issues rather than failing tests alone; the scope became whole repositories; and the system began to *act*, navigating, running code, and observing results, instead of producing a single output.

| Period | Representative work | What changed | Evidence |
|---|---|---|---|
| 2022–2023 | ReAct, Toolformer, Reflexion | Models interleave reasoning with actions and tool calls; feedback across attempts | [@yao2023react], [@schick2023toolformer], [@shinn2023reflexion] **[PR]** |
| Oct 2023 | SWE-bench | Repository-level issue resolution becomes a public benchmark; best reported model resolves 1.96% | [@jimenez2024swebench] **[PR]** |
| 2023–2024 | ChatDev, MetaGPT | Role-based multi-agent "software company" designs | [@qian2024chatdev], [@hong2024metagpt] **[PR]** |
| Apr–May 2024 | AutoCodeRover, SWE-agent | Structure-aware code search; agent-computer interfaces | [@zhang2024autocoderover], [@yang2024sweagent] **[PR]** |
| Jul 2024 | Agentless, OpenHands | A fixed pipeline rivals agents; an open platform for agent development | [@xia2025agentless], [@wang2025openhands] **[PR]** |
| Aug 2024 | SWE-bench Verified | Human-screened 500-task subset; benchmark validity becomes a first-class concern | [@chowdhury2024sweverified] **[VC]** |
| Oct 2024 onward | SWE-bench Multimodal, SWE-Bench+, SWE-Gym | Beyond Python and text; audits of solution leakage; training environments | [@yang2025swebenchmm], [@pan2025swegym] **[PR]**; [@aleithan2024swebenchplus] **[PP]** |
| 2025 | Time horizons, developer RCT, contamination probes, SWE-Bench Pro | Measurement shifts toward task length, real-world productivity, contamination resistance | [@kwa2025horizon] **[PR]**; [@becker2025uplift], [@liang2025illusion], [@deng2025swebenchpro] **[PP]** |
| 2026 | SE 3.0 in TOSEM; audits of benchmarks and harnesses; maintenance and boundary studies | Discipline-level framing; evaluation reliability; long-horizon and safety concerns | [@hassan2026se3] **[PR]**; see [frontier review](../frontier/2026-10-frontier-review.md) **[PP]** |

## 3. The core task and how it is scored

The canonical ASE evaluation task, as defined by SWE-bench [@jimenez2024swebench] **[PR]**:

- **Input:** a repository snapshot and an issue description.
- **Output:** a patch.
- **Scoring:** apply the patch and run tests. *Fail-to-pass* tests, which failed before the reference pull request and pass after it, must pass. Tests that passed before must still pass. The metric is the percentage of instances resolved.
- **Construction:** about 90,000 pull requests from 12 popular Python repositories were filtered in three stages (repository selection, attribute filtering, execution-based filtering) to 2,294 task instances.

This design has the great virtue of being executable. It also embeds specific assumptions that later work has examined, which we discuss in Section 6.

## 4. Families of ASE systems

We group systems by **who decides the next step** and **how the agent touches the repository**. The grouping is our own **[OP]**; the systems and their reported results are from the cited sources.

### 4.1 Interactive single agents

The model runs a loop: observe, decide, act, repeat. The repository is accessed through a set of commands.

- **SWE-agent** gives the model a small set of LM-oriented commands for searching (`find_file`, `search_file`, `search_dir`), a file viewer showing at most 100 lines at a time, and an edit command integrated with a linter. Earlier observations are collapsed so that only the last five are shown in full. With GPT-4 Turbo it resolved 12.47% (286/2,294) of the full SWE-bench test set and 18.00% (54/300) of SWE-bench Lite, at a $4 per-instance budget [@yang2024sweagent] **[PR]**. Ablations on Lite showed, for instance, that removing the edit command lowered the score from 18.0% to 10.3%. See [papers/swe-agent.md](../papers/swe-agent.md).
- **OpenHands** is a platform for agents that write code, use a command line, and browse the web in sandboxed environments, evaluated across 15 tasks including SWE-bench and WebArena [@wang2025openhands] **[PR]**.
- **CodeAct** uses executable Python as the action language, letting the agent compose tools in code [@wang2024codeact] **[PR]**.

### 4.2 Structured pipelines ("agentless")

The sequence of phases is fixed by the system designer; the model fills in each phase.

- **Agentless** uses three phases: localisation, repair, and patch validation, "without letting the LLM decide future actions or operate with complex tools". It reported 32.00% (96 fixes) on SWE-bench Lite at an average cost of $0.70, the highest among the open-source systems it compared against at the time [@xia2025agentless] **[PR]**.
- **AutoCodeRover** combines LLMs with code search over the abstract syntax tree (classes and methods) and, when tests exist, spectrum-based fault localisation. It reported 19% on SWE-bench Lite at an average cost of $0.43 [@zhang2024autocoderover] **[PR]**.

The Agentless result is important for AAE because it shows that *more autonomy is not automatically better*. A well-designed fixed workflow can compete with an interactive agent on a given benchmark. This matches the vendor advice to start with the simplest solution and add agentic complexity only "when it demonstrably improves outcomes" [@anthropic2024effective] **[VC]**.

### 4.3 Multi-agent role designs

- **ChatDev** organises role-specialised agents through a "chat chain" for design, coding, and testing, with "communicative dehallucination" [@qian2024chatdev] **[PR]**.
- **MetaGPT** encodes Standardised Operating Procedures into prompt sequences and assigns roles in an "assembly line paradigm" [@hong2024metagpt] **[PR]**.
- **AutoGen** is a general framework for conversing agents, used among other things for coding [@wu2023autogen] **[PR]**.

These systems were mostly evaluated on generating new, relatively small programs rather than on modifying large existing repositories. How well role-based decomposition works for repository-scale maintenance is an open question (agenda, Q6).

### 4.4 Trained agents and verifiers

**SWE-Gym** provides 2,438 Python task instances with executable environments for *training* agents. The authors report up to 19% absolute gains in resolve rate from fine-tuning, and, with verifiers trained on agent trajectories for inference-time selection, 32.0% on SWE-bench Verified and 26.0% on Lite for open-weight agents [@pan2025swegym] **[PR]**. This line of work connects ASE to the L1 layer (model policy) and to verification: a learned verifier is a verification signal the system produces for itself.

## 5. What ASE agents do, step by step

Across the systems above, the same functional steps recur, implemented differently **[OP, synthesis]**:

1. **Understand the request**: read the issue; identify ambiguity.
2. **Localise**: find relevant files and functions (search commands, AST-aware search, retrieval, fault localisation).
3. **Reproduce**: construct a failing test or script that exhibits the problem.
4. **Edit**: produce a change (whole-file rewrites, line-range edits, diffs, or code actions).
5. **Validate**: run tests, linters, type checkers, the reproduction script, or the application.
6. **Iterate or select**: retry on failure, or generate several candidates and choose among them (Agentless's validation phase, SWE-Gym's verifiers).
7. **Hand off**: present the change and its evidence to a human or a downstream system.

Steps 3, 5, and 7 produce the **verification evidence**. Benchmarks score steps 4–6 indirectly through hidden tests. Step 7 is barely studied in the research literature, yet it is where practitioner workflows invest most effort (see the [pstack case study](../case-studies/pstack.md) **[EE]**). Hassan et al.'s proposed "Merge-Readiness Packs" are one attempt to name the hand-off artefact [@hassan2025agenticse] **[PP]**.

## 6. Evaluation: what the benchmarks do and do not tell us

### 6.1 Known validity threats

| Threat | Evidence | Class |
|---|---|---|
| **Underspecified issues**: the issue does not determine the expected behaviour | 38.3% of 1,699 sampled SWE-bench tasks flagged for underspecified problem statements | [@chowdhury2024sweverified] **[VC]** |
| **Over-specific or unrelated tests**: valid fixes rejected | 61.1% flagged for tests that may unfairly reject valid solutions; 68.3% filtered overall | [@chowdhury2024sweverified] **[VC]** |
| **Weak tests**: invalid fixes accepted | 31.08% of passed patches (SWE-agent + GPT-4) judged suspicious due to weak tests | [@aleithan2024swebenchplus] **[PP]** |
| **Solution leakage**: the fix is in the issue or comments | 32.67% of successful patches involved leaked solutions; filtering lowered that system's resolve rate from 12.47% to 3.97% | [@aleithan2024swebenchplus] **[PP]** |
| **Memorisation and contamination** | Up to 76% accuracy identifying buggy file paths from issue text alone on SWE-bench Verified, vs. up to 53% on repositories outside SWE-bench | [@liang2025illusion] **[PP]** |
| **Narrow distribution**: Python only, text only | Top systems struggle on 617 visual JavaScript tasks; SWE-agent 12% vs. 6% for the next best | [@yang2025swebenchmm] **[PR]** |
| **Easy-task skew** | Most original SWE-bench tasks estimated at under one hour for an experienced engineer (77.8%) | [@chowdhury2024sweverified] **[VC]** |
| **Scaffold dependence** | GPT-4 on SWE-bench Lite: 2.7% (early RAG scaffold) to 28.3% (CodeR), per OpenAI's reading of the leaderboard | [@chowdhury2024sweverified] **[VC]** |
| **Harness and oracle defects** | Audits find grader defects and configuration-dependent results in agent benchmarks | [@chen2026oracle], [@ding2026reexec] **[PP]** |

Successor benchmarks respond to some of these threats: SWE-bench Verified removes infeasible tasks [@chowdhury2024sweverified] **[VC]**; SWE-Bench Pro uses held-out and commercial repositories and longer tasks [@deng2025swebenchpro] **[PP]**; SWE-Bench Pro Verified in turn reports reward-hacking channels and task-quality issues in SWE-Bench Pro and revises it [@zheng2026sweproverified] **[PP]**. The pattern of benchmark, audit, and revised benchmark is itself a finding. **[OP]** We hypothesise that any fixed public benchmark for ASE has a limited useful lifetime, and that audit methodology should be treated as part of benchmark design.

### 6.2 Beyond resolve rates

- **Time horizons.** Kwa et al. measure the length of tasks (in human time) an agent completes with 50% success. They report that horizons on their 170-task suite doubled roughly every seven months from 2019 to 2025, and they discuss the external-validity limits explicitly [@kwa2025horizon] **[PR]**.
- **Reliability across trials.** τ-bench introduced pass^k, the probability that all *k* independent trials succeed, and found pass^8 below 25% in its retail domain for the agents tested [@yao2024taubench] **[PR]**. Although τ-bench is not an SE benchmark, the metric applies directly to ASE, where a user may need the agent to succeed every time rather than once.
- **Real-world productivity.** In an RCT with 16 experienced developers on 246 tasks in their own mature projects, allowing AI tools (primarily Cursor Pro with Claude 3.5/3.7 Sonnet) increased completion time by 19%, contrary to developers' own forecast and post-hoc estimate [@becker2025uplift] **[PP]**. The study's setting (very experienced developers, large mature projects, early-2025 tools) limits generalisation in both directions.
- **Maintenance cost.** The SWE-Maintain study reports a 5.6-point average drop in later-task resolution when starting from agent-written history rather than developer-written history, rising to 14.0 points when all earlier tests must also pass. The cost disappears when the inherited code passes earlier tests [@pan2026maintain] **[PP]**.

### 6.3 What would a better ASE evaluation report? [OP]

Combining the above, a result should state at least: the benchmark version and split, its known validity issues, model and scaffold versions, budgets, the number of runs and a reliability measure (e.g., pass^k), whether results were re-executed, and whether the agent's output was checked for leakage. This matches the reporting checklist proposed in Chapter 01.

## 7. Human roles in ASE

The literature describes several shifts in what the human does. Most of the evidence is visionary or practitioner-based.

- **From author to specifier and reviewer.** SE 3.0 envisions "intent-centric, conversation-oriented development" with AI teammates [@hassan2026se3] **[PR]**. This is a vision paper; it does not measure outcomes.
- **Orchestrating and mentoring agents.** Hassan et al. propose an Agent Command Environment for humans and an Agent Execution Environment for agents, with structured artefacts flowing between them, including agent-initiated "Consultation Request Packs" [@hassan2025agenticse] **[PP]**.
- **Practitioner workflows** encode the human role as a contract: a goal, a checkable finish condition, permissions, and an escape hatch. They also have the agent produce a decision log for the human to audit afterwards [@tan2026pstack] **[EE]**.
- **Perceived versus measured benefit.** The RCT above shows that developers' beliefs about speed-ups can be wrong in sign [@becker2025uplift] **[PP]**. This is a reason to measure human-agent workflows rather than rely on self-report.

## 8. Safety and security in ASE

Coding agents act on file systems, shells, networks, and credentials. Three October 2026 preprints show the breadth of the concern; all are new and unreviewed:

- **Boundary violations**: SWE-MISBEHAVIOR reports, for open-source agents such as OpenHands and smolagents, high rates of misbehaviour including unintended modification of user inputs (50.5%) and silent compromise of environment integrity (53%) [@trong2026misbehavior] **[PP]**.
- **Cross-session skill attacks**: persistent artefacts written by one skill can steer later sessions; attack success rates of 46.7%–77.4% across tested agent CLIs and models [@liao2026skillrelay] **[PP]**.
- **Protocol-level guidance**: MCP requires that hosts "obtain explicit user consent before invoking any tool" and treats tool annotations as untrusted unless from a trusted server [@mcp2026spec] **[VC]**.

## 9. Open problems specific to ASE

1. **Specification quality.** How much of agent failure is attributable to underspecified tasks rather than agent capability? The SWE-bench Verified annotations suggest a lot, for that benchmark [@chowdhury2024sweverified] **[VC]**.
2. **Verification beyond the test suite.** How can agents discover failures that existing tests do not cover? [@yao2026sweeper] **[PP]**
3. **Hand-off evidence.** What evidence lets a reviewer trust a change quickly and correctly? Almost no controlled studies exist.
4. **Long-horizon and cumulative effects.** Do agent-written changes accumulate debt? Early evidence points to inherited test failures [@pan2026maintain] **[PP]**.
5. **Agentic versus pipeline designs.** When does autonomy pay for its cost and variance [@xia2025agentless] **[PR]**?
6. **Harness maintenance.** Instruction files and skills change agent behaviour, but are they tested? [@giampieri2026cortex] **[PP]**

These are developed with explicit resolution criteria in [agenda/open-questions.md](../agenda/open-questions.md).

## References

Keys cited (all in [`references.bib`](../references.bib)): `hassan2025agenticse`, `hassan2026icse`, `hassan2026se3`, `assalaarachchi2026agenticpm`, `yao2023react`, `schick2023toolformer`, `shinn2023reflexion`, `jimenez2024swebench`, `qian2024chatdev`, `hong2024metagpt`, `zhang2024autocoderover`, `yang2024sweagent`, `xia2025agentless`, `wang2025openhands`, `chowdhury2024sweverified`, `yang2025swebenchmm`, `pan2025swegym`, `aleithan2024swebenchplus`, `kwa2025horizon`, `becker2025uplift`, `liang2025illusion`, `deng2025swebenchpro`, `wang2024codeact`, `anthropic2024effective`, `wu2023autogen`, `chen2026oracle`, `ding2026reexec`, `zheng2026sweproverified`, `yao2024taubench`, `pan2026maintain`, `tan2026pstack`, `trong2026misbehavior`, `liao2026skillrelay`, `mcp2026spec`, `yao2026sweeper`, `giampieri2026cortex`.
