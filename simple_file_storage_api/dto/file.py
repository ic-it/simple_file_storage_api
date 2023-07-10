from pydantic import BaseModel
from uuid import UUID


class File(BaseModel):
    id: UUID
