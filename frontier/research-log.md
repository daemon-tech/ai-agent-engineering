# Research Log

Chronological log of searches, verifications, and decisions. Times are Europe/Berlin (CEST, UTC+2) unless marked UTC.

## R1: 2026-10-14, bibliography verification for v0.1

- **Goal:** verify every candidate reference before citing it.
- **Sources used:**
  - arXiv API (`export.arxiv.org/api/query?id_list=...`) for titles, authors, first-version dates, comments, and DOIs, for all seed arXiv IDs.
  - Crossref REST API (`api.crossref.org/works/<DOI>`) for journal and ACM/ACL/Springer/MIT Press records.
  - Official proceedings indexes: `proceedings.neurips.cc` (2020, 2022, 2023, 2024 pages), `papers.nips.cc` (2025 hash page found via web search, then opened), `proceedings.iclr.cc` (2024, 2025), `iclr.cc/virtual/2023/papers.html`, `proceedings.mlr.press` (v235, v267), the TMLR paper list at `jmlr.org/tmlr/papers/`.
  - Vendor pages opened directly: OpenAI (SWE-bench Verified), Anthropic (Building effective agents), modelcontextprotocol.io.
- **Obstacles:**
  - `dblp.org` search API returned non-JSON responses (blocked); not used.
  - `openreview.net` and its APIs returned a challenge (HTTP 403/307); OpenReview pages could not be read automatically. ICLR acceptance was verified via proceedings.iclr.cc and iclr.cc/virtual instead.
  - Semantic Scholar API was rate-limited (HTTP 429); not used.
- **Decisions:**
  - AutoGen (2308.08155): the venue could not be verified from a primary page, so it is cited as a preprint.
  - τ-bench (2406.12045): not found in the ICLR 2025 proceedings index; no other venue verified; cited as a preprint.
  - MemGPT (2310.08560): no venue found; preprint.
  - *Update 2026-10-15:* AutoGen verified as COLM 2024 (OpenReview BAakY1hNKS) and τ-bench as ICLR 2025 (ICLR proceedings index); MemGPT remains a preprint. See references-verification.md.
  - Agentless: the arXiv title differs from the published FSE 2025 (PACMSE) title "Demystifying LLM-Based Software Engineering Agents"; cited by the published record with an arXiv cross-reference.
  - Hassan et al. ASE roadmap: the arXiv preprint (7 authors) and the ICSE 2026 two-page item (9 authors, DOI 10.1145/3774748.3776601) are different records; both kept, and the ICSE item is marked "review type unverified".
  - Kwa et al. (time horizons): arXiv journal_ref says NeurIPS 2025; confirmed on the NeurIPS 2025 virtual poster page and proceedings hash page. Author lists differ by one name (Chris Painter in arXiv v4 only), noted in BibTeX.
- **Outcome:** 52 BibTeX entries, all verified; see `references-verification.md`.

## R2: 2026-10-14, frontier scan of arXiv cs.SE

- **Query (arXiv API):** `search_query=cat:cs.SE AND (abs:agent OR abs:agents)`, `sortBy=submittedDate`, `sortOrder=descending`, `max_results=60`. Run on the afternoon of 2026-10-14 (CEST).
- **Returned:** 60 entries with submission dates 2026-10-08 to 2026-10-13 (UTC).
- **Kept for the review (9):** 2610.13361 (AgentSWE), 2610.14096 (SWEeper-Bench), 2610.14768 (SWE-Maintain), 2610.16067 (oracle failures), 2610.14460 (re-execution), 2610.18206 (SWE-MISBEHAVIOR), 2610.13227 (cross-session skill attacks), 2610.14216 (Cortex), 2610.17418 (workflow failure taxonomy).
- **Inclusion criteria:** bears directly on verification, evaluation validity, cumulative effects, boundaries and security, or harness engineering for ASE, and states concrete results in the abstract.
- **Seen but not included (examples, with reason):**
  - 2610.18484 ReTerm (terminal-agent recovery training): training-method focus; revisit.
  - 2610.18004 SWEPatchTest; 2610.13065 TestSuiteBench; 2610.16870 SpecGuardBench: test-generation benchmarks, relevant to verification; deferred to a dedicated test-generation review.
  - 2610.17616 StateHarness: long-horizon project state; deferred, relevant to memory (Chapter 03 §5).
  - 2610.15093 TurnCost (cache-aware loop engineering): relevant to harness efficiency; deferred.
  - 2610.15567 (agent vs. human PR review); 2610.12849 (agent PRs co-modifying infrastructure): empirical studies of agent PRs; deferred to a review of mining studies.
  - 2610.13668 (code-review agents, "lights-off" software factory); 2610.13022 (interactive requirement clarification): relevant to oversight and specification; deferred.
  - 2610.14405 SPROUT; 2610.13395 ProgramGym; 2610.14163 AutoEnvScaling: RL training environments; out of v0.1 scope.
  - Others (kernel development, SQL test generators, spatial AI, MARL platforms, product management vision): out of scope.
- **Also checked:** SWE-Bench Pro (2509.16941) and SWE-Bench Pro Verified (2609.08149) via an arXiv title search, because the re-execution paper references SWE-Bench Pro.

## R3: 2026-10-14, standards and vendor sources

- `https://modelcontextprotocol.io/specification/latest` redirected to `/specification/2026-07-28` (HTTP 200); changelog read.
- OpenAI "Introducing SWE-bench Verified" page: dated August 13, 2024, "Updated February 24, 2025".
- Anthropic "Building effective agents": "Published Dec 19, 2024". The page now carries a note that "Much of the tooling landscape described in this post has changed since December 2024."

## R4: 2026-10-14, pstack case study

- Cloned `https://github.com/cursor/plugins` (sparse checkout `pstack/`) at commit `1e5c90a4b6f249917bd21fe361b3a2a7deb741b8`, 2026-10-14T00:04:30-07:00 (09:04:30 CEST), commit message "chore(pstack): bump to 0.15.24 (#617)".
- The local cached copy on the research machine (version 0.15.23) differed from the official checkout in 41 file comparisons (40 changed files, 1 file present in only one copy); the official source was used.
- Searched README, guide, playbooks, and principles for outcome claims; found none quantitative (see case study §5).

## R5: 2026-10-14, term-usage check

- Web search for prior use of "agent engineering". Practitioner sites use the term (e.g., agentengineering.org, which returned HTTP 200 when checked). Two 2026 arXiv reviews use "harness engineering" (2604.08224, 2606.20683; both verified via the arXiv API). Result: we do not claim the term; see Chapter 00 §6.2 and Chapter 01 §2.3.
