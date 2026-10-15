# Methodology

This document describes how sources enter the notebook, how claims are labelled, how changes are reviewed, and how to contribute (§7). It applies to every file in the repository.

## 1. Sourcing rules

1. **Primary sources only for bibliographic facts.** Titles, authors, dates, venues, DOIs, and numbers are taken from the primary record: the arXiv abstract page or arXiv API, the publisher's DOI record (resolved via Crossref), the official proceedings page (NeurIPS, ICLR, PMLR, ACL Anthology), OpenReview, or a vendor's own page for vendor claims. Secondary aggregators (Google Scholar, Semantic Scholar, blogs, search-engine summaries) may be used to *find* a source, never to *fill* a field.
2. **No invented references.** If we cannot open the primary record, the work is not cited. It goes to the "Not yet verified" list in `references-verification.md` instead.
3. **Venue acceptance is checked, not assumed.** An arXiv comment such as "accepted at X" is an author statement. We record a work as peer-reviewed only after finding it on the venue's own proceedings page or publisher record. Where we could only see the author statement, the work stays a preprint.
4. **Versions matter.** arXiv papers change between versions. We record the version we read when a number depends on it (for example, `2405.15793v3`).
5. **Numbers are quoted with their setup.** A benchmark number is meaningless without the split, model, scaffold, budget, and date. We quote numbers only from the primary source and always give at least the split and model.
6. **Brief quotations only.** Quotations are short, in quotation marks, and attributed. We paraphrase otherwise.
7. **Dates are checked.** Frontier entries record both the publication date (from the primary record) and the review date. We never call a work "the latest" or "state of the art" without a dated check, and even then we prefer "most recent we found as of <date>".

## 2. Evidence classes

| Tag | Class | Inclusion criterion | How to read it |
|---|---|---|---|
| **[PR]** | Peer-reviewed | Listed on a verified peer-reviewed venue's proceedings or publisher record. | Has passed a review process. It is still not necessarily replicated or correct. |
| **[PUB]** | Published, review type unverified | Verified publisher record (DOI) in proceedings or a journal, but track or review process not verified. | Formally published, but not evidence of a reviewed empirical result. |
| **[PP]** | Preprint | Public manuscript without verified publication. | Has not been reviewed. Treat findings as provisional. |
| **[VC]** | Vendor claim | A company describing its own product, benchmark, or internal practice. | May be accurate, but the incentive to present results favourably is structural. Usually not independently reproducible. |
| **[EE]** | Engineering experience | Practitioner tooling, documentation, talks, or reports without controlled evaluation. | Valuable for hypotheses and practice. It is not evidence of effect size or generality. |
| **[OP]** | Our proposal or hypothesis | Introduced in this notebook. | A conjecture to be tested. Never a finding. |

Two edge cases appear in v0.1:

- **Published, review type unverified.** Two items appear in ACM proceedings (a two-page item in the ICSE-Companion '26 proceedings, pp. 22–23 and a paper in the proceedings of the 2026 International Workshop on Agentic Engineering, AGENT '26, pp. 157–164) where we verified the DOI and proceedings but not the track or review process. BibTeX marks them `published-review-type-unverified`; the text tags them **[PUB]** (since v0.1.1).
- **Same work, different records.** When a preprint and a peer-reviewed version differ in title or authors (e.g., Agentless, Hassan et al.'s ASE roadmap), we cite the version we actually read and say so.

### Evidence grading within a source

The class is a property of the *source*. Inside a peer-reviewed paper, we still distinguish:

- the **measured result** (e.g., a resolve rate on a stated split),
- the **authors' interpretation** of that result, and
- **our extrapolation** to AAE, which is always tagged **[OP]**.

## 3. Literature process

1. **Seed set.** Foundational agent papers and the core ASE systems and benchmarks (see `references.bib`).
2. **Forward and backward search** from the seed set, guided by explicit questions in `notes/open-questions.md`.
3. **Frontier scan.** A dated review of recent arXiv submissions (for v0.1: arXiv API query `cat:cs.SE AND (abs:agent OR abs:agents)`, sorted by submission date, run on 2026-10-14), plus checks of standards and benchmark pages. Every scan is logged in `notes/research-log.md` with the query, date, and what was kept or discarded and why.
4. **Annotation.** Works central to an argument get an entry in `papers/` using the fixed template (question, method, findings, setup, limitations, novelty, connections, open questions, implications).
5. **Integration.** Findings are folded into the manuscript only with their evidence tag.

We do not claim systematic-review completeness. v0.1 is a structured narrative review; a protocol for a systematic mapping study is listed as future work.

## 4. Review process

All substantive changes go through a pull request with the scientific-review checklist (`.github/PULL_REQUEST_TEMPLATE.md`). "Substantive" means any change that adds or alters a claim, a number, a citation, a definition, or an evidence tag.

1. **Author self-check:** every new citation key exists in `references.bib` and has a row in `references-verification.md`; every number has a source and setup; every proposal is tagged **[OP]**. Every claim carries one of [PR], [PUB], [PP], [VC], [EE], [OP]; never present a preprint or a [PUB] item as peer-reviewed (check the venue's own listing).
2. **Scientific review:** at least one reviewer other than the author re-opens each new primary source and checks the claim against it. Reviewers record what they checked in the PR.
3. **Disagreement:** if reviewers disagree on an evidence class or interpretation, the text states both positions or is downgraded to the weaker claim.
4. **Merging:** only after the checklist is complete and the reviewer approves. Typos and formatting can merge with lighter review.
5. **Corrections:** errors are fixed in a new commit, never by rewriting history, and recorded in `CHANGELOG.md`.

## 5. Use of AI assistance

This notebook was drafted with the help of an AI agent operating under the rules above, then is to be reviewed by humans. That is relevant to the subject matter: an agent writing about agents can reproduce the failure modes it describes, such as confident but unsupported claims. AI-assisted drafts therefore get the same verification as any other contribution, and the review checklist explicitly asks whether each claim was checked against the primary source by a human.

## 6. Threats to validity of this notebook

- **Selection bias:** the seed set is centred on English-language, mostly US and Chinese, ML and SE venues.
- **Recency bias:** the frontier review samples one week of arXiv submissions.
- **Verification limits:** OpenReview blocked automated access on 2026-10-14, so ICLR acceptance was verified via the ICLR proceedings and ICLR virtual-conference pages instead.
- **Author position:** the maintainers practise agentic software engineering, which can bias toward optimistic readings. Negative and null results are therefore actively sought (e.g., [@becker2025uplift], [@xia2025agentless]).

## 7. Contributing

This is a scientific manuscript, so the bar for changing *claims* is higher than the bar for changing *prose*. Substantive changes follow the sourcing rules (§1), evidence classes (§2), and review process (§4) above; typo fixes, formatting, and link repairs can be merged after a light review.

### Where things go

| You want to… | Use |
|---|---|
| Ask a research question, or propose one for the agenda | An **issue** with the [research question template](.github/ISSUE_TEMPLATE/research-question.md) |
| Suggest a paper for annotation or citation | An **issue** with the [paper addition template](.github/ISSUE_TEMPLATE/paper-addition.md) |
| Challenge a claim, number, citation, or evidence tag | An **issue** first (cite the primary source), then a PR |
| Change any text, add a paper entry, or add a reference | A **pull request** using the [PR template](.github/PULL_REQUEST_TEMPLATE.md) |

Discussion belongs in issues. Changes belong in pull requests.

### Writing style

- English, Markdown, one topic per section, no empty headings.
- Prefer "most recent we found as of YYYY-MM-DD" over "latest" or "state of the art".
- Prefer plain statements of what a source measured over adjectives.
- Report negative and null results with the same care as positive ones.

### Proposed weekly literature-scan workflow (manual, human-reviewed)

This is a **proposal for a human process**. It is *not* an automated pipeline, and nothing is published automatically. We deliberately do not ship a GitHub Action.

1. **Monday: scan.** A designated scanner runs the logged queries (initially the arXiv API query in `notes/research-log.md`, R2, plus checks of the SWE-bench family pages and the MCP specification) and records the date, query, and number of results in a new research-log entry.
2. **Triage.** For each candidate, the scanner records keep, defer, or exclude, with a one-line reason, in the log. Inclusion criteria are those in the log entry R2.
3. **Verify.** For each kept item, the scanner verifies metadata against the primary record and checks for any venue acceptance.
4. **Draft.** Kept items are drafted as frontier entries (publication date, review date, what changed, mechanism, independently verified?, why it matters, limits) on a branch.
5. **Review.** A second person reviews the PR with the scientific-review checklist. Disagreements on evidence class default to the weaker class.
6. **Merge and log.** After approval, merge and add a CHANGELOG line. Items that later gain peer review or replication are updated in place, with the change recorded.

If automation is ever added (for example, a script that only *collects* candidate lists), its output must still go through steps 2–6 by a human, and it must never commit, push, or publish on its own.

### AI assistance in contributions

AI-assisted contributions are welcome and must be disclosed in the PR. They are held to the same verification standard: a human must have opened each cited primary source.

### Code of conduct

Be precise, be kind, and attack claims rather than people. A formal code of conduct is still to be adopted.
