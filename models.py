from pydantic import BaseModel, Field
from utils import PyObjectId
from typing import Optional, List


class Dino(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str
    description: str
    image: str
    diet: str
    live: str
    found: str
    type: str
    length: str
    color: str


class DinoCollection(BaseModel):
    dinos: List[Dino]
