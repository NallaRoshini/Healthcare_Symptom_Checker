from pydantic import BaseModel

class SymptomRequest(BaseModel):
    text: str

class SymptomResponse(BaseModel):
    probable_conditions: str
    recommendations: str
    disclaimer: str
