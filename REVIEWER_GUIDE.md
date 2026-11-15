# Two-minute reviewer guide — Evidence Boundaries

**Project type:** exploratory, author-led and materially AI-assisted documentary research. **Status:** working study; not peer reviewed, independently adjudicated or a validated automated fact-checking system.

## Central question

When official examination notices record a corrected number or the beginning of an administrative process, what exactly do they establish—and when does later reporting overstate a downstream outcome?

## Evidence and examples

The [research overview](paper/RESEARCH_OVERVIEW.md) examines three selected contexts:

- **SSC CGL Tier-I 2025:** the official correction concerns a published aggregate table; the notice says the candidate list did not change. One selected secondary account states a stronger list-change proposition.
- **NEET-UG 2026:** updated bank details and initiated refund processing do **not** alone establish completed payments. The project does **not** independently verify bank transfers.
- **CUET-UG 2025:** announcing a rescheduled session does not establish its later completion or attendance.

**Method:** compare the exact object, stage, date and population in the primary notice with a selected reporting claim. Label a direct contradiction separately from a proposition merely unsupported by that notice.

## What is inspectable now

| Resource | Purpose |
| --- | --- |
| [Methodology and codebook](methodology/METHODOLOGY.md) | Classification rules and case-selection limitations |
| [Source register](methodology/SOURCE_REGISTER.md) | Primary notices and focal articles |
| [Diagnostic comparisons](data/diagnostic_claims_12.csv) | Twelve purposively selected examples |
| [Outlet/event grid](data/outlet_event_grid_10.csv) | Ten retrospective lookup slots, not an independent probability sample |
| [Limitations](LIMITATIONS.md) | Biases, missing publication-day archives and evidentiary boundaries |
| [Authorship/AI assistance](AUTHORS_AND_AI.md) | Roles, validation gaps and responsibility |
| [Report release status](report/README.md) | Why the complete report PDF has not yet been publicly uploaded |

**Do not sum the two datasets as 22 independent articles:** four article URLs overlap.

## Repeat the structural checks

From the repository root with Python 3.10+:

    python tools/verify_corpus.py
    python -m unittest discover -s tests -v

These checks verify the *stored tables and declared structure*, not source truth, original-page timing, human annotations or real-world administrative outcomes.

## What remains before using it as a finished research report

The student author should personally reopen focal government notices and disputed article links, confirm the exact wording and dates, review both CSVs and the full PDF, and sign off on the claims and AI disclosure. No independent second-coder, prospective probability sample or published error-rate estimate is claimed. The full report should be added only after author review and rights/privacy checks.

**Suggested path for an internship evaluator:** [research overview](paper/RESEARCH_OVERVIEW.md) → [methodology](methodology/METHODOLOGY.md) → [source register](methodology/SOURCE_REGISTER.md) → [coded tables](data/README.md) → [limitations](LIMITATIONS.md).
