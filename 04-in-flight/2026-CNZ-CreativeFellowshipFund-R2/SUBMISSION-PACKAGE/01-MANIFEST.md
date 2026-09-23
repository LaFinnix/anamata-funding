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
| 02 | `02-CNZ-CreativeFellowship-R2-Portal-Answers.pdf` | 4 | The executive summary and the five answers, with character and word counts per field | Paste into the portal fields. The `.txt` version is the raw paste source |
| 03 | `03-CNZ-CreativeFellowship-R2-Somatosensory.pdf` | 6 | The application as a document: at a glance, the five answers, twelve month timeline, budget ledger, collaborators | Support material, if the form takes an upload |
| 04 | `04-CNZ-CreativeFellowship-R2-Accessibility-Evidence.pdf` | 3 | What the 2026 Development Fund programme is, what is publicly verifiable, what is ongoing, what does not exist yet | Support material for the accessibility claims |
| 05 | `05-CNZ-CreativeFellowship-R2-Method-Annex.pdf` | 8 | The practice brief (rig, twelve phase one tests, session architecture, phase alignment, roles) and tactile notation v0.1 | Support material for the method the application claims |

Working files behind them: `06-PORTAL-ANSWERS.txt` (raw paste text), `07-APPLICATION-full.md` (answers plus timeline, budget and collaborator annexes, and the internal correct-these list), `08-SUBMIT-CHECKLIST.md`, `09-FIRST-CONTACT-EMAILS.md`, `10-COLLABORATOR-SHORTLIST.md`, `11-ACCESSIBILITY-PROGRAMME-EVIDENCE.md`, `12-PRACTICE-BRIEF.md`, `13-TACTILE-NOTATION.md`.

All four PDFs render through one design system: A4, Liberation Serif, crescent letterhead with the entity line, kōkōwai used for the wordmark and kicker only, booktabs tables with hairline rules, page numbers in the footer. No em dashes, no emoji, no sans-serif body. Rebuild with `build/build_pdfs.py`, which writes both the source markdown and the PDF.

## Counts, verified against the pasted text

| Field | Characters | Words |
|---|---|---|
| Executive summary | 944 | 155 |
| Question 1 | 2,366 | 404 |
| Question 2 | 2,436 | 397 |
| Question 3 | 2,199 | 394 |
| Question 4 | 2,162 | 347 |
| Question 5 | 2,248 | 393 |

Question 5 grew nine characters when the collective name was corrected, and the caption in `PORTAL-ANSWERS.txt`, the count table in `APPLICATION.md` and the checklist table were all updated to match. The counts in the PDF are computed from the text that is pasted, not copied from a caption.

## Naming audit

| Finding | Action |
|---|---|
| "Anamata Kāhui" used for the collective in the first contact emails, and "Anamata" alone in the closing paragraph of Question 5 | Corrected to **Te Kāhui Anamata** everywhere the collective is named |
| Letterhead entity line and footer in every PDF | Now read Te Kāhui Anamata |
| "Anamata Kāhui Limited" as the registered company | Left as is in seven places, being where the company is the applicant or the trading entity. That is the name on the register (NZBN 9429052960734, company 9350922). Say the word if the register name itself has changed and all seven change with it |

## Gaps I cannot close without you

| Item | State |
|---|---|
| **Artistic CV** | Not written. The fund asks for it. I can draft it from the verified record inside an hour, but the training, roles, awards and dates are yours |
| **Samples of work** | Exist, not picked. Three links need choosing from the released catalogue |
| **Letters of support** | None obtained. Two are worth asking for: Maurea on cultural process, and a Deaf arts partner or Arts Access Aotearoa on the collaboration structure |
| **Te reo title sign-off** | Outstanding. Recommendation stands: Ngā Wiri o te Tinana, subtitle stopping at vibrotactile waiata |
| **Collaborator names** | None named, because none has been approached. The application discloses selection within 30 days of award |
| **Six waiata** | Referenced without names. Send the slate and the answers get specific |
| **Hardware quotes** | The $6,800 line is a planning envelope, labelled indicative in the method annex and backed by a quote plan (who is asked, what is asked, due before purchase). No figure is claimed as a price |

## Revision, 24 September, after review

The method annex was reviewed and revised. Vest routing and latency (analog or USB path, Bluetooth not
accepted as the scored path, latency measured and logged), vibration exposure referenced to ISO 2631-1 and
ISO 5349-1 with accelerometer measurement, participant care (screening, informed consent naming the sensory
experience, opt out at any point, fees for time, CARE-based data sovereignty, cultural review of the protocol
before the first session), a hardware quote plan, a specific phase alignment method with a five millisecond
residual target, a cross-channel simultaneity rule in the notation, and a proposed te reo column on the body
location codes with three terms deliberately left open for the reviewer.

## Two integrity checks before this goes in

1. **The Maurea relationship.** The application, the platform accessibility page and the funded programme's partner file all describe cultural review with Maurea dating from 2024. If the first contact email is genuinely first contact, that wording is wrong in three places and needs changing today.
2. **Programme end date.** The delivery schedule puts final report and acquittal in June 2027; the application cites December 2026 and February 2027 work from that programme.

## Archive

`github.com/LaFinnix/anamata-funding` → `04-in-flight/2026-CNZ-CreativeFellowshipFund-R2/`.
