from fastapi import FastAPI
import logging
from models.SearchModel import SearchModel
from models.TraversalModel import TraversalModel
from models.SortingModel import SortingModel

from services import binary_search, quick_sort, bfs_traversal
import constants
from utilities import set_up_logging

app = FastAPI()


@app.get("/")
def ping():
    
    return {"Message": " Testing successful"}


@app.post("/v1/binary_search")
def binary_search_algorithm(binary_search_data: SearchModel):
    set_up_logging()
    return binary_search(binary_search_data)

@app.post("/v1/quick_sort")
def quick_sort_algorithm(quick_sort_data: SortingModel):
    set_up_logging()
    return quick_sort(quick_sort_data)

@app.post("/v1/breadth_search_traversal")
def breadth_first_search(traversal_model: TraversalModel):
    set_up_logging()
    return bfs_traversal(traversal_model)


    
    
