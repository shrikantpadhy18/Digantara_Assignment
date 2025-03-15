
from pydantic import BaseModel


class SortingModel(BaseModel):
    array: list[int]
    