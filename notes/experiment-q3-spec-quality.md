# [OP] Experiment Q3: Spec-Qualität und Agent-Erfolg auf SWE-bench Verified

Refs #2 (closes nothing). Status: **[OP]** preregistration draft, 2026-10-15. Design by Technical Scholar; source checks below.

## 1. Wie SWE-bench Verified unterspezifizierte Tasks gefiltert hat

Quelle: OpenAI, "Introducing SWE-bench Verified", 13.08.2024 (aktualisiert 24.02.2025), https://openai.com/index/introducing-swe-bench-verified/ (Volltext gelesen, inkl. eingebetteter Rubrik)

- **Annotatoren:** "We worked with 93 software developers experienced in Python to manually screen SWE-bench samples for quality. We annotated 1,699 random samples from the SWE-bench test set".
- **Onboarding:** "Our team of engineers first hand-labeled 50 samples to a high degree of confidence for use in annotator onboarding tests." Wer mitmachen wollte, musste diese Tests bestehen. Die Annotatoren waren "not necessarily prior experts in the codebases", bekamen aber Zeit zur Einarbeitung.
- **Zwei Kriterien:** (a) ob die Issue-Beschreibung "underspecified and hence unfair to be testing on" ist, (b) ob die `FAIL_TO_PASS`-Tests valide Lösungen aussortieren. Dazu kam ein Freitextfeld für andere schwere Probleme (z. B. Tests, die sich leicht austricksen lassen).
- **Skala:** "Each annotation criterion has a label ranging [0, 1, 2, 3] in increasing severity. Labels 0 and 1 are minor; labels 2 and 3 are severe".
  - Unterspezifikation:
    - 0 "The issue is well-specified and it is clear what is required for a successful solution."
    - 1 "There are some blanks to fill in about the issue, but there is a sensible interpretation of what is required for a successful solution."
    - 2 "The issue is vague and there is room for ambiguity. It is unclear what a successful solution would look like."
    - 3 "It is almost impossible to understand what you are being asked to do without further information."
  - Test-Validität:
    - 0 "The tests perfectly cover all possible solutions."
    - 1 "The tests cover the majority of correct solutions, however some unusual solutions may be missed."
    - 2 "The tests work but some perfectly reasonable solutions may be missed by the tests."
    - 3 "The tests are too narrow/broad or they look for something different than what the issue is about."
- **Redundanz/Ensembling:** "each sample is labeled 3 times by separate annotators ... we conservatively ensemble annotations by taking the highest-severity label amongst the 3 annotators."
- **Schwellenregel:** "we filter out any sample ... where either the problem statement or the `FAIL_TO_PASS` unit tests have an ensemble label of 2 or above in severity. We also filter out all samples that have other major issues flagged." Das heißt: Ein einzelner Annotator von dreien reicht für den Ausschluss. OpenAI nennt das selbst "a higher false-positive rate in removing samples".
- **Zahlen [VC]:** "38.3% of samples were flagged for underspecified problem statements, and 61.1% were flagged for unit tests that may unfairly mark valid solutions as incorrect. Overall ... 68.3% of SWE-bench samples being filtered out". Von 1.699 bleiben rechnerisch also etwa 539 Kandidaten. Diese ~539 sind meine Hochrechnung, keine Angabe von OpenAI.
- **Weg zu 500:** "We include as many samples with difficulty 1-4 hours and >4 hours as possible, and then we randomly sample the remainder to arrive at the 500 samples".
- **Schwierigkeits-Buckets** (Zusatzinfo, "not used for dataset filtering"):
  - Die vier Stufen sind "<15 min fix", "15 min–1 hour", "1–4 hours" und ">4 hours".
  - Zusammengeführt wird per Mehrheit, ohne Mehrheit per Median.
  - In Verified stammen "196 <15-minute fix tasks" (easy) und "45 >1-hour tasks" (hard). Der Rest von 500 − 196 − 45 = 259 liegt im Bucket 15 min–1 h (abgeleitet).
  - Im Original sind "77.8%" der Tasks unter 1 h, in Verified sind "fewer than 10%" über 1 h.
- **Effekt laut OpenAI:**
  - GPT-4o (bester Scaffold, Agentless) kommt auf 33,2 % auf Verified gegenüber 16 % auf dem vollen SWE-bench.
  - "performance increases within individual difficulty categories", also nicht nur durch leichtere Aufgaben erklärbar.
  - Einschränkung: "We ran a single seed".
- Fallbeispiel `scikit-learn__scikit-learn-14520`: Der Test verlangt eine exakte DeprecationWarning-Nachricht, die nur in der PR-Diskussion stand. Die Spec macht den Task "nearly impossible".
- **Daten:** Datensatz, alle Annotationen und Rubrik sind über die Links im Post verfügbar (HF `princeton-nlp/SWE-bench_Verified`). Die Annotations-CSV habe ich nicht geöffnet, ihre Spaltennamen sind also noch offen. Der Post selbst ist vollständig verifiziert (Volltext per WebFetch, 15.10.2026). Der curl-403 in lit_issue2_3.md war nur eine Bot-Sperre.

## 2. Quantitative Belege: Spec-Qualität beeinflusst den Erfolg

1. **OpenAI Verified** (Link oben): Fallen schlecht spezifizierte und unfair getestete Tasks heraus, steigt GPT-4o von 16 % auf 33,2 %, auch innerhalb der Schwierigkeits-Buckets. Unterspezifikation und Testqualität sind dabei vermischt, der Effekt ist korrelativ.
2. **SWE-Bench+** (Aleithan et al., https://arxiv.org/abs/2410.06992):
   - Spec-*Überinformation* in Form von "solution leakage": Von 251 erfolgreichen Patches von SWE-Agent+GPT-4 fallen 82 (32,67 %) darunter, 31,08 % beruhen auf schwachen Tests.
   - Die Resolve-Rate fällt von 12,47 % auf 3,97 % (nach Filter). Zählt man nur korrekte Fixes, sind es 5,49 % (Abschnitt 2.2).
   - Auf **Verified** haben 37 Instanzen Lösungs-Leaks. Von 112 gelösten Tasks (22,4 %) sind 55,36 % verdächtig, die Rate fällt dann auf 10,0 %.
   - Auf SWE-bench+ (Issues nach dem Cutoff, ohne Leaks) erreicht SWE-Agent+GPT-4 noch 0,55 %, AutoCodeRover+GPT-4o 3,83 % (statt 18,83 % auf dem Leaderboard).
   - Fazit: Hinweise in der Spec treiben scheinbaren Erfolg stark.
3. **Ambig-SWE** (Vijayvargiya, Zhou, Yerukola, Sap, Neubig; **[PP]**, ICLR 2026 nur selbst angegeben; https://arxiv.org/abs/2502.13069):
   - Ist eine unterspezifizierte Variante von Verified mit einem simulierten User, der die volle Spec kennt.
   - Interaktion verbessert die Leistung bei unterspezifizierten Inputs um "up to 74% over the non-interactive settings" (arXiv 2502.13069v3, Abstract S. 1, Einleitung S. 2): Je Modell sehr unterschiedlich. Ein deutlicher Abstand zu voll spezifizierten Issues bleibt.
   - Unterspezifikation erkennen: Nur Claude Sonnet 4 (89 %) und Claude Sonnet 3.5 (84 %) erreichen nennenswerte Genauigkeit.
   - Dateipfade als Hinweis helfen vor allem schwächeren Modellen. Qwen 3 Coder wird damit sogar schlechter.
   - Das passt zur Hypothese "Effekt größer für schwächere Harnesses", allerdings nur qualitativ.
   - **Verifiziert: Resolve-Raten aus Figure 3** (Volltext-PDF v3, https://arxiv.org/pdf/2502.13069v3, S. 5). Die Werte habe ich aus dem Balkendiagramm abgelesen. Eine Tabelle mit diesen Zahlen gibt es im Paper nicht.

     | Modell | Hidden | Interaction | Full |
     |---|---|---|---|
     | Llama 3.1 70B | 3,2 | 4,8 | 8,8 |
     | Deepseek-v2 | 5,6 | 7,2 | 12,2 |
     | Claude Haiku 3.5 | 15,4 | 26,8 | 33,8 |
     | Claude Sonnet 3.5 | 24,2 | 39,6 | 49,4 |
     | Qwen 3 Coder | 45,6 | 53,8 | 64,6 |
     | Claude Sonnet 4 | 40,0* | 61,4 | 68,0 |

     \* Fußnote 4: Sonnet 4 lief im Hidden-Setting nur auf "a subset of 100/500 instances". Sonnet 4 und Qwen 3 Coder hatten bis zu 100 Turns, die übrigen Modelle 30.
   - Statistik im Paper: Wilcoxon signed-rank (α = 0,05). Hidden vs. Interaction und Interaction vs. Full sind laut Text "significant for all evaluated models" (Table 4).
   - Anteil der Full-Leistung, der durch Interaktion zurückgewonnen wird: Sonnet 3.5 und Haiku "up to 80%", Deepseek 59 %, Llama 3.1 54 %, Sonnet 4 89 %.
   - Inkonsistenz im Paper: Abschnitt 5 nennt "46% vs 41.8%" für Qwen 3 Coder und Sonnet 4 und verweist dabei auf Figure 3. Diese Werte passen nicht zu den Balken. Für Figure 3 als Quelle zitieren und den Widerspruch vermerken.
4. **Original SWE-bench** (Jimenez et al., ICLR 2024, Volltext v3 https://arxiv.org/pdf/2310.06770v3), **verifiziert:**
   - "Using a BM25 retriever, Claude 2 is only able to resolve 1.96% of the issues."
   - Table 5 (BM25, volles SWE-bench): Claude 3 Opus 3,79 %, Claude 2 1,97 %, GPT-4-turbo 1,31 %, ChatGPT-3.5 0,17 %.
   - Mit Lokalisierungsinformation im Oracle-Setting (die vom Gold-Patch editierten Dateien) steigt Claude 2 auf 4,8 %. Wörtlich: "Claude 2 scores at 2.2% compared to 4.8% in the main table for 'oracle' retrieval". Die 2,2 % beziehen sich auf eine Teilmengen-Analyse.
   - Das ist ein frühes Indiz dafür, dass Scope-Information (D3) wirkt. Es ist allerdings Kontext-Retrieval, keine Spec-Umformulierung.
5. **ClarifyGPT** (arXiv 2310.10996): weiterhin **nicht geprüft**, außerhalb des Scopes dieses Follow-ups.
6. **OpenAI, "Why we no longer evaluate SWE-bench Verified"**, 23.02.2026, https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/, **verifiziert** (Volltext per Fetch):
   - Audit von 138 Verified-Problemen, die o3 "did not consistently solve over 64 independent runs". Jedes wurde von mindestens sechs Engineers geprüft.
   - "59.4% of the 138 problems contained material issues in test design and/or problem description". Davon 35,5 % narrow tests, 18,8 % wide tests (Tests prüfen nicht spezifizierte Zusatzfunktionalität), 5,1 % Sonstiges.
   - Beispiele: `pylint-dev__pylint-4551` (Test importiert `get_annotation`, das in der Issue nicht genannt ist) und `sympy__sympy-18199` (Beschreibung deckt nur 1 von 3 Issues ab).
   - Contamination: "all frontier models we tested were able to reproduce the original, human-written bug fix ... or verbatim problem statement specifics for certain tasks".
   - "models that have seen the problems during training are more likely to succeed, because they have additional information needed to pass the underspecified tests."
   - Zahlen zu dieser Erfolgssteigerung nennt OpenAI nicht. Einzelfall: GPT-5.2 löste 31 als "almost impossible" eingestufte Tasks.
   - SOTA auf Verified: 74,9 % → 80,9 % in 6 Monaten. OpenAI empfiehlt SWE-bench Pro.
   - **Konsequenz für Q3:** Den Effekt von S1 vs. S0 kann Memorization verdecken. Eine Contamination-Probe und ein Post-Cutoff- bzw. Pro-Kontrollset werden damit Pflicht.
7. **UTBoost** (Yu, Zhu, He, Kang; ACL 2025, S. 3762–3774; https://aclanthology.org/2025.acl-long.189/, arXiv 2506.09289), **verifiziert** (Abstract und Anthology-Metadaten, Volltextausschnitt):
   - "we identified 36 task instances with insufficient test cases and uncovered 345 erroneous patches incorrectly labeled as passed".
   - Die Korrekturen betreffen "40.9% of SWE-Bench Lite and 24.4% of SWE-Bench Verified leaderboard entries", mit 18 bzw. 11 Rangänderungen (Verified: 11/45 Einträge).
   - Der Wert "26/500 Verified-Tasks mit unzureichenden Tests" aus lit_issue2_3.md stammt aus einem nur bruchstückhaften Snippet ("26/5..."). Ohne vollständige Volltext-Zeile ist er **nicht sicher bestätigt**.
   - Korrektur zu lit_issue2_3.md: Die Autoren sind Boxi Yu et al., nicht "Boshi Wang". Zitiert werden sollte die ACL-Version, nicht der Substack-Blog.
   - **Konsequenz für Q3:** Die False-success-Messung sollte UTBoost-augmentierte Tests (HF-Datensatz) als zweiten Grader nutzen.

Lücke: Mir ist keine Studie bekannt, die *dieselben* Verified-Issues kontrolliert verschlechtert **und** anreichert (S1/S2) und dabei false-success und Kosten misst. Ambig-SWE deckt nur die Verschlechterung ab. Genau dort liegt der Beitrag von Q3.

## 3. Messdesign-Vorschlag

### Unabhängige Variablen (within-instance manipuliert)
Spec-Dimensionen, jeweils als eigene, kontrollierte Transformation desselben Issues:
- **D1 Reproduzierbarkeit:** mit oder ohne Minimal-Repro / Fehlermeldung.
- **D2 Akzeptanzkriterium (Done-Prädikat):** erwartetes Verhalten explizit, z. B. "kernS('(2*x)/(x-1)') == 2*x/(x-1)", oder nicht vorhanden.
- **D3 Scope/Lokalisierung:** betroffene Datei oder Funktion genannt oder nicht.
- **D4 Ambiguität:** Kerninfo entfernt oder vage formuliert (Ambig-SWE-Methode, LLM-umgeschrieben und manuell geprüft).

Bedingungen:
- **S0** Original
- **S1** degradiert (D4, ohne D1)
- **S2** angereichert (D1+D2, optional D3 als eigener Arm S2+loc)
- Optional faktoriell 2×2 (D2 × D3), um Lokalisierung von Done-Prädikat zu trennen.

**Leakage-Kontrolle für S2:**
- Kein Code aus dem Gold-Patch.
- Keine Testnamen oder Testcode.
- Keine Formulierung, die nur aus der PR-Diskussion stammt.
- Ein zweiter Rater prüft blind gegen den Gold-Patch (Checkliste, Cohen's κ melden).
- Zusätzlich wird automatisch gemessen: n-Gram/AST-Overlap der Spec mit dem Gold-Patch unter einem Schwellwert.

**Manipulation-Check:** Die drei OpenAI-Rubrik-Labels (0–3) werden für S0/S1/S2 neu vergeben. Ziel: S1 ≥ 2, S2 ≤ 1.

### Kontrollen
- Gleiches Modell (gepinnte Snapshot-ID), Scaffold-Version (Commit-Hash), System-Prompt, Temperatur, Seeds.
- Gleiches Token-, Schritt- und Zeitbudget.
- Offizieller Docker-Harness (gepinnte Image-Digests), gleicher Repo-Snapshot (`base_commit`), kein Netzwerk bzw. keine GitHub-Suche, damit Issue oder PR nicht nachgeschlagen werden können.
- `hints_text` immer aus.
- Contamination:
  - SWE-bench+-Leak-Instanzen ausschließen oder als Kovariate führen.
  - Memorization-Probe: Modell nach Gold-Patch-Snippet bzw. Dateipfad fragen, ohne Spec.
  - Optional ein Post-Cutoff-Kontrollset (SWE-bench+ / neuere Issues).
- Reihenfolge der Bedingungen randomisieren, alle Läufe im selben Zeitfenster.
- Mindestens 2 Harnesses (stark vs. schwach) für die Interaktionshypothese.

### Metriken
- **Primär:** Resolve-Rate (FAIL_TO_PASS + PASS_TO_PASS, offizieller Harness).
- pass@k und pass^k (k = 3–5 Läufe pro Instanz und Bedingung).
- Kosten: Input- und Output-Tokens, USD, Wall-Clock; Kosten pro gelöstem Task (vgl. SWE-bench+ "effectiveness-aware cost").
- Turns/Schritte bis Submit; Lokalisierungsgüte (Datei-Hit@1 gegen Gold-Patch).
- **Clarification-Requests** (nur im Interaktions-Arm): Anzahl, Rate, Relevanz.
- **False-success-Rate:**
  - (a) Agent meldet "done", Harness sagt fail.
  - (b) Harness sagt pass, manuelle Prüfung gegen Gold-Patch ergibt incorrect oder incomplete (SWE-bench+-Kategorien).
  - (b) auf einer Stichprobe mit 2 Ratern bestimmen.

### Stichprobe und Statistik
- **Paired Design:** jede Instanz in allen Bedingungen.
- Stichprobe: **Ziel ~190 Paare** Verified-Instanzen, stratifiziert nach Repo und Schwierigkeits-Bucket, nur Instanzen mit Rubrik-Labels ≤ 1, fixer Seed.
- **Power** (eigene Schätzung, Reviewer-Korrektur): Für Δ = 10 pp bei ~20 % diskordanten Paaren braucht McNemar (α = 0,05, Power 0,8) ~155 Paare, mit Holm ~190. Reichen die Verified-Kandidaten mit Labels ≤ 1 nicht, gilt bei 80–100 Paaren ehrlich eine **MDE von ~13–15 pp**.
- **Tests:**
  - **Primärvergleich (konfirmatorisch): S2 vs. S0**, McNemar. Sekundär: S1 vs. S0, Holm-korrigiert.
  - Hauptmodell: Mixed-Effects-Logistik `resolved ~ condition * harness + (1|instance) + (1|repo)`.
  - Cluster-Bootstrap über Instanzen (10.000 Resamples) für 95 %-CIs von Δ-Resolve und Kosten.
  - Effektgröße: Odds Ratio und Δ in pp.
- **Pre-Registration** im Notebook vor dem ersten Lauf, festgeschrieben:
  - Hypothesen; primäre Metrik Resolve-Rate; Ausschlussregeln.
  - Primärvergleich S2 vs. S0 (McNemar, α = 0,05); sekundär S1 vs. S0 (Holm).
  - Analyseplan: Mixed-Effects-Logistik `resolved ~ condition * harness + (1|instance) + (1|repo)`, Cluster-Bootstrap-CIs (10.000), OR und Δ pp.
  - Stichprobe/MDE: Ziel ~190 Paare (Δ 10 pp); bei 80–100 Paaren MDE ~13–15 pp.
  - Pflicht: Contamination-Probe (Post-Cutoff/SWE-bench Pro) und UTBoost als zweiter Grader.

### Threats to Validity
- **Konstrukt:** Die Umschreibungen ändern neben der Spec-Qualität auch Länge und Stil. Gegenmaßnahme: längenangepasste Kontrollbedingung mit neutralem Füllinhalt.
- **Leakage in S2:** Der Effekt wäre dann "Hint" statt "Spec". Gegenmaßnahme: Rater-Check und Overlap-Metrik.
- **Contamination:** Verified-Issues sind öffentlich, der Effekt von S1 kann durch Memorization gedämpft werden.
- **Test-Validität:** Die Verified-Filterung ist konservativ, aber schwache Tests bleiben (SWE-bench+: 9,82 % incomplete und 12,5 % incorrect fixes auf Verified). Deshalb ist die False-success-Prüfung nötig.
- **Extern:** Ein Python-only-Datensatz mit 12 Repos und überwiegend <1 h-Tasks lässt sich nur begrenzt auf reale Specs übertragen.
- **Nichtdeterminismus und API-Drift:** Gegenmaßnahme sind gepinnte Versionen, k Läufe und ein enges Zeitfenster.
- **Simulierter User** (falls Interaktions-Arm): Er kann mehr verraten als ein echter Mensch.

## Offene Punkte
- Spaltennamen der OpenAI-Annotations-CSV.
- ClarifyGPT nicht geprüft.
- UTBoost: Die Zahl "26/500 Verified-Tasks" ist nicht voll bestätigt (PDF S. ~7 lesen).
- Ambig-SWE: Werte aus der Grafik abgelesen (±0,1 pp möglich). Text und Figure 3 widersprechen sich ("46% vs 41.8%").


## Quellenprüfung (2026-10-15)

Verifiziert:
- OpenAI 38,3 / 61,1 / 68,3 %: wörtlich im Post (Volltext) und im archive.org-Snapshot. Tag **[VC]** (Herstellerangabe zum eigenen Benchmark).
- OpenAI "Why we no longer evaluate SWE-bench Verified" (23.02.2026): Volltext gelesen ([VC]). Folge: Contamination-Probe mit Post-Cutoff- bzw. SWE-bench-Pro-Kontrollset ist **Pflicht**.
- Ambig-SWE (2502.13069v3): wörtlich "up to 74% over the non-interactive settings" (S. 1–2); [PP], ICLR 2026 nur selbst angegeben. Resolve-Raten aus Figure 3 (S. 5) aus dem Diagramm abgelesen (±0,1 pp). **Widerspruch:** §5 nennt "46% vs 41.8%" (Qwen 3 Coder vs. Sonnet 4) mit Verweis auf Fig. 3; das passt nicht zu den Balken. Wir zitieren Fig. 3 und vermerken den Widerspruch.
- SWE-bench (2310.06770v3, ICLR 2024): Claude 2 erreicht 4,8 % mit Oracle-Retrieval vs. 1,96 % mit BM25 (§5, Table 5/18).
- UTBoost (ACL 2025, S. 3762–3774, arXiv 2506.09289): Abstract und Anthology-Metadaten geprüft. **Pflicht** als zweiter False-success-Grader.

Offen:
- Ambig-SWE: Tabellen 1/2/4/6 nicht zahlenweise geprüft; Fig.-3-Werte nur abgelesen.
- Oracle-Werte anderer Modelle.
- UTBoost "26/500 Verified-Tasks" nicht voll bestätigt.
- ClarifyGPT (2310.10996): nur Existenz und Titel geprüft, keine Ergebnisse; nicht zitieren.
