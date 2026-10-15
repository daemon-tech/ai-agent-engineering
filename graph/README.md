# Knowledge graph (v0, initial)

Flat graph of the notebook, built from `manuscript/`, `references.bib` and `references-verification.md`.

The graph is built from the sources in the same commit that contains it. The build is byte reproducible: rerunning `python3 graph/build.py` leaves graph/ unchanged.

Rebuild from the repo root with `python3 graph/build.py`. The output is deterministic.

Files:

* `nodes.csv`: columns id, type, label, evidence_class, source. Types are `paper` (one per bib key, class PR/PUB/PP/VC/EE and primary record taken from `references-verification.md`), `chapter` (one per manuscript file), `concept` (one per level 2 section, id prefixed with the chapter) and `open_question` (one per [OP] proposal or hypothesis; source is its issue if one exists, else file:line).
* `edges.csv`: columns source, relation, target, citation. Relations are `contains` (chapter to concept), `cites` (concept or chapter to paper) and `raises` (concept or chapter to proposal). The citation is the file:line where the link appears.
* `tag-flags.csv`: citations whose tag directly after `[@key]` is missing or differs from the verified class, using the same rule as `scripts/check_citations.py`. Expected to be empty.
* `coverage.md`: citations per chapter, the share that are PR or PUB, and papers that are not cited.

Only links present in the repo files are included; nothing is inferred. [OP] proposals are not claims about the literature and are kept as separate `open_question` nodes; see [METHODOLOGY.md, Claims and proposals](../METHODOLOGY.md#claims-and-proposals).
