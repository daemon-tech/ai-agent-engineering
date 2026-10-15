# Changelog

All notable changes to the AAE Research Notebook. Dates are Europe/Berlin.

## [0.1.1], 2026-10-15

### Added
- `LICENSE`: Creative Commons Attribution 4.0 International (CC BY 4.0).
- Repository published at https://github.com/daemon-tech/ai-agent-engineering (public).

### Changed
- New evidence tag **[PUB]** (published, review type unverified), defined in README, METHODOLOGY and CONTRIBUTING and added to the issue/PR templates.
- Venue corrections: AutoGen (`wu2023autogen`) is COLM 2024; tau-bench (`yao2024taubench`) is ICLR 2025. Both now tagged **[PR]** in the manuscript. MemGPT (`packer2023memgpt`) remains a preprint **[PP]**.
- README, CONTRIBUTING and this changelog no longer describe the license as undecided or the repository as unpublished.

### Fixed
- Missing evidence tag on `assalaarachchi2026agenticpm` (Chapter 01, layer L5): now **[PUB]**.
- `wu2023autogen` title corrected to the COLM 2024 title ("...via Multi-Agent Conversations").
- `assalaarachchi2026agenticpm` bib entry: venue AGENT '26 (ACM), pp. 157–164, verified via Crossref.
- `hassan2026icse` bib entry: venue corrected to ICSE-Companion '26 per Crossref; tagged **[PUB]** in Chapters 00 and 02.
- "How to cite" now names v0.1.1.

## [0.1.0], 2026-10-14

### Added
- README with mission, scope, evidence classes, structure, status ("v0.1, not peer reviewed"), and a license *suggestion* (CC BY 4.0 for text; not yet decided).
- METHODOLOGY (sourcing rules, evidence classes, literature process, review process, threats to validity).
- CONTRIBUTING with a proposed weekly literature-scan workflow (text only; human review; no automation).
- Manuscript chapters 00 (introduction), 01 (proposed definition and taxonomy, [OP]), 02 (agentic software engineering), 03 (agent architectures).
- Annotated paper entries: ReAct, SWE-bench, SWE-agent.
- Case study: pstack (engineering experience).
- Frontier review for October 2026, plus a research log.
- Research agenda with 13 open questions.
- Central `references.bib` (52 entries) and `references-verification.md`.
- GLOSSARY, first research note (`notebook/2026-10-14.md`), GitHub issue templates (research question, paper addition) and a pull-request template with a scientific-review checklist.

### Not included, by design
- No LICENSE file (maintainer decision pending; resolved in 0.1.1).
- No GitHub Actions or automated publishing.
- No remote repository; nothing pushed (resolved in 0.1.1).
