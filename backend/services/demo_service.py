from backend.models import DemoRequest, DemoResultResponse
from backend.services.mock_samples import MOCK_DEMO_RESULTS


class DemoService:
    """Mock demo service that mirrors the website demo contract."""

    def __init__(self) -> None:
        self._samples = MOCK_DEMO_RESULTS

    def embed_demo(self, request: DemoRequest) -> DemoResultResponse:
        # Future integration point: replace mock sample lookup with real engine execution
        # and normalize the resulting embed/verify output into DemoResultResponse.
        result = self._samples[request.sample_id]

        if request.message:
            # Keep this small and explicit for Phase 2. The mock endpoint echoes
            # the requested payload shape without pretending to run the engine.
            result = result.model_copy(update={"decoded_payload": request.message})

        return result
