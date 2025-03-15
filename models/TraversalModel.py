from pydantic import BaseModel
from collections import defaultdict
from typing import Dict, List

class TraversalModel(BaseModel):
    graph: Dict[str , List[str]]
    root: str
    
    

    
    
    