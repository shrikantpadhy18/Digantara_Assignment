

from pydantic import BaseModel
from typing import Any
import constants
class ResponseModel:
    
    def __init__(self, response: Any, status_code: int, status):
        self.response = response
        self.status = status
        self.status_code = status_code
        
    def get_formatted_output(self):
        
        return{
            constants.STATUS: self.status,
            constants.STATUS_CODE: self.status_code,
            constants.RESPONSE: self.response
        }
    
    
    
