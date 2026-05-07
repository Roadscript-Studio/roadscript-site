from backend.models import DemoRequest, DemoResultResponse


class DemoService:
    """Mock demo service that mirrors the frontend demo contract.

    TODO:
    - Replace static sample lookup with real engine orchestration.
    - Support subprocess-based integration for `rse embed` / `rse verify`.
    - Support direct native bindings once the engine is exposed as a library.
    """

    def __init__(self) -> None:
        self._samples = {
            "portrait": DemoResultResponse.model_validate(
                {
                    "id": "portrait",
                    "label": "Portrait",
                    "images": {
                        "original": "assets/demo/portrait-original.png",
                        "watermarked": "assets/demo/portrait-watermarked.png",
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
                        "fits": "yes",
                    },
                    "profile": {
                        "layout": "center-ring",
                        "step": "30",
                        "key_mode": "none",
                        "prng": "Roadscript PRNG v1",
                        "haar": "Roadscript Haar v1",
                    },
                }
            ),
            "architecture": DemoResultResponse.model_validate(
                {
                    "id": "architecture",
                    "label": "Architecture",
                    "images": {
                        "original": "assets/demo/architecture-original.png",
                        "watermarked": "assets/demo/architecture-watermarked.png",
                    },
                    "verification": "PASS",
                    "decoded_payload": "arch",
                    "metrics": {
                        "snr": "63.91 dB",
                        "utilization": "0.57%",
                        "embed_time": "194.83 ms",
                        "verify_time": "221.14 ms",
                        "capacity": "23625 bits",
                        "message_size": "4 bytes",
                        "required_bits": "88",
                        "fits": "yes",
                    },
                    "profile": {
                        "layout": "center-ring",
                        "step": "28",
                        "key_mode": "none",
                        "prng": "Roadscript PRNG v1",
                        "haar": "Roadscript Haar v1",
                    },
                }
            ),
            "landscape": DemoResultResponse.model_validate(
                {
                    "id": "landscape",
                    "label": "Landscape",
                    "images": {
                        "original": "assets/demo/landscape-original.png",
                        "watermarked": "assets/demo/landscape-watermarked.png",
                    },
                    "verification": "PASS",
                    "decoded_payload": "vista",
                    "metrics": {
                        "snr": "65.12 dB",
                        "utilization": "0.49%",
                        "embed_time": "176.42 ms",
                        "verify_time": "209.37 ms",
                        "capacity": "23625 bits",
                        "message_size": "5 bytes",
                        "required_bits": "96",
                        "fits": "yes",
                    },
                    "profile": {
                        "layout": "center-ring",
                        "step": "32",
                        "key_mode": "none",
                        "prng": "Roadscript PRNG v1",
                        "haar": "Roadscript Haar v1",
                    },
                }
            ),
        }

    def embed_demo(self, request: DemoRequest) -> DemoResultResponse:
        # TODO: Run the real watermark embed and verify pipeline here.
        # This will eventually translate the request into engine calls and normalize
        # the raw engine output into the DemoResultResponse contract.
        result = self._samples[request.sample_id]

        if request.message:
            # Keep this small and explicit for Phase 2. The mock endpoint echoes
            # the requested payload shape without pretending to run the engine.
            result = result.model_copy(update={"decoded_payload": request.message})

        return result
