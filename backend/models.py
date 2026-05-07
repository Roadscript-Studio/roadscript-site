from typing import Literal, Optional

from pydantic import BaseModel, Field

SampleId = Literal["portrait", "architecture", "landscape"]
VerificationStatus = Literal["PASS", "FAIL"]


class DemoImageSet(BaseModel):
    original: str = Field(..., description="URL or path to the original demo image.")
    watermarked: str = Field(..., description="URL or path to the watermarked demo image.")


class DemoMetrics(BaseModel):
    snr: str = Field(..., description="Signal-to-noise ratio display value.")
    utilization: str = Field(..., description="Capacity utilization display value.")
    embed_time: str = Field(..., description="Embed timing display value.")
    verify_time: str = Field(..., description="Extract and verify timing display value.")
    capacity: str = Field(..., description="Capacity display value.")
    message_size: str = Field(..., description="Message size display value.")
    required_bits: str = Field(..., description="Required bits display value.")
    fits: str = Field(..., description="Whether the payload fits the current sample.")


class DemoProfile(BaseModel):
    layout: str
    step: str
    key_mode: str
    prng: str
    haar: str


class DemoRequest(BaseModel):
    sample_id: SampleId = Field(..., description="Selected preset sample.")
    message: Optional[str] = Field(
        default=None,
        description="Optional future payload override. Not used by the mock implementation yet.",
    )


class DemoResultResponse(BaseModel):
    id: SampleId
    label: str
    images: DemoImageSet
    verification: VerificationStatus
    decoded_payload: str
    metrics: DemoMetrics
    profile: DemoProfile
