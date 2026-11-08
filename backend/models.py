from pydantic import BaseModel
from typing import Optional
from datetime import date

class Patient(BaseModel):
    patient_id: str
    name:str
    age:int
    primary_condition:str
    social_need: Optional[str] = None
    assigned_coordinator: str

class PatientSummary(BaseModel):
    patient_id: str
    first_name: str
    last_name: str
    birthdate: date
    gender: str
    city: str
    state: str
    primary_condition: Optional[str] = None
    active_careplans: int

class PatientBasic(BaseModel):
    patient_id: str
    first_name: str
    last_name: str
    birthdate: date
    gender: str
    city: str
    state: str

class PatientCondition(BaseModel):
    code: str
    description: str
    start_date: str
    end_date: str

class PatientCareplans(BaseModel):
    id: str
    description: str
    start_date: str
    end_date: str
    reason_description: str