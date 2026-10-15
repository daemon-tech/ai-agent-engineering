# Knowledge graph (v0, initial)

Flat graph of the notebook built from `manuscript/`, `references.bib` and `references-verification.md`.

- `nodes.csv` — `id,type,label,evidence_class,source`. Types: `paper` (one per bib key; class [PR]/[PUB]/[PP]/[VC]/[EE] from `references-verification.md`, source = primary record), `chapter` (one per manuscript file), `concept` (one per `##` section).
- `edges.csv` — `source,relation,target,citation`. Relations: `contains` (chapter → concept), `cites` (concept/chapter → paper). `citation` is the `file:line` where the link appears.

Only links present in the repo files are included; nothing is inferred. [OP] items are not nodes yet.
