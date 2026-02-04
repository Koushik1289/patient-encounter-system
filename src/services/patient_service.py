from fastapi import HTTPException
<<<<<<< HEAD
from sqlalchemy.orm import Session
=======
>>>>>>> 577784b7a45da4ba89f09b33f249607d8f4c0e43
from src.models.patient import KoushikPatient as Patient


def create_patient(db: Session, data):
    existing = db.query(Patient).filter(Patient.email == data.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")

    patient = Patient(**data.dict())
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient


def get_patient(db: Session, patient_id: int):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient
