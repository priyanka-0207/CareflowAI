from fastapi import FastAPI
from patient_repository import *
from models import *
from fastapi import *

app = FastAPI(title = "CareFlow AI")

@app.get("/health")
def health_check():
    return{
        "status":"ok",
        "project":"CareFlow AI"
    }

@app.get("/patients", response_model=list[PatientBasic])
def get_patients():
    return get_all_patients()

@app.get("/patients/{patient_id}", response_model=PatientBasic)
def get_patient_by_details(patient_id: str):
    patient = get_patient_by_id(patient_id)
    if patient_id is None:
        raise HTTPException(
            status_code = 404,
            detail="Patient not found"
        )
    return patient

@app.get("/patients/{patient_id}/conditions", response_model=list[PatientCondition])
def get_conditions(patient_id: str):
    if patient_id is None:
        raise HTTPException(
            status_code = 404,
            detail="Patient not found"
        )
    return get_patient_conditions(patient_id)

@app.get("/patients/{patient_id}/careplans", response_model=list[PatientCareplans])
def get_careplans(patient_id: str):
    patient = get_patient_by_id(patient_id)
    if patient is None:
        raise HTTPException(
            status_code= 404,
            detail= "Patient not found"
        )
    return get_patient_careplans(patient_id)
