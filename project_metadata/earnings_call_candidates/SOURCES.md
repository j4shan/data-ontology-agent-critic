# Earnings-call transcript sources

These candidates are not assessment domains. They are a provenance pool for later ontology
experiments. Question files paraphrase analyst questions. They do not store transcript text.

## Primary source

**The Motley Fool earnings-call transcript archive**

- Index: https://www.fool.com/earnings-call-transcripts/
- Article pattern: `https://www.fool.com/earnings/call-transcripts/{year}/{month}/{day}/{slug}/`
- Coverage used here: U.S. earnings calls, including S&P 500 names, with speaker-labeled Q&A.
- Access: public HTML pages. No account was required for the calls fetched in this pass.
- Discovery query: `site:fool.com/earnings/call-transcripts {TICKER} earnings call transcript`
- Selection rule: the four most recent dated transcripts for that ticker. Fiscal labels on the
  page decide order when the URL date and the fiscal period disagree.

Fool pages are the source of record for a call when both Fool and a fallback carry it.

## Fallback source

**MarketBeat earnings-report pages**, transcript body credited to Quartr.

- Company earnings index: `https://www.marketbeat.com/stocks/{EXCHANGE}/{TICKER}/earnings/`
- Report pattern: `https://www.marketbeat.com/earnings/reports/{YYYY-MM-DD}-{company-slug}-stock/`
- Use a MarketBeat page only when Fool has fewer than four recent calls for that company.
- Do not prefer MarketBeat over an available Fool transcript for the same event.

## Sources considered and not used for extraction

| Source | Why it is not the fetch path |
| --- | --- |
| Seeking Alpha | U.S. transcripts exist, and full text generally requires a paid subscription. |
| Koyfin | Free plan is a short recent window and is not a stable page-per-call archive. |
| Quartr | First-party audio and transcripts, primarily through an app rather than a stable public URL. |
| Company investor-relations sites | Prepared remarks, slides, and audio are common. Full analyst Q&A is inconsistent. |
| SEC EDGAR 8-K exhibits | Some issuers file prepared remarks or a transcript. Coverage of live analyst Q&A is uneven, so EDGAR is not the primary fetch. |
| Financial Modeling Prep, Alpha Vantage, and similar APIs | Transcript endpoints require an API key that this workspace does not have. |

## What is persisted

Each company file records the call date, fiscal period, source name, and URL, plus a paraphrase of
each analyst question that asks for a business comparison, driver, mix, outlook, or exception.
Verbatim questions and prepared remarks stay on the source site.
