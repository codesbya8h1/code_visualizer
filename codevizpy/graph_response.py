from typing import Optional

from pydantic import BaseModel, Field

class CodeGraphResponse(BaseModel):
    name: Optional[str] = Field(default=None, description="name of the method or class from the source code as node")
    connections: Optional[list[str]] = Field(default=None, description="A list of methods/functions being called by another method/class creating edges")
    #TODO: ADD script file name