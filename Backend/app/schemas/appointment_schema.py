from pydantic import BaseModel


class AppointmentCreate(BaseModel):
    doctor_id: int
    patient_id: int
    date: str
    time: str