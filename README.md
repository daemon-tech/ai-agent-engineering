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
| **[PP]** | Preprint | Available on arXiv or similar, with no verified peer-reviewed publication. |
| **[VC]** | Vendor claim | Stated by a company about its own product, benchmark, or practice. |
| **[EE]** | Engineering experience | Practitioner reports, tooling, and documentation that describe practice without controlled evaluation. |
| **[OP]** | Our proposal or hypothesis | Terms, definitions, taxonomies, conjectures, and frameworks introduced in this notebook. |

Citations use Pandoc style, e.g. `[@yao2023react]`, and resolve against the single [references.bib](references.bib). The verification record for every entry is in [references-verification.md](references-verification.md).

## Structure

```
.
├── README.md                     you are here
├── METHODOLOGY.md                sourcing rules, evidence classes, review process
├── CONTRIBUTING.md               how to propose questions, papers, and changes
├── GLOSSARY.md                   terms, with established vs. proposed status
├── CHANGELOG.md
├── references.bib                the only bibliography
├── references-verification.md   how and when each entry was verified
├── manuscript/
│   ├── 00-introduction.md        academically structured introduction
│   ├── 01-definition-taxonomy.md proposed definition and taxonomy of AAE [OP]
│   ├── 02-agentic-software-engineering.md
│   └── 03-agent-architectures.md technical chapter
├── papers/                       annotated entries for individual works
├── case-studies/                 engineering-experience case studies
├── frontier/                     dated frontier reviews and the research log
├── agenda/open-questions.md      the research agenda
└── notebook/                     dated research notes
```

Suggested reading order: `00-introduction` → `01-definition-taxonomy` → `02-agentic-software-engineering` → `03-agent-architectures`, then `papers/`, `case-studies/`, and `agenda/`.

## Status

| Item | State |
|---|---|
| Version | v0.1 (2026-10-14) |
| Peer review | **None.** No external reviewer has read this material. |
| Citations | 52 BibTeX entries, each verified against a primary source on 2026-10-14 |
| Known gaps | See "Not yet verified" in [references-verification.md](references-verification.md) and the open questions in [agenda/](agenda/open-questions.md) |

## License (suggestion, not yet decided)

We **suggest** licensing the text under **Creative Commons Attribution 4.0 International (CC BY 4.0)**, which allows reuse with attribution and suits a scientific manuscript. Any code snippets could additionally be placed under a permissive software license such as MIT. **No LICENSE file is included yet; the maintainer (0xDaemon) has to decide.** Until a license is added, default copyright applies.

Third-party material quoted here (short attributed quotations only) remains under its original license. The pstack case study quotes an MIT-licensed project.

## How to cite

Until a versioned release exists, cite as: *0xDaemon et al., "AAE Research Notebook", v0.1, 2026-10-14, not peer reviewed.* A `CITATION.cff` should be added once the repository is public and the license is chosen.
