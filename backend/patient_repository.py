import csv
from pathlib import Path
from datetime import datetime

def get_all_patients():
    file_path = Path(__file__).resolve().parent / "data" / "patients.csv"
    with open(file_path, mode = "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        patients = []
        for row in reader:
            patients.append(
                {
                "patient_id" : row["Id"],
                "first_name" : row["FIRST"],
                "last_name" : row["LAST"],
                "birthdate": datetime.strptime(row["BIRTHDATE"], "%m/%d/%Y").date(),
                "gender" : row["GENDER"],
                "city" : row["CITY"],
                "state" : row["STATE"]
            }
            )
        return patients

if __name__ == "__main__":
    result = get_all_patients()
    print(len(result))
    print(result[0].keys())

def get_patient_by_id(patient_id):
    patients = get_all_patients()
    for patient in patients:
        if patient["patient_id"] == patient_id:
            return patient
    return None

if __name__ == "__main__":
    patients = get_all_patients()

    existing_id = patients[0]["patient_id"]

    print(get_patient_by_id(existing_id))
    print(get_patient_by_id("nonexistent-id"))

def get_patient_conditions(patient_id):
    conditions = []
    file_path = Path(__file__).resolve().parent / "data" / "conditions.csv"
    with open(file_path, mode = "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["PATIENT"] == patient_id:
                conditions.append({
                    "code": row["CODE"],
                    "description": row["DESCRIPTION"],
                    "start_date": row["START"],
                    "end_date": row["STOP"]
                })
        return conditions


if __name__ == "__main__":
    patients = get_all_patients()
    patient_id = patients[0]["patient_id"]

    conditions = get_patient_conditions(patient_id)

    print("Patient ID:", patient_id)
    print("Conditions found:", len(conditions))
    print("First condition:", conditions[0] if conditions else "None")

    print("Unknown patient:", get_patient_conditions("unknown-id"))

def get_patient_careplans(patient_id):
    careplans = []
    file_path = Path(__file__).resolve().parent / "data" / "careplans.csv"
    with open(file_path, mode = "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["PATIENT"] == patient_id:
                careplans.append({
                    "id": row["Id"],
                    "description": row["DESCRIPTION"],
                    "start_date": row["START"],
                    "end_date": row["STOP"],
                    "reason_description": row["REASONDESCRIPTION"]
            })
        return careplans