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

