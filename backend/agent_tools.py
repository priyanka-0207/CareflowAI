from patient_repository import *

def lookup_patient_conditions(patient_id: str):
    return get_patient_conditions(patient_id)

def lookup_patient_careplans(patient_id: str):
    return get_patient_careplans(patient_id)