from fastapi import FastAPI

from app.database import Base, engine

from app.routers.auth_router import router as auth_router
from app.routers.doctor_router import router as doctor_router
from app.routers.patient_router import router as patient_router
from app.routers.appointment_router import router as appointment_router
from app.routers.upload_router import router as upload_router

from app.models.user import User
from app.models.doctor import Doctor
from app.models.patient import Patient
from app.models.appointment import Appointment
from app.models.file import File

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(auth_router)
app.include_router(doctor_router)
app.include_router(patient_router)
app.include_router(appointment_router)
app.include_router(upload_router)


@app.get("/")
def home():
    return {
        "message": "Hospital Management System Running"
    }