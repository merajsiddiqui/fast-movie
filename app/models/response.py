from pydantic import  BaseModel

class Response(BaseModel):
    status: int
    error: Dict
    data: Dict