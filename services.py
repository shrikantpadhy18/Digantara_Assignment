
from models.SearchModel import SearchModel
import logging 
from models.ResponseModel import ResponseModel
from models.SortingModel import SortingModel
from models.TraversalModel import TraversalModel
import constants
from enums import ResponseStatusEnum
from utilities import check_if_array_is_empty, check_if_input_array_is_unsorted

def binary_search(input: SearchModel) -> ResponseModel:
    
    try:
        
        input_array = input.array
        data_to_be_searched = input.data
        logging.info(f"Binary Search Algorithm Invoked on following array: {input_array} and data to be found: {data_to_be_searched}")
        response_model, is_empty_array = check_if_array_is_empty(input_array, binary_search.__name__)
        
        if is_empty_array:
            return response_model
        
        response_model, is_unsorted_array = check_if_input_array_is_unsorted(input_array)
        
        if is_unsorted_array:
            return response_model
        
        logging.info("Binary Search Algorithm Completed")
        return bin_search_helper(input_array, data_to_be_searched)
    
    except Exception as e:
        logging.exception(" The Exception occured as %s", e)
    

def bin_search_helper(array: list, data_to_be_searched: int):
    
    low = 0
    high = len(array) - 1
    
    while high - low > 1:
        
        mid = low + (high - low)//2
        
        if array[mid] > data_to_be_searched:
            high = mid - 1
            
        else:
            low = mid
            
    response = f"Data Not Found"
    
    if array[low] == data_to_be_searched:
        response = f"{data_to_be_searched} found at index {low}"
    
    if array[high] == data_to_be_searched:
        response = f"{data_to_be_searched} found at index {high}"
        
    return  ResponseModel(status_code = constants.SUCCESS_CODE, status = ResponseStatusEnum.SUCCESS, response = response)
        
            
                
def quick_sort(input: SortingModel) -> ResponseModel:
    
    try:
        input_array = input.array
        quick_sort_helper(input_array,0,len(input_array) - 1)
        logging.info(f"Quick Sort Algorithm Started on input array: {input_array}")
        
        response = f" Following is the sorted array using Quick Sort Algorithm {input_array}"
        
        
        return ResponseModel(status_code = constants.SUCCESS_CODE, status =  ResponseStatusEnum.SUCCESS, response = response)
                
        
    except Exception as e:
        logging.exception(f"The Exception occurred in {quick_sort.__name__} function ", e)
        
        
    
def quick_sort_helper(array: list, start: int, end: int):
    if start >= end:
        return
    
    pivot_index = partition(array, start, end)
    quick_sort_helper(array, start, pivot_index - 1)
    quick_sort_helper(array, pivot_index + 1, end)
    

def partition(array: list, start: int, end: int):
    
    pivot_element = array[end]
    
    i = start - 1
    
    for j in range(start, end):
        
        if array[j] >  pivot_element:
            pass
        else:
            i += 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            
            
    i += 1
    temp = array[i]
    array[i] = array[end]
    array[end] = temp
    
    return i
    
    
def bfs_traversal(input:TraversalModel) -> ResponseModel:
    
    try:
        graph = input.graph
        root = input.root
        response_model, is_empty_array = check_if_array_is_empty(graph, bfs_traversal.__name__)
        
        if is_empty_array:
            return response_model
        
        
        
        answer = bfs_algorithm(graph, root)
        
        response = f" Following is the output array using bfs traversal algorithm:  {answer}"
        
        return ResponseModel(status_code = constants.SUCCESS_CODE, status =  ResponseStatusEnum.SUCCESS, response = response)
        
    except Exception as e:
        logging.exception("The Exception occurred in bfs_traversal %s", e)
        


def bfs_algorithm(graph: dict[str, list], root: str):
    
    queue = [root]
    
    answer = []
    visited = set()
    visited.add(root)
    while queue != []:
        
        size = len(queue)
        nodes_at_same_level = []
        
        while size > 0:
            node = queue.pop(0)
            nodes_at_same_level.append(node)
            
            for adjacent_node in graph.get(node, []):
                if adjacent_node not in visited:
                    visited.add(adjacent_node)
                    
                    queue.append(adjacent_node)
            size-= 1
            
        answer.append(nodes_at_same_level)
        
    return answer
                