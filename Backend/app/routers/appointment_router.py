from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.appointment_schema import AppointmentCreate
from app.services.appointment_service import create_appointment
from app.models.appointment import Appointment

router = APIRouter(prefix="/appointment")

@router.post("/")
def book_appointment(
    appointment: AppointmentCreate,
    db: Session = Depends(get_db)
):

    result = create_appointment(db, appointment)

    if not result:
        raise HTTPException(
            status_code=400,
            detail="Time Slot Already Booked"
        )

    return result


@router.get("/")
def get_appointments(
    status: str = "",
    page: int = 1,
    limit: int = 5,
    db: Session = Depends(get_db)
):

    skip = (page - 1) * limit

    appointments = db.query(Appointment).filter(
        Appointment.status.contains(status)
    ).offset(skip).limit(limit).all()

    return appointments
