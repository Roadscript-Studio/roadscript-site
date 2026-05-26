# Roadscript Demo Backend

Minimal FastAPI mock contract for the Roadscript website demo.

This backend is intentionally small:
- no database
- no uploads
- no auth
- no queues
- mock responses only

Its job right now is to define the API contract that `demo.html` can talk to, so the current static demo can evolve into a real watermark pipeline later.

The deployed website does not depend on this backend today. `demo.html` uses frontend mock data by default, and this
FastAPI app remains the local development and future integration contract.

## Files

- `main.py`
  FastAPI app, CORS config, API routes
- `models.py`
  Typed request and response models
- `services/demo_service.py`
  Mock demo service that returns structured sample results
- `services/mock_samples.py`
  Centralized mock response catalog used by the website demo

## Run locally

From the repo root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
uvicorn backend.main:app --reload
```

The API will be available at:

- `http://127.0.0.1:8000/api/health`
- `http://127.0.0.1:8000/api/demo/embed`

## Local frontend testing

The demo frontend should be served from a localhost HTTP server during development.

In a second terminal, from the repo root:

```bash
python3 -m http.server 8080
```

Then open:

- `http://127.0.0.1:8080/demo.html`

### Important note about `file://`

Do not open `demo.html` directly from disk with a `file://` URL for backend testing.

Because the backend CORS setup allows localhost development origins, opening the page directly from the filesystem may produce fetch or CORS-related issues due to the browser using a `null` origin.

## Frontend integration

`demo.html` can post the selected preset sample to:

```text
POST /api/demo/embed
```

Example request:

```json
{
  "sample_id": "portrait"
}
```

The response mirrors the current demo result structure:

```json
{
  "id": "portrait",
  "label": "Portrait",
  "images": {
    "original": "assets/demo/portrait-original.png",
    "watermarked": "assets/demo/portrait-watermarked.png"
  },
  "verification": "PASS",
  "decoded_payload": "hello",
  "metrics": {
    "snr": "64.48 dB",
    "utilization": "0.41%",
    "embed_time": "181.99 ms",
    "verify_time": "213.72 ms",
    "capacity": "23625 bits",
    "message_size": "5 bytes",
    "required_bits": "96",
    "fits": "yes"
  },
  "profile": {
    "layout": "center-ring",
    "step": "30",
    "key_mode": "none",
    "prng": "Roadscript PRNG v1",
    "haar": "Roadscript Haar v1"
  }
}
```

By default, the deployed website uses frontend mock responses from `scripts/demoMockData.js`.

To re-enable backend mode later:

1. Set `USE_FRONTEND_MOCK_DATA = false` near the top of the `demo.html` script.
2. Ensure `window.DEMO_API_BASE` points at the backend host, or keep the default:
   - `http://127.0.0.1:8000`

If needed, the frontend API base can be overridden before the demo script runs:

```html
<script>
  window.DEMO_API_BASE = "http://127.0.0.1:8000";
</script>
```

## Where real engine integration will happen

When the real backend phase begins, replace the mock logic in `services/demo_service.py`.

Planned integration points:
- invoke CLI subprocesses such as `rse embed` and `rse verify`
- or call direct native engine bindings
- normalize raw engine outputs into the existing `DemoResultResponse` shape

That keeps the frontend contract stable while the implementation behind it becomes real.
