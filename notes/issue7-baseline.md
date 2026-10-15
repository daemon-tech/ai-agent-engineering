# Issue #7: Runde-0-Baseline zur Claim-Qualität (AAE-Bot-Team)
Stand: 2026-10-15 04:50 (Europe/Berlin), Repo daemon-tech/ai-agent-engineering, HEAD 436ec44, read-only geklont.
Seed: **20261015** (Python `random.seed`, `random.sample(..., 40)` über alle Claims mit Zitation). Skript: [issue7-extract.py](issue7-extract.py) (vom Repo-Root ausführen). CSV: [issue7-baseline.csv](issue7-baseline.csv)

## Grundgesamtheit
- Gescannt: `manuscript/*.md` und `notes/2026-10-frontier-review.md`. Ein Verzeichnis `frontier/` gibt es nicht, der Frontier-Review liegt seit d44496c unter notes/.
- 201 Sätze bzw. Tabellenzellen mit Zitation oder Tag; 186 mit Zitation.
- Zitationen ohne Inline-Tag: 15 Treffer. Davon sind 12 Quellenzeilen im Frontier-Review, deren Tag in der Nachbarzeile "Class" steht, und 3 tragen **[PUB]**, die sechste Klasse aus METHODOLOGY.md:20 (fehlte im Regex). **Echte Untagged in der Grundgesamtheit: 0.**

## Metriken (Stichprobe n=40)
| Metrik | Wert |
|---|---|
| % untagged | 0 % (0/40) |
| % falscher Tag (Venue in references.bib und Primärquelle vs. Tag) | 0 % (0/40) |
| % nicht gestützt ("nein") | 0 % (0/40) |
| % nur teilweise gestützt | 10 % (4/40) |
| % nicht verifizierbar | 2,5 % (1/40) |
| Defekte gesamt (teilweise + nein) | 10 % (4/40), 95%-KI nach Wilson ca. 4–23 % |
| Median-Überlebenszeit defekter Claims | **nicht schätzbar, alle 4 zensiert**: eingeführt in 6366a3f (2026-10-14 16:19), bis HEAD (2026-10-15 04:32) nicht korrigiert, also ≥ 12,2 h |

Methodische Hinweise:
- Alle Commits des 14.10. tragen denselben Zeitstempel 16:19:25 (Bulk-Import). Das Einführungsdatum ist also das Importdatum, nicht der Zeitpunkt des Schreibens.
- 2 der 40 Zeilen wurden später editiert (a819ed4, Tag-Cleanup). Darunter ist der defekte Claim #15, dessen Defekt dabei nicht behoben wurde.
- "Gestützt" wurde gegen Abstracts geprüft (arXiv, abgerufen 2026-10-15), bei konkreten Zahlen und Zitaten gegen den Volltext (ReAct, Kwa, SWE-agent, Anthropic-Seite, pstack @1e5c90a).
- Der OpenAI-Blog zu Verified liefert per curl 403 und konnte nicht direkt geprüft werden.
- Wooldridge 1995 wurde nicht geöffnet (Paywall).

## Die 5 schwächsten Claims
1. manuscript/02-agentic-software-engineering.md:134: "The SWE-bench Verified annotations suggest a lot". Vage, keine Zahl, Primärquelle (Blog) nicht direkt abrufbar. Fix: "38,3 % flagged underspecified" einsetzen.
2. manuscript/03-agent-architectures.md:284: "pass^k-style metrics … are rarely used in ASE papers". Die Zitation (tau-bench) belegt nur die Metrik, nicht die Seltenheit in der ASE-Literatur. Fix: als [OP] markieren oder Zählung belegen. Wurde in a819ed4 editiert, der Defekt blieb.
3. manuscript/01-definition-taxonomy.md:78: Governance "permissions, security, auditability, and accountability". Die Quellen (SkillRelay, SWE-MISBEHAVIOR) decken nur Security und Grenzverletzungen ab.
4. manuscript/01-definition-taxonomy.md:88: "tests can be weak or over-specific" mit Verweis auf SWE-Bench+. "over-specific" stammt aus OpenAI Verified und fehlt in der zitierten Quelle.
5. manuscript/01-definition-taxonomy.md:30: Wooldridge 1995 als "ancestor". Plausibel, aber in dieser Runde nicht verifiziert (Paywall).

## Befund für Hypothese #2 (Novel Directions)
Die Baseline ist niedrig: keine falschen Tags, keine ungestützten Claims. Die Defekte sind Überdehnungen, also Aussagen, die über das hinausgehen, was die Quelle trägt. Sie sitzen alle in Synthese- und Übersichtssätzen, nicht in referierten Zahlen. Die Messung lohnt sich deshalb vor allem für **Überdehnung**. Die Überlebenszeit wird erst nach weiteren Runden schätzbar.
