import csv
from pathlib import Path

file_path = Path(__file__).resolve().parent / "data" / "patients.csv"

with open(file_path, mode = "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    patient_ids = set()
    total_patient_rows = 0
    for row in reader:
        patient_ids.add(row["Id"])
        total_patient_rows += 1
    unique_patient_ids = len(patient_ids)
    duplicate_patient_ids = total_patient_rows - unique_patient_ids
    print(f"Length : {len(patient_ids)}")
    print(f"Total patient rows: {total_patient_rows}")
    print(f"Unique patient ids: {unique_patient_ids}")
    print(f"Duplicate patient ids: {duplicate_patient_ids}")


def validate_references(file_name, patient_ids):
    file_path = Path(__file__).resolve().parent / "data" / f"{file_name}.csv"

    with open(file_path, mode = "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        total_records = 0
        invalid_references = 0
        for row in reader:
            total_records += 1
            if row["PATIENT"] not in patient_ids:
                invalid_references += 1
        return total_records, invalid_references

total, invalid = validate_references("careplans", patient_ids)
print(total, invalid)
total, invalid = validate_references("encounters", patient_ids)
print(total, invalid)