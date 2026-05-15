from sqlalchemy.orm import Session
from app.models.appointment import Appointment


def create_appointment(db: Session, appointment_data):

    existing = db.query(Appointment).filter(
        Appointment.doctor_id == appointment_data.doctor_id,
        Appointment.date == appointment_data.date,
        Appointment.time == appointment_data.time
    ).first()

    if existing:
        return None

    appointment = Appointment(**appointment_data.dict())

    db.add(appointment)
    db.commit()
    db.refresh(appointment)

    return appointment