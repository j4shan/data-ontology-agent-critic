# Agent instructions

## Requirements

`project_metadata/product/` is the only authoritative source of product requirements and design
decisions. Read them there. Do not restate, extend, or record them in agent instruction files;
plans under `project_metadata/plans/` are working notes, not requirements.

## Configuration

The actor location, artifact location, and socket path are configurable inputs. Never hardcode
them.

## Domain file layout

An authored file belongs to one business domain; never mix domains in one file.

- Schema-candidate catalogs and the question sheet (`questions.md`) live under
  `project_metadata/schema_candidates/<domain>/`.
- Suites and reference answers live in per-domain directories.
- Do not add an assessment domain without explicit direction.
