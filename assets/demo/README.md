# Demo Assets

This directory contains the recruiter-facing sample media used by `demo.html` and the mock FastAPI backend.

The demo expects the following files:

- `portrait-original.png`
- `portrait-watermarked.png`
- `architecture-original.png`
- `architecture-watermarked.png`
- `landscape-original.png`
- `landscape-watermarked.png`

The current set is intentionally sample-driven and procedurally generated for a clean local preview. Each
`*-watermarked.png` variant is visually near-identical to its paired original so the demo can communicate
non-destructive watermarking without implying production engine execution.

If these files are absent, `demo.html` falls back to a deliberate missing-image state instead of showing broken browser placeholders.
