# Creative Fellowship Fund 2026, Round 2 — submission package

**Applicant:** Ngaika Smith, applying as an individual
**Fund:** Creative New Zealand, Creative Fellowship Fund 2026 Round 2
**Pool:** Ngā toi Māori
**Ask:** $50,000, up to twelve months. Activity window 2 December 2026 to 31 December 2027.
**Deadline:** 1:00 PM NZ time, Thursday 24 September 2026 (01:00 UTC the same day)
**Prepared:** 24 September 2026

## The documents, in the order they are used

| # | PDF | Pages | What it is | Where it goes |
|---|---|---|---|---|
| 02 | `02-CNZ-CreativeFellowship-R2-Portal-Answers.pdf` | 5 | The executive summary and the five answers, with character and word counts per field | Paste into the portal fields. The `.txt` version is the raw paste source |
| 03 | `03-CNZ-CreativeFellowship-R2-Somatosensory.pdf` | 7 | The application as a document: at a glance, the five answers, twelve month timeline, budget ledger, collaborators | Support material, if the form takes an upload |
| 04 | `04-CNZ-CreativeFellowship-R2-Accessibility-Evidence.pdf` | 4 | What the 2026 Development Fund programme is, what is publicly verifiable, what is ongoing, what independent corroboration exists, how it relates to this fellowship, what does not exist yet | Support material for the accessibility claims |
| 05 | `05-CNZ-CreativeFellowship-R2-Method-Annex.pdf` | 8 | The practice brief (rig, twelve phase one tests, participant care, session architecture, alignment method) and tactile notation v0.1 | Support material for the method the application claims |

Support material added 24 September:

| # | PDF | Pages | What it is |
|---|---|---|---|
| 14 | `14-CNZ-CreativeFellowship-R2-CV-Ngaika-Smith.pdf` | 2 | Artistic CV, built from the verified record: practice, recorded work, funding and programme leadership, cultural practice, accessibility practice, sector relationships. No education or earlier roles because those are not verified, so add them and it regenerates |
| 15 | `15-CNZ-CreativeFellowship-R2-People-and-Organisations.pdf` | 2 | The participation records entered in the portal, formatted for upload if the form asks for the same thing as a document |

Working files behind them: `06-PORTAL-ANSWERS.txt` (raw paste text), `07-APPLICATION-full.md` (answers plus timeline, budget and collaborator annexes and the internal correct-these list), `08-SUBMIT-CHECKLIST.md`, `09-FIRST-CONTACT-EMAILS.md`, `10-COLLABORATOR-SHORTLIST.md`, `11-ACCESSIBILITY-PROGRAMME-EVIDENCE.md`, `12-PRACTICE-BRIEF.md`, `13-TACTILE-NOTATION.md`.

All four PDFs render through one design system: A4, Liberation Serif, crescent letterhead with the entity line, kōkōwai used for the wordmark and kicker only, booktabs tables with hairline rules, page numbers in the footer. No em dashes, no emoji, no sans-serif body. Rebuild with `build/build_pdfs.py`, which writes both the source markdown and the PDF. The paste-ready answers are regenerated from `APPLICATION.md` with `build/build_portal_answers.py`, so the counts in the PDF are computed from the text that is pasted.

## Counts, verified against the pasted text

| Field | Characters | Words |
|---|---|---|
| Executive summary | 1,167 | 198 |
| Question 1 | 2,485 | 416 |
| Question 2 | 2,425 | 395 |
| Question 3 | 2,494 | 436 |
| Question 4 | 2,476 | 399 |
| Question 5 | 2,499 | 436 |

Every field is under 2,500. The fund publishes no limit, so these are targets rather than caps, and the tables in `APPLICATION.md` and `SUBMIT-CHECKLIST.md` carry the same figures.

## Revision, 24 September, after two review passes

**Method annex.** Vest routing and latency (analog or USB path, Bluetooth not accepted as the scored path, latency measured and logged), vibration exposure referenced to ISO 2631-1 and ISO 5349-1 with accelerometer measurement, participant care (screening, informed consent, opt out at any point, fees for time, CARE-based data sovereignty, cultural review of the protocol before the first session), a hardware quote plan, a specific phase alignment method with a five millisecond residual target, a cross-channel simultaneity rule in the notation, and a proposed te reo column on the body location codes.

**Evidence annex.** Revised after the programme files were re-baselined. The annex had been carrying the pre-re-baseline schedule: a July 2026 to June 2027 window, a September 2026 baseline report, a December 2026 vibrotactile trial, a February 2027 prototype, and a March 2027 mid-programme report to Creative New Zealand that does not exist and is not owed. Every date now comes from the programme's own DELIVERABLES.md and TIMELINE.md: eighteen months to December 2027, trial 30 April 2027, prototype 30 June 2027, single report and acquittal 17 December 2027. Added: an "independent corroboration" section separating what is self-published from what a third party can check (award letter on file, named partner contacts, letters of support requested not received, contracts not signed), an explicit no-double-funding paragraph on the two vibrotactile lines, a time partition sentence, and a reframed non-engagement line that treats not asking disabled artists to work unpaid before funding exists as the protocol rather than a gap.

**Application.** Four changes:
1. **Scope discipline.** The method, the notation and three recorded works are now named as the core deliverable in the executive summary, Question 1 and Question 5. The public wānanga and the mentoring sit inside the same year and are stated as what flexes first if the year runs behind.
2. **The solitary baseline, answered.** Question 3 and the timeline now record that T1 to T3 are measured on hearing bodies first and are provisional by design, with a Deaf collaborator engaged from month one and Access Advisors reviewing those figures at month two, and every threshold re-measured with Deaf and tāngata whaikaha collaborators from month five.
3. **The open-versus-protected boundary.** Question 4 and the collaborator table state what is published openly (notation, DAW and mixing templates, protocol) and what stays under kaitiakitanga (mātauranga Māori, the waiata, kōrero tuku iho, and anything a collaborator brings to a session), released only with the holders' consent and only for the use consented to.
4. **Production and the ledger.** The answers state that recording and production run through the label's own studio and post-production workflow, so no commercial studio hire sits in the ask. The ledger was rebalanced: interpreter cover now costed at two interpreters per session including preparation time ($5,500), collaborator fees at fair pay day rates including the month-one calibration collaborator ($11,000), hardware unchanged ($6,800), documentation trimmed to $1,200, and the stipend is the line that flexes ($25,500, about $490 a week).

## Naming audit

| Finding | Action |
|---|---|
| "Anamata Kāhui" used for the collective, and "Anamata" alone in the closing paragraph of Question 5 | Corrected to **Te Kāhui Anamata** everywhere the collective is named |
| Letterhead entity line and footer in every PDF | Read Te Kāhui Anamata |
| "Anamata Kāhui Limited" as the registered company | Left as is in seven places, being where the company is the applicant or the trading entity. That is the name on the register (NZBN 9429052960734, company 9350922). Say the word if the register name itself has changed and all seven change with it |

## Gaps I cannot close without you

| Item | State |
|---|---|
| **Artistic CV** | Written from the verified record and in the package as document 14. It carries no education or earlier roles, because none is verified. Send those and it regenerates in minutes |
| **Samples of work** | Exist, not picked. Three links need choosing from the released catalogue |
| **Letters of support** | None obtained. Two are worth asking for: Maurea on cultural process, and a Deaf arts partner or Arts Access Aotearoa on the collaboration structure |
| **Te reo title sign-off** | Outstanding. Recommendation stands: Ngā Wiri o te Tinana, subtitle stopping at vibrotactile waiata |
| **The stipend figure** | $31,200 down to $25,500 to fund interpreter and collaborator lines properly. Confirm you accept it |
| **Month-one collaborator** | The timeline now depends on a Deaf collaborator being engaged within 30 days of award. Confirm that is realistic |
| **The supplement claim** | The answers say the access relationships, cultural review and trilingual pipeline are already in place through the 2026 programme. Confirm before an assessor reads it |
| **Hardware quotes** | The $6,800 line is a planning envelope, labelled indicative in the method annex and backed by a quote plan. No figure is claimed as a price |
| **Collaborator names, six waiata slate** | As previously flagged |

## Integrity checks before this goes in

1. **The Maurea relationship.** The application, the platform accessibility page and the funded programme's partner file all describe cultural review with Maurea dating from 2024. If the first contact email is genuinely first contact, that wording is wrong in three places and needs changing today.
2. **Programme end date. Resolved 2026-09-24.** The programme runs to the end of 2027, and the application and the annex now cite the re-baselined dates. The fellowship answered the review by stating the two programmes share no cost line and no hour.

## Final upload names

`final/` holds byte-identical copies of the built PDFs under the names that go into the portal. Rebuild with
`build/build_pdfs.py`, then re-publish with `build/publish_final.py`.

| Final name | Internal source | Document |
|---|---|---|
| `Ngaika-Smith-CNZ-Creative-Fellowship-Fund-2026-R2-Application.pdf` | `CNZ-CreativeFellowship-R2-Somatosensory.pdf` | The application (the proposal) |
| `Ngaika-Smith-CNZ-Creative-Fellowship-Fund-2026-R2-Portal-Answers.pdf` | `CNZ-CreativeFellowship-R2-Portal-Answers.pdf` | Paste-ready answers, reference copy |
| `Ngaika-Smith-CNZ-Creative-Fellowship-Fund-2026-R2-Method-Annex.pdf` | `CNZ-CreativeFellowship-R2-Method-Annex.pdf` | Method annex |
| `Ngaika-Smith-CNZ-Creative-Fellowship-Fund-2026-R2-Accessibility-Evidence.pdf` | `CNZ-CreativeFellowship-R2-Accessibility-Evidence.pdf` | Accessibility evidence |
| `Ngaika-Smith-CNZ-Creative-Fellowship-Fund-2026-R2-Arts-CV.pdf` | `CNZ-CreativeFellowship-R2-CV-Ngaika-Smith.pdf` | Artistic CV |
| `Ngaika-Smith-CNZ-Creative-Fellowship-Fund-2026-R2-Participation-Records.pdf` | `CNZ-CreativeFellowship-R2-People-and-Organisations.pdf` | Participation records |

## Archive

`github.com/LaFinnix/anamata-funding` → `04-in-flight/2026-CNZ-CreativeFellowshipFund-R2/`. The repo gitignores `*.pdf`, so the markdown sources and both build scripts are committed and every PDF is reproducible from them.
