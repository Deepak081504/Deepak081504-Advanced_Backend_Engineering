from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.doctor import Doctor
from app.schemas.doctor_schema import DoctorCreate

router = APIRouter(prefix="/doctors", tags=["Doctors"])


@router.post("/")
def create_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):

    new_doctor = Doctor(**doctor.dict())

    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)

    return new_doctor


@router.get("/")
def get_doctors(search: str = "", db: Session = Depends(get_db)):

    doctors = db.query(Doctor).filter(
        Doctor.name.contains(search)
    ).all()

    return doctors