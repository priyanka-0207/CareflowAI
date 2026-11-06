from fastapi import FastAPI
from patient_repository import *
from models import PatientBasic
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

