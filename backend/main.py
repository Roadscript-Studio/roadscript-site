from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.models import DemoRequest, DemoResultResponse
from backend.services.demo_service import DemoService


app = FastAPI(title="Roadscript Demo Backend", version="0.1.0")
demo_service = DemoService()

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"https?://(localhost|127\.0\.0\.1)(:\d+)?",
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/demo/embed", response_model=DemoResultResponse)
def embed_demo(request: DemoRequest) -> DemoResultResponse:
    return demo_service.embed_demo(request)
