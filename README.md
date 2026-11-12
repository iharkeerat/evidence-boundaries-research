# Evidence Boundaries in Public Examination Reporting

**Documentary research project · Public administration · Evidence provenance · Source-to-claim reasoning**

**Status:** exploratory working study (2026) · **Author-led, AI-assisted** · Not peer-reviewed or independently validated.

> **Central question:** In selected public reports, when are numerical corrections or process-stage announcements presented as changed administrative outcomes, and what source evidence distinguishes warranted statements from overclaims?

Public notices record changes to **particular objects and stages**: a cutoff *table*, an unchanged *candidate list*, a bank-details *submission*, a refund *process*, or a promised *resit*. Reporting may convert one into a stronger downstream outcome. This project examines how to distinguish **an express source contradiction** from an outcome **not established by the identified source**, without pretending the source audit independently verified those administrative events.

## At a glance

| Case | What the official notice establishes | Source-to-claim boundary |
| --- | --- | --- |
| **SSC CGL Tier-I 2025** | The List-III *table* total was corrected from 130,418 to 131,027; SSC said the published candidate list remained unchanged. | One selected article described withheld candidates as newly included, contradicting SSC's express non-effect statement. |
| **NEET-UG 2026** | NTA's July notices counted updated/confirmed or submitted bank details and announced that refunding or processing had begun. | These counts do not independently establish the number of completed payments; selected reports made stronger completion claims. |
| **CUET-UG 2025** | A notice reported 76 affected candidates at one Srinagar centre/shift and promised rescheduling. | A planned remedy is not evidence of completed attendance; selected reports also supply aligned examples. |

**Finding:** The focal cases illustrate an *affected-object transfer* (corrected table ≠ changed list) and a *completion upgrade* (process initiation ≠ completed service). The study does **not** estimate how common these problems are or why journalists wrote particular descriptions.

## Research materials

| Resource | What to expect |
| --- | --- |
| [Research overview](paper/RESEARCH_OVERVIEW.md) | Research question, the three case comparisons, findings and authorship statement |
| [Working report status](report/README.md) | Where the full 10-page report belongs, its current status and release requirements |
| [Methods and codebook](methodology/METHODOLOGY.md) | Unit of analysis, classifications, case selection and evidence limits |
| [Primary-source register](methodology/SOURCE_REGISTER.md) | Four official notices and three focal article links |
| [12 diagnostic comparisons](data/diagnostic_claims_12.csv) | Purposive article-to-notice coding examples |
| [10-slot outlet/event grid](data/outlet_event_grid_10.csv) | Retrospective five-outlet-family × two-event lookup |
| [Data dictionary](data/README.md) | Meaning of columns, status codes and dataset overlap |
| [Structural verifier](tools/verify_corpus.py) | Dependency-free checks of data counts, codes, URLs and overlap |
| [Scope and limitations](LIMITATIONS.md) | What this evidence does and does not substantiate |
| [Authorship and AI disclosure](AUTHORS_AND_AI.md) | Student leadership and material AI assistance |

## Quick reproducibility check

Python 3.10+; no external packages or API keys required for the structural check.

```bash
git clone https://github.com/iharkeerat/evidence-boundaries-research.git
cd evidence-boundaries-research
python tools/verify_corpus.py
python -m unittest discover -s tests -v
```

The verifier checks whether the **supplied files** have the documented structure; it does **not** independently re-check article accuracy, retrieve archived news pages, perform human coding or establish a general media error rate.

## Study design and limitations

The **12-item diagnostic comparison set** is purposive and partly informed by previously noticed concerns. The **10-slot retrospective grid** crosses five outlet families and two events. The collections share **four article URLs**, so they are **not 22 independent reports**. Eight grid slots are standalone articles, one is a changing live blog and one report was not located by the bounded search. No prospective probability sampling or independent adjudication is claimed.

Author review remains necessary for the complete report and focal source classifications. Original publication-day snapshots of news pages were not independently preserved. The source records establish what the issuing agencies **said**, not independently audited refund transfers, candidate rosters or resit attendance. See [limitations](LIMITATIONS.md).

## Originality and prior work

This is a domain-specific **transparent source-to-claim audit**. Provenance, revisions and structured validation have extensive prior art (including W3C PROV-O, DCAT 3 and SHACL). It is not presented as a new general-purpose verification algorithm or as outperforming a careful documentary checklist.

## Attribution, publication and use

**Student author:** Harkeerat Singh. **Research process:** author-led and AI-assisted; source discovery, comparisons, provisional classifications, writing and documentation received material AI help. No second human coder or independent external validation is claimed. See [authorship disclosure](AUTHORS_AND_AI.md). The full working report is **not** an accepted publication.

Third-party sources are **linked and narrowly paraphrased**, not reproduced. No licence is granted over linked articles or official publications. See [rights and reuse](RIGHTS_AND_REUSE.md).

**How to cite:** [CITATION.md](CITATION.md). **Release checklist:** [RELEASE_CHECKLIST.md](RELEASE_CHECKLIST.md).

---

*Evidence boundaries are a question of what a particular record warrants—not a claim that an official notice proves everything that happened afterwards.*
