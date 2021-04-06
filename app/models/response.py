from pydantic import BaseModel
from typing import Dict, Optional


class Response(BaseModel):
    error:  Optional[Dict] = None
