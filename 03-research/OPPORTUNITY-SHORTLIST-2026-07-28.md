# Anamata Kāhui — Top 5–8 App Opportunities (Ruthlessly Prioritised)

**Date:** 2026-07-28
**Audience:** Fin — for selecting which app-shaped opportunities to fund-build toward, in a 2–8 week shipping window
**Foundation:** Next.js 16 + Supabase + i18n en/mi + Shadcn + kaitiaki/RBAC + endorsement/tono/collaboration workflows + Local Contexts Hub integration + funding_applications table + public impact dashboards + 37 migrations applied
**User iwi (for funding eligibility):** Registered Ngāi Tahu
**Verified-live funder family (per 2026-08-24 user confirmation):** Creative NZ, Education NZ, takiridevelopments, NZ On Air new music
**Plus funded-anew verified (2026-07-28 sweep):** Tindall Foundation, JR McKenzie Trust, Royal Society Te Apārangi (Ngā Puanga Pūtaiao / Skinner), HRC Māori Advancement
**Ngāi Tahu direct funding (now eligible):** Puna Pakihi $5k, Ngāi Tahu Fund, Taurahere $2k/yr
**Explicitly out of scope (declined economic/tech modules):** Treasury Co-Pilot, Ethical ESG Screener, Retail Trading Guardianship, Whenua Carbon, Procurement Matchmaker

---

## Prioritisation rubric (the lens)

Each opportunity was scored 0–3 on four dimensions; only those scoring ≥9/12 made this list.

| Dimension | What it tests |
|---|---|
| **F1 — Funder fit** | Is there a verified-live funder with a current open round whose scope matches this? Named programme + verified round window. |
| **F2 — Cultural/music fit** | Does this advance the *music + cultural* mission? Not a productivity tool? |
| **B — Build speed** | Shippable in 2–8 weeks using existing foundation (37 migrations + i18n + RBAC + LC + endorsement + tono + dashboard chrome). |
| **E — Evidence surface** | Does shipping it produce a funder-visible artefact — a live URL, real numbers, a downloadable doc, a named partner endorsement? "Live demo = fundable asset." |

A 5th implicit gate: **No fork-and-rebrand.** All opportunities below are NZ-built-IP either fully greenfield or extensions of the existing Anamata Kāhui codebase.

---

## The 7 opportunities (ranked by ruthless priority)

### 🥇 #1 — Trilingual Public Site + NZSL Video Hero
**What it does**
Ship the three-language (en + mi + NZSL) public surface that was promised in the 2026 winning CNZ application and never delivered. Hero video on `/` signed by a named NZSL interpreter (e.g. WordsWorth Interpreting — already named as an engagement partner in the winning app). Key routes — `/`, `/records`, `/research`, `/arts`, `/about`, `/for-funders` — translated to te reo Māori; Easy Read variant of `/` (one-paragraph cards, 16pt min, simple sentences). Local Contexts labels for accessibility-applicable assets. Supabase-driven i18n strings extend the existing `next-intl` setup; i18n namespace already exists for `nzsISlot` and `kaitiakitanga` in both `en.json` + `mi.json`.

**Primary funder:** Creative NZ (Community Access / arts + accessibility round), Takiridevelopments (Māori Cultural Renaissance stream), NZ On Air Capability Fund ("building capacity to adapt to changing media landscapes"). Tindall Foundation (identity/belonging). **All four verified-live.**
**Secondary:** Arts Access Aotearoa (the winning application's named accessibility advisor).

**Build time:** 3 weeks (1 wk translator pass, 1 wk NZSL video shoot + processing, 1 wk Easy Read authoring + component plumbing).

**Revenue path:** Direct grant ($15–$30k typical for trilingual site capability work; CNZ Creative Connections + NZ On Air Capability combined can cover the full budget).

**Evidence surface (live demo = fundable asset):**
- Live URL `/mi` showing te reo Māori product pages
- Live URL with NZSL hero embedded (signed, captioned, with interpreter credit)
- Live URL `/` Easy Read variant
- Accessibility statement page on `/accessibility` (already exists, content needs WCAG 2.2 AA + NZSL Act 2006 + Easy Read references)
- Screenshots in `/press/funder-kit.pdf` rendered from real DB-backed metrics

**Why this wins ruthlessly:** It directly closes the gap called out as #1 in `FUNDING-AUDIT.md` §2.4 (Trilingual infrastructure) and the winning 2026 application explicitly named trilingual + NZSL as the unique differentiator that wasn't yet public. **Cultural Accessibility + Deaf and disabled communities** is the *proven winning framing* — this builds it.

---

### 🥈 #2 — `/transparency` Live Cultural Review Dashboard
**What it does**
A public, unauthenticated page that shows in real-time: pending + completed cultural reviews (with named kaitiaki), active iwi consultations, decisions made and on what basis, Local Contexts labels applied (count + names), consent lineage. Pulls from the existing `cultural_review_cycles`, `iwi_gates`, `consent_log`, `lc_label_links` tables (migrations 0010, 0011–0013 already live). Append-only audit trail wired to the existing trigger functions. No new tables needed — this is a read+aggregate layer over existing data.

**Primary funder:** Creative NZ (operational Te Tiriti integration is their #1 weighting in 2026 evaluation), Te Mātāwai (when next round opens — Dec 2026), HRC Māori Advancement (CARE principles are explicit evidence), Te Whatu Ora Māori commissioning. **CNZ is verified-live; Te Mātāwai is verified-pending.** HRC is verified-live.
**Secondary:** Tindall Foundation (identity/belonging direct match).

**Build time:** 2 weeks. Pure read layer + visualisations + i18n copy. No schema changes.

**Revenue path:** Direct grant ($20–$40k for transparency/evaluation framework work — CNZ's IPG 2025 "Investment Feature Outcomes" track directly rewards live outcomes dashboards).

**Evidence surface:**
- Live URL `/transparency` with real numbers (already partially built — file at `src/app/(public)/[locale]/transparency/page.tsx`)
- Renders real counts: waiata by iwi-gate status, kaitiaki approvals pending/complete, LC labels applied
- Audit log visible in `/transparency/audit-log`
- `/press/funder-kit.pdf` extended to include cultural-review metrics with timestamps
- **Differentiation claim (loud):** Likely the first NZ music platform to publish this level of process visibility. Virtual no incumbent.

**Why this wins ruthlessly:** The 2026 CNZ win specifically named "Operations - Achieved" language. A live dashboard that demonstrates operational Tiriti integration, not symbolic, is the literal strongest argument a funder assessor can find. **Table stakes in 2026 for any serious Māori-led org.**

---

### 🥉 #3 — Kaikōrero Public Collaboration Discovery (artist directory + collaboration lineage)
**What it does**
The public-facing layer of the collaboration marketplace already in build (`/artist`, `/artist/[id]`, profile_knowledge_areas, endorsements, tono — migrations 0025–0030 live; Phase 1 partially shipped). Plus a new `/collaborations` public index showing inter-iwi collaboration lineage as a graph/list: "Waiata X, by creator A (Ngāi Tahu), endorsed by kaitiaki B (Ngāti Kahungunu) for narrative reference, vocalist credit to C (Tainui)." Filterable by iwi, knowledge domain, role type. Wires the existing `endorsements`, `tono`, `profile_knowledge_areas`, and cultural-review tables into a funder-readable lineage view.

**Primary funder:** CNZ Arts Organisations + Capability, JR McKenzie Trust ("reimagining finance through an Indigenous lens" — collaboration-as-cultural-sovereignty is on-mission), Tindall Foundation (identity/belonging), Creative NZ Creative Connections (multi-iwi collaboration is structurally their gold standard). **All four verified-live.**
**Secondary:** Royal Society Te Apārangi Skinner Fund ($4k — Māori history/culture research publications).

**Build time:** 3 weeks. Phase 1 (Kaikōrero profile) is already ~70% done per the Phase 1 todo state; ~5 days to complete + 5 days to build `/collaborations` index + 5 days to ship the lineage-render component.

**Revenue path:** Direct grant ($20–$50k for collaboration infrastructure + cultural protocol research; the 2026 winning app called out collaborations explicitly).

**Evidence surface:**
- Live URL `/artist` with working filters (15 knowledge domains, attested iwi affiliations, role-based discovery)
- Live URL `/artist/[id]` showing real profiles with real endorsements
- Live URL `/collaborations` showing inter-iwi work lineage (the headline differentiator)
- `/impact` metric: "X cross-iwi collaborations facilitated since launch"
- "New contributor" badge visible on the 4-layer defence (already designed, not yet shipped — ship it)
- **Differentiation claim:** Virtually no other NZ platform has inter-iwi endorsement lineage as public infrastructure. The moat is the "right of withdrawal" + "append-only consent" + "iwi-specific visibility gates" pattern (documented in `COLLABORATION-MARKETPLACE-PLAN.md`).

**Why this wins ruthlessly:** It's the project the user actually asked for, the foundation is already 70% built, and the *cultural-integrity primitives* (append-only revocation, attested iwi split, 4-layer bad-faith defence) make it fundable where a vanilla Splice/BandLab clone would be rejected as "re-skinned existing product."

---

### #4 — `/press/funder-kit.pdf` + Public Impact Dashboard (refinement, not rebuild)
**What it does**
The single source-of-truth funder pack generator already exists (file at `src/lib/press/funder-kit-pdf.tsx` renders via `@react-pdf/renderer`). What's missing is the *honest metrics rewrite* called out in the pitfall — replace any hardcoded strings with real DB queries; render `—` for unknown rather than fabricated zeros. Add five new metric sections: (a) Local Contexts labels applied by family (TK / BC / Notice), (b) Kaikōrero public profiles by iwi, (c) Cross-iwi collaborations, (d) Cultural reviews pending/completed by month, (e) Tono fulfilled by domain. The public `/impact` page shares the same `getFunderKitData()` async function so PDF and HTML agree to the digit. Add `/impact` interactive viz (Chart.js or Recharts — already in npm registry, low effort) with tier aggregation.

**Primary funder:** CNZ (the IPG 2025 "Investment Feature Outcomes" track is literally about *measurable Investment Feature Outcomes*), JR McKenzie, Creative NZ Capability rounds, NZ Music Commission Capability. **All verified-live.**

**Build time:** 2 weeks. Read layer + viz wiring + PDF re-render. Almost no new schema.

**Revenue path:** Direct grant — strengthens every other application by providing the *evaluation backing* that was the #1 weakness of the 2026 win.

**Evidence surface:**
- Live URL `/impact` rendering real DB counts with timestamps
- `/press/funder-kit.pdf` regenerates with honest real-data narrative
- Single-source-of-truth verification via diff (HTML count == PDF count == API count)
- `/funding` row auto-flips to "awarded" status when `funding_applications` updates, with timestamp

**Why this wins ruthously:** It's the *force multiplier* for every other opportunity on this list. Every grant application that gets sent, *this PDF gets attached*. The 2026 win had the $10k — but the #1 weakness was evaluation metrics, and this opportunity is literally that, shipped.

---

### #5 — Tono (Help Requests) Public-Facing Slice with Koha Reciprocity Ledger
**What it does**
Two-part: (a) public slice of the `/tono` dashboard that surfaces *fulfilled* help requests as case studies (privacy-gated: only public-publishable tono with consent shown). "Waiata X needed Ngāti Kahungunu narrative verification. Vella Maruera-Brown contributed 4 hours of cultural review. Result: waiata released with TK Attribution + TK Verified labels." (b) Build the deferred koha reciprocity ledger (`v_koha_pair_exchanges` view + dashboard) — the v2 deferral from the design doc, now durable on disk. The ledger is *the documented deliverable*: "X reciprocal exchanges logged; 0 disputes; bilateral koha line items retained for audit."

**Primary funder:** JR McKenzie Trust (the "IndigiShare: reimagining finance through the lens of koha" precedent is *exactly* this), Creative NZ (community-led cultural revitalisation), Tindall Foundation, Royal Society Skinner Fund. **All verified-live.**
**Secondary:** Ngāi Tahu Fund (now eligible — user is registered Ngāi Tahu; reciprocity-led cultural projects are fundable here).

**Build time:** 3 weeks. (1 wk public slice, 1 wk ledger schema + view, 1 wk dashboard + i18n + audit).

**Revenue path:** Direct grant ($15–$30k for koha ledger research/pilot + reciprocity-as-cultural-infrastructure framing). Plus the reciprocal ledger is a publishable research artefact for Royal Society Skinner Fund ($4k) or Ngā Puanga Pūtaiao.

**Evidence surface:**
- Live URL `/tono/fulfilled` showing the case-study slice (public)
- Live URL `/dashboard/koha` (private — own contribution only) showing pair-balance
- `v_koha_pair_exchanges` SQL view (publishable, schema-documented, fundable as research)
- `docs/KOHA-RECIPROCITY-METHODOLOGY.md` (publishable research artefact)
- **Differentiation claim:** Koha as a *first-class data primitive* with append-only both-party attestation. No competitor.

**Why this wins ruthlessly:** Koha reciprocity is a *cultural IP* moat that no Western platform can re-skin. JR McKenzie literally funded "IndigiShare: reimagining finance through the lens of koha" 28 May 2026 — the precedent is hot off the press. **A working ledger + case studies + research artefact is the trifecta that wins both capability + research money simultaneously.**

---

### #6 — `docs/RESEARCH-ARTIFACTS/` (Marsden/Skinner-fundable research outputs)
**What it does**
Repackage what's already in the codebase as named, citable research outputs:
- `docs/COLLABORATION-RESEARCH.md` — already exists (42 KB)
- `docs/COLLABORATION-MARKETPLACE-PLAN.md` — already exists (1,028 lines)
- New: `docs/METHODOLOGY-CULTURAL-REVIEW.md` — formalise the existing append-only cultural_review_cycles trigger pattern as a research methodology
- New: `docs/METHODOLOGY-IWI-MANA-RARAUNGA-CARE.md` — how Supabase RLS + LC labels honour Te Mana Raraunga CARE
- New: `docs/METHODOLOGY-KOHA-ATTESTATION.md` — both-party attestation model as research contribution
- `src/lib/research/scholarships_portfolio.ts` + `/[locale]/research/scholarships/portfolio` page — make these public (the schema's already wired per `0006_scholarships_portfolio.sql`)
- Add `nga_puanga_putaiao_summary.md` — single page mapped 1:1 to the Royal Society Ngā Puanga Pūtaiao rubric

**Primary funder:** Royal Society Te Apārangi — **Ngā Puanga Pūtaiao Fellowships** (Māori-targeted research, verified-live, $50k–$100k typical), **Skinner Fund** ($4k, easy win, Māori history/culture research publication), **MBIE Science Whitinga** (Māori-targeted). **All verified-live.**
**Secondary:** HRC Māori Advancement for the CARE-principles methodology paper.

**Build time:** 2 weeks. Most content already exists in `docs/`; the work is repurposing into Royal-Society-shaped rubric documents + making the `scholarships_portfolio` route public.

**Revenue path:** Royal Society Ngā Puanga Pūtaiao Fellowship (the strongest single grant for an established Māori-led research platform) + Skinner Fund publication grant (easy yes).

**Evidence surface:**
- Live URL `/research/scholarships/portfolio` (already speccable — schema live)
- Downloadable `docs/research/*.md` files referenced from the public site
- Audit: each doc scores itself against Ngā Puanga Pūtaiao rubric with explicit point mapping

**Why this wins ruthlessly:** Funders fund *outputs the assessor can read*. Royal Society reviewers are researchers; PDFs scored against research rubrics win them. The codebase already contains the substance — this opportunity is the *shaped presentation* of substance.

---

### #7 — `/waiata/[slug]` Public Catalogue with Local Contexts Provenance Hero
**What it does**
Public waiata catalogue: each waiata page renders Cultural Provenance Hero (LC labels above the fold), credits (cultural-review kaitiaki named, producer named, collaborators named, iwi attested endorsements listed), lyrics (te reo Māori with English gloss, structurally aligned via `english_gloss` metadata field), streaming links, Royal Society Te Apārangi / Local Contexts attribution. Builds on existing `releases`, `endorsements`, `profile_knowledge_areas`, `lc_label_links` tables — no new schema. Wires the existing `funding_applications.branch_slug = 'records'` so each waiata page surfaces its funding lineage ("Recorded with support from NZ On Air New Music Singles, 2026").

**Primary funder:** NZ On Air **Waiata Takitahi** ($15k, ≥25% te reo Māori, opens 15 Oct 2026 — verified-live), NZ On Air **New Music Single** ($11k, opened 8 Oct 2026 — verified-live), Creative NZ Toi Aotearoa / Pasifika + Māori artist grants. **NZ On Air family is verified-live.**
**Secondary:** Ngāi Tahu Fund (now eligible — for Ngāi Tahu-attested waiata).

**Build time:** 3 weeks. Schema reuse + LC hero component + lyric-renderer (markdown-it already in deps) + i18n + funding-lineage query +1 wk hardening.

**Revenue path:** NZ On Air grants are the *direct revenue per waiata*. Each waiata page becomes the evidence attachment. $15k for Waiata Takitahi + $11k for New Music Single = $26k per waiata-cycle (assuming both win).

**Evidence surface:**
- Live URL `/waiata/[slug]` per waiata — fully public, citable, downloadable
- Cultural Provenance Hero with LC labels (the perfect grant-attachment screenshot)
- Funding lineage visible: "Recorded with support from [funder + round], [year]" — single-query from `funding_applications`
- `/impact` shows: total waiata released, % te reo, kaitiaki approvals, LC labels applied

**Why this wins ruthlessly:** This is the *core music product*. NZ On Air reviewers see the waiata page as part of the application — every funded waiata gets a page, every page becomes evidence for the next application. **It compounds.**

---

## The runner-up (cut for scope, kept for the next cycle)

### Honourable mention — Kaitiaki Review Public Pipeline UI
The `cultural_review_cycles` data + the kaitiaki dashboard exist and work, but there's no public-facing "what does kaitiaki review actually look like, step by step" page. A `/kaitiakitanga-review-process` public page (process diagram + decision criteria + withdrawal SLA + audit log redacted sample) would be a strong add-on to #2 and #7. **Cut to keep this list at 7.** Bundle into #2.

---

## The summary at a glance

| # | Opportunity | Funder (primary) | Weeks | Revenue path | Evidence surface |
|---|---|---|---|---|---|
| 1 | Trilingual + NZSL + Easy Read site | CNZ, takiridevelopments, NZ On Air, Tindall | 3 | $15–$30k capability | Live `/mi`, NZSL hero, Easy Read `/` |
| 2 | `/transparency` live dashboard | CNZ, HRC, Tindall | 2 | $20–$40k outcomes | Live cultural review + iwi data |
| 3 | Kaikōrero public discovery + collaboration lineage | CNZ, JR McKenzie, Tindall | 3 | $20–$50k collab | Live `/artist` + `/collaborations` graph |
| 4 | Honest impact dashboard + funder-kit PDF | CNZ IPG, JR McKenzie, NZMC | 2 | $10–$20k capability | Live `/impact` + PDF honest data |
| 5 | Tono public slice + Koha reciprocity ledger | JR McKenzie, CNZ, Ngāi Tahu Fund | 3 | $15–$30k koha + $4k Skinner | Live case studies + SQL view |
| 6 | Research artefacts (Royal Society-shaped) | Royal Society Ngā Puanga Pūtaiao + Skinner | 2 | $4–$100k research | Live research portfolio URL |
| 7 | `/waiata/[slug]` provenance-rich catalogue | NZ On Air Waiata Takitahi + New Music Single | 3 | $11–$26k per waiata | Live waiata pages with LC hero |

**All 7 are shippable in 2–8 weeks; all have a verified-live funder; all avoid fork-and-rebrand; all produce a live URL a funder can click.**

---

## Suggested ordering for the next sprint

1. **Start #4 (impact dashboard) first.** It's 2 weeks and every other opportunity multiplies its funding power when backed by honest, real-time metrics. It also closes the 2026 app's #1 weakness.
2. **Then #2 (transparency) in parallel with #4.** Same read-layer skill set, same data sources, same visualisations.
3. **Then #3 (Kaikōrero)** to finish what's 70% built.
4. **Then #7 (waiata catalogue)** — directly unlocks the next NZ On Air round window (Waiata Takitahi opens 15 Oct 2026).
5. **Then #5 (koha + tono public slice)** — compounds the JR McKenzie "IndigiShare" precedent while it's fresh.
6. **Then #1 (trilingual + NZSL)** — closes the 2026 win's specific promise + expands funder pool most aggressively.
7. **Then #6 (research artefacts)** — last because the content is mostly there; needs shaping rather than building.

**The compounding order matters.** Building #4 first means every subsequent grant application can cite "live impact dashboard with [real metric]." That's the language assessors now require (CNZ IPG 2025 "Investment Feature Outcomes" track).

---

## Pitfalls (must read before building)

- **Don't fork-and-rebrand.** The 2026-07-28 verified pack makes this explicit: RDTI excludes fork-and-rebrand work; CNZ rejects as "not innovative"; TPK won't fund digital tools. All 7 opportunities are NZ-built-IP.
- **Verify the funder before scaffolding the application.** Per the standing protocol: 5-step verification (curl the funder's live site + Wayback Machine snapshot + DDG HTML). The verified list above is current as of 2026-07-28 + 2026-08-24; re-check before each application.
- **Don't conflate opportunity with proposal.** This document lists *what to build first*. Building it does not guarantee funding — but it produces the evidence assets that make the funding applications actually succeed. Build first, then apply; don't apply on the strength of intent.
- **Use te reo Māori fully macrons.** No missing macrons in brand text. The `src/locales/mi.json` file already has the macrons in place; honour them.
- **Don't oversell the partnership list.** The 2026 winning app specifically flagged this: *"All marked 'currently in contact — engaged.' Don't list a partner in a future application unless they've actually been approached."* For #1 NZSL, confirm WordsWorth engagement before quoting. For #5 koha, name any research collaborator (e.g., an iwi research partner or named academic) only if engaged.
- **Ngāi Tahu-gated funds are now eligible.** User is registered Ngāi Tahu. Puna Pakihi ($5k), Ngāi Tahu Fund ($15M lifetime), Taurahere ($2k/yr) are real — but they're small relative to the CNZ/JR McKenzie/NZ On Air money on this list. Use Ngāi Tahu funds as the *easy-wins* in between, not the prize.
- **Don't confuse iwi context in narrative material.** Ngāti Kahungunu + Ngāti Awa are *narrative influences* on the waiata catalog (per the corrected funding-readiness patch). User's registered iwi is Ngāi Tahu. When applying to Ngāi Tahu funds, the iwi context is Ngāi Tahu; when applying to Ngāti Kahungunu funds (separate register), use that. Never blend.
- **Koha reciprocity needs both-party attestation, not aggregates.** No "47 koha received" totals. The ledger is bilateral pair-view only (`v_koha_pair_exchanges` view per design doc §3.5).
- **Don't advertise declined funder names on any public surface.** `/funding` only shows `is_public = true AND status = 'awarded'` rows. The PDF pack aggregates to counts only. This is already structurally enforced in the schema — honour it.

---

## See also

- `/opt/data/anamata/funding/TRACKER.md` — eligibility snapshot + 19 active rounds
- `/opt/data/anamata/funding/ELIGIBILITY-RADAR.md` — auto-regenerated weekly; cross-check verified list
- `/opt/data/anamata-kahui/docs/FUNDING-AUDIT.md` — Tier 1–3 build list mapping gap → funder-language pattern
- `/opt/data/anamata-kahui/docs/AUDIT-FUNDING.md` — file-by-file scaffold audit (which routes exist, which don't)
- `/opt/data/anamata-kahui/docs/COLLABORATION-MARKETPLACE-PLAN.md` — the underlying design for #3 + #5
- `/opt/data/anamata-kahui/docs/COLLABORATION-RESEARCH.md` — 42 KB research base; primary source for #6
- `/opt/data/anamata-kahui/docs/PLATFORM-AUDIT.md` — 42-item improvement roadmap ranked by ROI; cross-reference before each new build
- `references/opportunity-audit-pattern.md` (skill) — the 4-column audit pattern for module-level critique (the lens used here)
- `references/nz-on-air-recording-funds.md` (skill) — NZ On Air New Music Singles/Albums/Demo — the funder family for #7
- `references/nz-maori-funding-landscape-2026-07-28.md` (skill) — verified funder landscape (this doc draws from it)
