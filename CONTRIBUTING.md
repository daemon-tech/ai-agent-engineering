# Contributing

Thank you for helping build the AAE Research Notebook. This is a scientific manuscript, so the bar for changing *claims* is higher than the bar for changing *prose*.

## Where things go

| You want to… | Use |
|---|---|
| Ask a research question, or propose one for the agenda | An **issue** with the [research question template](.github/ISSUE_TEMPLATE/research-question.md) |
| Suggest a paper for annotation or citation | An **issue** with the [paper addition template](.github/ISSUE_TEMPLATE/paper-addition.md) |
| Challenge a claim, number, citation, or evidence tag | An **issue** first (cite the primary source), then a PR |
| Change any text, add a paper entry, or add a reference | A **pull request** using the [PR template](.github/PULL_REQUEST_TEMPLATE.md) |

Discussion belongs in issues. Changes belong in pull requests.

## Rules for substantive changes

A change is *substantive* if it adds or alters a claim, a number, a citation, a definition, a taxonomy element, or an evidence tag. Substantive changes:

1. **Must cite primary sources.** Use the arXiv abstract page or API, publisher DOI, official proceedings page, ACL Anthology, OpenReview, or the vendor's own page. Never cite from memory, search snippets, or aggregators.
2. **Must add or update `references.bib` and `references-verification.md`.** Every new key needs a verification row saying how and when it was checked.
3. **Must tag evidence.** Use [PR], [PP], [VC], [EE], or [OP] (see [METHODOLOGY.md](METHODOLOGY.md)). Never present a preprint as peer-reviewed; check the venue's own listing.
4. **Must quote numbers with setup**: benchmark, split, model, and where possible budget and date.
5. **Must keep proposals separate.** New terms, frameworks, or hypotheses are tagged [OP] and placed where readers expect proposals.
6. **Must keep quotations brief and attributed.**
7. **Require scientific review before merging.** At least one reviewer other than the author re-opens each new primary source and confirms the claim, recording what they checked in the PR conversation.

Typo fixes, formatting, and link repairs can be merged after a light review.

## Writing style

- English, Markdown, one topic per section, no empty headings.
- Prefer "most recent we found as of YYYY-MM-DD" over "latest" or "state of the art".
- Prefer plain statements of what a source measured over adjectives.
- Report negative and null results with the same care as positive ones.

## Proposed weekly literature-scan workflow (manual, human-reviewed)

This is a **proposal for a human process**. It is *not* an automated pipeline, and nothing is published automatically. We deliberately do not ship a GitHub Action.

1. **Monday: scan.** A designated scanner runs the logged queries (initially the arXiv API query in `frontier/research-log.md`, R2, plus checks of the SWE-bench family pages and the MCP specification) and records the date, query, and number of results in a new research-log entry.
2. **Triage.** For each candidate, the scanner records keep, defer, or exclude, with a one-line reason, in the log. Inclusion criteria are those in the log entry R2.
3. **Verify.** For each kept item, the scanner verifies metadata against the primary record and checks for any venue acceptance.
4. **Draft.** Kept items are drafted as frontier entries (publication date, review date, what changed, mechanism, independently verified?, why it matters, limits) on a branch.
5. **Review.** A second person reviews the PR with the scientific-review checklist. Disagreements on evidence class default to the weaker class.
6. **Merge and log.** After approval, merge and add a CHANGELOG line. Items that later gain peer review or replication are updated in place, with the change recorded.

If automation is ever added (for example, a script that only *collects* candidate lists), its output must still go through steps 2–6 by a human, and it must never commit, push, or publish on its own.

## Use of AI assistance

AI-assisted contributions are welcome and must be disclosed in the PR. They are held to the same verification standard: a human must have opened each cited primary source.

## Code of conduct

Be precise, be kind, and attack claims rather than people. A formal code of conduct is still to be adopted.
