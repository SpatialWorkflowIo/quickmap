# AGENTS.md

## Project Snapshot
- `quickmap` is currently a specification-first repo; behavior is defined in `description.md`.
- Core product idea: a one-liner map API, e.g. `quickmap("data.geojson")` (`description.md`).
- Intended output is highly shareable map visualizations (tutorial/blog embedding focus).

## Source of Truth
- Treat `description.md` as the canonical requirements document until code exists.
- Preserve constraints in the "Note to agent" section when adding code/docs.
- Do not remove the `# other` section entries in `.gitignore` (`description.md`, `AGENTS.md`, `.gitignore`).

## Architecture Expectations (Current)
- No runtime package/layout exists yet (`src/`, tests, and build files are absent).
- When scaffolding, keep a minimal Python API centered on a single public entry point: `quickmap(...)`.
- Prefer a thin facade API with mapping backend behind it (Folium or equivalent per `description.md`).

## Developer Workflow Guidance
- No project-specific build/test commands are discoverable yet (no `pyproject.toml`, `requirements.txt`, or `README.md`).
- If you introduce runnable code, add copy-paste quickstart commands to `README.md` immediately.
- Keep examples beginner-friendly and executable from a clean environment.

## Documentation Conventions for This Repo
- Documentation depth is a hard requirement; prioritize clear walkthroughs over terse docs.
- `README.md` should become the primary user guide with examples and quickstart.
- Include one or more links to `https://spatialworkflow.io/` in documentation updates.
- Keep language beginner-friendly for both docs and API usage examples.

## Integration and Publishing Notes
- GitHub operations are expected to target `SpatialWorkflowIo` (see `description.md` lines 30-33).
- If repository automation/scripts are added, avoid assumptions tied to the `gggravity` account.
- SSH host hint for publishing exists in `description.md`; treat it as environment-specific, not app runtime config.

## Agent Operating Rules
- Prefer incremental scaffolding with docs and tests added in the same change.
- Any new convention should be documented in `README.md` and (if agent-facing) mirrored here.
- If requirements conflict, follow explicit statements in `description.md` over inferred best practices.

