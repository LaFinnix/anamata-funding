# anamata-funding — Methodology

**Author:** Ngaika Smith (ORCID [0009-0002-1952-7454](https://orcid.org/0009-0002-1952-7454))
**Affiliation:** Anamata Kāhui Limited — [anamatakahui.co.nz](https://anamatakahui.co.nz)
**Version:** 1.0
**Date:** 2026-08-18
**Status:** Public — citable.

---

## Citation

```bibtex
@techreport{smith_anamata_funding_methodology_2026,
  author      = {Smith, Ngaika},
  title       = {anamata-funding: Methodology for prioritising funding applications in iwi/hapu contexts},
  institution = {Anamata Kāhui Limited},
  year        = {2026},
  version     = {1.0},
  url         = {https://github.com/LaFinnix/anamata-funding/blob/main/METHODOLOGY.md},
}
```

## 1. Scope

This document describes the method used by `anamata-funding` to identify, prioritise, and prepare funding applications for Anamata Kāhui Limited and affiliated iwi/hapū. The methodology has three parts: **landscape mapping**, **opportunity shortlisting**, and **application preparation**.

## 2. Landscape mapping

`00-funding-landscape/` catalogues the verified-live NZ funding family relevant to iwi/hapū applicants. Each entry records:

- Funder name and programme
- Round window (open/closed dates)
- Eligibility criteria (iwi registration, charitable status, sector scope, dollar band)
- Required artefacts (financial statements, governance attestations, tikanga submissions)
- Past submission outcomes (where available)

The landscape is reviewed on a rolling basis and refreshed at minimum quarterly. Stale entries (closed rounds, defunct programmes) are archived but not deleted.

## 3. Opportunity shortlisting

`03-research/OPPORTUNITY-SHORTLIST-*.md` records the prioritisation process. Each opportunity is scored 0-3 on four dimensions:

| Dimension | Tests |
|---|---|
| **F1 - Funder fit** | Is there a verified-live funder with a current open round whose scope matches this? Named programme + verified round window. |
| **F2 - Eligibility certainty** | Are the eligibility criteria unambiguous? Does Anamata Kāhui / the named iwi clearly meet them? |
| **F3 - Capacity fit** | Can we deliver the funded activity within the 2-8 week shipping window with current resourcing? |
| **F4 - Mana return** | Does the funded activity advance cultural, environmental, or iwi-self-determination outcomes beyond the dollar value? |

Only opportunities scoring **>=9 / 12** make the shortlist. The rubric is deliberately conservative — the cost of an unsuccessful application (iwi reputation, time, narrative exhaustion) outweighs the marginal upside of a low-probability submission.

## 4. Application preparation

`01-templates/` carries the boilerplate, style guide, and tikanga submission templates. Each past application in `02-past-applications/` is archived with:

- The full submitted text
- The funder's response (received, declined, successful)
- A post-mortem on what worked and what didn't
- The dollar amount and reporting obligations (where successful)

This archive is the institutional memory. Future applications build directly on what has succeeded.

## 5. Cultural protocol

Applications that reference iwi or hapū require **iwi consultation before submission**, not after. The consultation protocol is:

1. Draft circulated to the named iwi/hapū contact at least 14 days before submission.
2. Comments received and incorporated or responded to in writing.
3. The final submitted text is the agreed version, not the Anamata Kāhui author's first draft.

This is a hard rule, not a courtesy. Submitting an application that names an iwi without their prior agreement damages the relationship beyond the value of any individual grant.

## 6. Limitations

- The landscape is NZ-specific. The method does not generalise to non-NZ funders without extension.
- The prioritisation rubric is opinionated — it assumes the Anamata Kāhui operating context (small team, 2-8 week shipping window, multi-vertical platform). Other organisations should re-weight the dimensions.
- Past outcomes are N=3 in the current archive (CNZ, NZ On Air, Tindall). The base rate is too small to draw strong conclusions about what "works".

## 7. Versioning

- **v1.0** (2026-08-18) — initial public methodology statement. Aligns with the Anamata Kāhui platform documentation standards.

---

**Author contact:** Ngaika Smith · ngaika@anamatakahui.co.nz
**Repository:** https://github.com/LaFinnix/anamata-funding
**License of this document:** CC-BY-4.0 (intentionally more permissive than the code, since the methodology itself is meant to be reused).
