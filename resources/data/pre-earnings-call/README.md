# Pre-earnings-call schemas

A pre-earnings-call schema is a schema version 3 warehouse for one GICS sub-industry, written before a transcript is read. It uses the same layout as an earnings-call warehouse and the same rules in `../model-learnings.md`.

```
pre-earnings-call/<gics-slug>/warehouse/
  directory-manifest.yaml
  yaml/
  MODEL.md
  <slice>/coverage.md
```

Transcript question sheets and call references stay under `../earnings-call/<gics-slug>/`. The owner name matches the earnings-call schema for that slug. No weblinks. One industry does not share a file with another.
