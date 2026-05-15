from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base


class Appointment(Base):

    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)

    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    patient_id = Column(Integer, ForeignKey("patients.id"))

    date = Column(String)
    time = Column(String)

    status = Column(String, default="Pending")