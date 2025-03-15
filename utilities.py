from models.ResponseModel import ResponseModel
from typing import Optional
import constants
from enums import ResponseStatusEnum
import logging
from typing import Any

def check_if_array_is_empty(input_array: list, operation_name: Any) -> tuple[Optional[ResponseModel],bool]:
    
    if input_array == []:
        response = f"{operation_name} cant be applied as the provided input is empty"
        logging.info(response)
            
        response_model = ResponseModel(status_code = constants.BLANK_INPUT_CODE, status = ResponseStatusEnum.FAILURE, response = response)
            
        return response_model, True
    
    return None, False

def check_if_input_array_is_unsorted(input_array: list):
    
    if input_array != sorted(input_array):
        response = f"Binary Search cant be applied as the provided input is not sorted"
        logging.info(response)
            
        response_model = ResponseModel(status_code = constants.INVALID_INPUT, status = ResponseStatusEnum.FAILURE, response = response)
            
        return response_model, True
    
    return None, False