# Knowledge graph (v0, initial)

Flat graph of the notebook, built from `manuscript/`, `references.bib` and `references-verification.md`.

Source commit of main: `436ec449d6187993e8e887f14816eba3cfe2f5bf`

Rebuild from the repo root with `python3 graph/build.py`. The output is deterministic.

Files:

* `nodes.csv`: columns id, type, label, evidence_class, source. Types are `paper` (one per bib key, class PR/PUB/PP/VC/EE and primary record taken from `references-verification.md`), `chapter` (one per manuscript file), `concept` (one per level 2 section, id prefixed with the chapter) and `open_question` (one per [OP] statement; source is its issue if one exists, else file:line).
* `edges.csv`: columns source, relation, target, citation. Relations are `contains` (chapter to concept), `cites` (concept or chapter to paper) and `raises` (concept or chapter to open question). The citation is the file:line where the link appears.
* `tag-flags.csv`: inline evidence tags that a heuristic matched to a different class than the verified one. Most are tags belonging to an adjacent citation; hand_check says which were checked.
* `coverage.md`: citations per chapter and the share that are PR or PUB.

Only links present in the repo files are included; nothing is inferred. Following the editor's rule, [OP] items are open questions, not claims.
