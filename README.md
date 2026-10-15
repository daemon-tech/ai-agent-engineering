# AAE Research Notebook

**AI Agent Engineering (AAE): a living manuscript, technical encyclopedia, literature review, and research notebook.**

> **Status: v0.1, not peer reviewed.** Everything here is a working draft written on 2026-10-14. Claims are labelled by evidence class (see below). Terms, definitions, taxonomies, and hypotheses marked **[OP]** are *our proposals*, not established consensus.

## Scientific mission

Large language model (LLM) agents now edit repositories, run tests, open pull requests, and operate for hours with limited human supervision. The research describing them is spread across machine learning, software engineering, human-computer interaction, and security venues, and much of the practical knowledge lives in vendor blog posts and practitioner tooling that has never been evaluated.

This notebook tries to do three things:

1. **Consolidate** what is actually established about engineering LLM agents, with every source verified against its primary record.
2. **Separate** established findings from preprints, vendor claims, engineering experience, and our own proposals, so a reader always knows how much weight a sentence can bear.
3. **Propose, carefully,** a discipline-level framing, *AI Agent Engineering*, and test whether that framing is useful. We treat AAE as a *proposed emerging discipline*, not an accepted one.

The first domain we study is **Agentic Software Engineering (ASE)**: agents whose task is to build, change, test, and maintain software. We start there because software engineering has unusually good verification signals (compilers, tests, CI), public benchmarks, and an existing research community that already uses the term. ASE is *not* our coinage; see [manuscript/02](manuscript/02-agentic-software-engineering.md) for its prior use.

## What this repository is not

- Not a software framework or SDK.
- Not a collection of prompts, rules files, or "best practices" presented as settled.
- Not a leaderboard. We record benchmark numbers only as reported by their primary source, with their setup.
- Not an endorsement of any vendor or tool. Case studies are case studies.

## Scope

**In scope:** architectures of LLM-based agents (loops, reasoning-and-acting, planning, tool use, memory and context, multi-agent setups); the engineering of the environment around the model (sometimes called the *harness*); verification and evaluation; benchmark validity; human oversight and delegation; security of agent tooling; empirical studies of agents in real software projects.

**Out of scope for v0.1:** model training internals except where they bear directly on agent behaviour; robotics and embodied agents; non-LLM multi-agent systems beyond historical context.

## Evidence classes

Every substantive claim carries one of these tags. Full definitions are in [METHODOLOGY.md](METHODOLOGY.md).

| Tag | Class | Meaning |
|---|---|---|
| **[PR]** | Peer-reviewed | Published at a peer-reviewed venue that we verified (proceedings page, publisher DOI, or journal page). |
| **[PUB]** | Published, review type unverified | In proceedings or a journal (verified DOI/publisher record), but we could not verify that it was peer reviewed (e.g. companion or workshop items). |
| **[PP]** | Preprint | Available on arXiv or similar, with no verified publication. |
| **[VC]** | Vendor claim | Stated by a company about its own product, benchmark, or practice. |
| **[EE]** | Engineering experience | Practitioner reports, tooling, and documentation that describe practice without controlled evaluation. |
| **[OP]** | Our proposal or hypothesis | Terms, definitions, taxonomies, conjectures, and frameworks introduced in this notebook. |

Citations use Pandoc style, e.g. `[@yao2023react]`, and resolve against the single [references.bib](references.bib). The verification record for every entry is in [references-verification.md](references-verification.md).

## License

The text is licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**; see [`LICENSE`](LICENSE). Reuse is permitted with attribution. The repository is public at https://github.com/daemon-tech/ai-agent-engineering.

Third-party material quoted here (short attributed quotations only) remains under its original license. The pstack case study quotes an MIT-licensed project.

## How to cite

Until a versioned release exists, cite as: *0xDaemon et al., "AAE Research Notebook", v0.1.1, 2026-10-15, not peer reviewed.* A `CITATION.cff` is still to be added.
