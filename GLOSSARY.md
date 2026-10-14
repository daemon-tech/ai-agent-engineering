# Glossary

Status column: **Established** = used with this meaning in the cited literature; **Vendor** = vendor or standards usage; **Practice** = practitioner usage; **[OP]** = our proposal or our sharpening of a term.

| Term | Definition | Status | Source |
|---|---|---|---|
| **Agent (LLM agent)** | A system in which a language model repeatedly selects actions conditioned on a goal and on prior actions and observations, the actions are executed in an environment, and observations are fed back until termination. | Established (functional definitions vary) | [@wang2024survey], [@sumers2024coala]; formalised in Ch. 03 [OP] |
| **Workflow (vs. agent)** | A system where LLMs and tools are orchestrated through predefined code paths, as opposed to agents, where the LLM directs its own process. | Vendor | [@anthropic2024effective] |
| **AI Agent Engineering (AAE)** | The systematic study and practice of designing, building, verifying, evaluating, operating, and governing multi-step AI agent systems so that they are reliably useful, verifiably correct within stated bounds, and safe to delegate to. | **[OP]** | Ch. 01 |
| **Agentic Software Engineering (ASE)** | Software engineering in which agents pursue goal-oriented SE objectives; also SE re-engineered for agents ("SE for Agents"). | Established (recent) | [@hassan2025agenticse], [@hassan2026icse] |
| **SE 3.0** | An AI-native, intent-centric, conversation-oriented vision of software engineering. | Established (vision) | [@hassan2026se3] |
| **Agent-computer interface (ACI)** | The interface (commands, feedback formats, guardrails) through which an LM agent interacts with a computer. | Established | [@yang2024sweagent] |
| **Harness** | The non-model software around an agent: loop, tools and interface, context construction, memory, permissions, sandbox, logging, verification hooks, and instruction files. | **[OP]**, building on emerging usage | [@zhou2026externalization], [@guo2026harness], [@giampieri2026cortex] |
| **Context** | The input the model receives at a step, constructed by the harness from history, memory, and instructions under a token budget. | Established | [@liu2024lost]; notation Ch. 03 [OP] |
| **Done predicate** | An observable, checkable condition whose truth ends the task successfully. | **[OP]** (cf. practitioner "finish condition") | Ch. 03 §1.1; [@tan2026pstack] |
| **Verification** | Establishing that a *particular* output meets its specification. | **[OP]** distinction | Ch. 01 §3.2 |
| **Evaluation** | Estimating how a *configuration* performs across a task distribution. | **[OP]** distinction | Ch. 01 §3.2 |
| **Verification signal** | Any observation bearing on whether output meets the goal (test, type check, reproduction, screenshot, review), characterised by strength and availability. | **[OP]** | Ch. 00 §3.4 |
| **Verification profile** | A domain's typical verification signals with their strength and availability to the agent. | **[OP]** | Ch. 01 §3.3 |
| **Fail-to-pass test** | A test that fails before and passes after the reference fix; the core SWE-bench success criterion, together with tests that must keep passing. | Established | [@jimenez2024swebench] |
| **Resolve rate** | Percentage of benchmark task instances whose generated patch applies and passes the associated tests. | Established | [@jimenez2024swebench] |
| **pass^k** | Probability that all *k* independent trials of a task succeed; a reliability metric. | Established | [@yao2024taubench] |
| **50% time horizon** | The human completion time of tasks that an AI system completes with 50% success. | Established | [@kwa2025horizon] |
| **ReAct** | Prompting pattern interleaving reasoning traces ("thoughts") with environment actions and observations. | Established | [@yao2023react] |
| **Reflexion** | Agents that verbally reflect on feedback after a trial and store the reflection in episodic memory for later trials. | Established | [@shinn2023reflexion] |
| **Code actions (CodeAct)** | Using executable code as the agent's action space. | Established | [@wang2024codeact] |
| **Episodic / semantic / procedural memory** | Memory of past experience / facts / how to act; adapted from cognitive architectures to language agents. | Established | [@sumers2024coala] |
| **Model Context Protocol (MCP)** | An open protocol for exposing tools, resources, and prompts to LLM applications over JSON-RPC. | Vendor / standard | [@mcp2026spec] |
| **Skill** | A reusable package of agent instructions, possibly with code and resources, loaded on demand. | Practice | [@tan2026pstack], [@liao2026skillrelay] |
| **Delegation scope** | How much of a task the agent owns (edit, PR, stack, project). | **[OP]** | Ch. 00 §3.5 |
| **Oversight point** | Where a human checks agent work (each action, irreversible actions, merge, after the fact). | **[OP]** | Ch. 00 §3.5 |
| **Solution leakage** | A benchmark issue text or comments that contain the fix. | Established (recent) | [@aleithan2024swebenchplus] |
| **Boundary violation** | An agent action outside the intended scope (e.g., modifying user inputs, compromising the environment). | Established (recent) | [@trong2026misbehavior] |
