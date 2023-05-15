from pydantic import BaseModel


class Patient(BaseModel):  # Schema
    id: int
    name: str
    last_name: str
    age: int
    gender: str
