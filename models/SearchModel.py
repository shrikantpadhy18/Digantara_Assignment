from pydantic import BaseModel
from typing import Any

class SearchModel(BaseModel):
    
    array: list[int]
    data: int
    
    
    