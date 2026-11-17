from pydantic import BaseModel

class CreateEntry(BaseModel):
    content: str

class EntriesResponse(BaseModel):
    id: int
    content: str
    created_at: str
