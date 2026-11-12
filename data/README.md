# Research data dictionary

This directory contains **two separate, nonrepresentative, partly overlapping documentary collections**, not a pooled dataset of 22 independent articles.

## `diagnostic_claims_12.csv`

One record per selected article/notice comparison. Fields:
- `id`: local article-comparison identifier
- `official_event`: triggering examination and notice context
- `outlet`: publication name
- `article_date`: article date or update note; not a verified immutable snapshot
- `article_url`: link observed during source checking
- `explicit_article_claim_paraphrase`: concise description, not full article text
- `source_comparison_code`: one of the case-level codes below
- `boundary`: which object, scope or stage matters
- `justification`: source-limited rationale
- `confidence_note`: internal uncertainty note, not statistical confidence

**Recorded codes:** eight `ALIGNED`, two `UNWARRANTED_COMPLETION`, one `DIRECT_CONTRADICTION`, one `MIXED_HEADLINE_UPGRADE`.

## `outlet_event_grid_10.csv`

One slot per event × outlet family for two events across five outlet families. Fields:
- `event`, `outlet`, `article_publication_date`, `article_url`
- `page_type`: `STANDALONE`, `ROLLING_LIVE_BLOG` or `NOT_LOCATED`
- `core_outcome_code`: the focal comparison label
- `source_to_claim_rationale`, `coding_confidence`: working coding notes

**Recorded codes:** four `ALIGNED`, three `ALIGNED_WITH_QUALIFIER`, one `DIRECT_CONTRADICTION`, one `ALIGNED_CANNOT_FREEZE`, one `NOT_CODED`. The slot counts are not a measured population-level error rate.

## Interpreting categories

- `DIRECT_CONTRADICTION`: identified official notice explicitly negates the article's focal assertion.
- `UNWARRANTED_COMPLETION`: an article asserts a completed downstream step that the cited notice does not establish; not proof the event never occurred.
- `MIXED_HEADLINE_UPGRADE`: heading and body differ in supported completion stage.
- `ALIGNED`: the focal claim maintains the notice's scope; not proof the entire article is accurate.
- `ALIGNED_WITH_QUALIFIER`: focal claim aligns but ancillary wording warrants caution.
- `ALIGNED_CANNOT_FREEZE`: live-blog post aligns but a stable publication-day snapshot is unavailable.
- `NOT_CODED`: report not located in bounded search; this is not evidence of no publication.

## Integrity check

Run `python tools/verify_corpus.py` from the repository root, or run the tests using `python -m unittest discover -s tests -v`. Both are **structural checks**. They do not adjudicate the truth of articles or government outcomes.

The two files share **four normalized article URLs**. Never add their category counts together as though they were independently sampled. Original source pages are not redistributed or cryptographically archived here.
