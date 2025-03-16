from models.ResponseModel import ResponseModel
from typing import Optional
import constants
from enums import ResponseStatusEnum
import logging
from typing import Any
from pathlib import Path
from logging.handlers import RotatingFileHandler
from datetime import datetime
import constants

def set_up_logging():
    if constants.ARE_LOG_ENABLED:
        return
    constants.ARE_LOG_ENABLED = True
    handlers = []
    
    log_format = "%(asctime)s - %(levelname)s -  %(filename)s - [line: %(lineno)d] - %(message)s"

    time_stamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    log_dir = Path("logs")
    log_dir.mkdir(parents = True, exist_ok = True)
    
    log_file_path = log_dir/f"{time_stamp}.log"
    log_file_path.touch(exist_ok = True)
    file_handler = RotatingFileHandler(filename = log_file_path, maxBytes = 5000000, backupCount = 2, encoding = "utf-8")
    handlers.append(file_handler)
    
    logging.basicConfig(level = logging.DEBUG, format = log_format, handlers = handlers)

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