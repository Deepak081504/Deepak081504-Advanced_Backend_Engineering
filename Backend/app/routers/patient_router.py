from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.patient import Patient
from app.schemas.patient_schema import PatientCreate

router = APIRouter(prefix="/patients", tags=["Patients"])


@router.post("/")
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):

    new_patient = Patient(**patient.dict())

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return new_patient