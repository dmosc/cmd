from typing import List
from pydantic import BaseModel


class CommandFlag(BaseModel):
    name: str
    value: str

class CommandModel(BaseModel):
    description: str
    full_command: str
    flags: List[CommandFlag]