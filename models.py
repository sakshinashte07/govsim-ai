from pydantic import BaseModel

class Observation(BaseModel):
    pollution: float
    economy: float
    satisfaction: float
    month: int

class Action(BaseModel):
    tax: float
    subsidy: float
    regulation: float