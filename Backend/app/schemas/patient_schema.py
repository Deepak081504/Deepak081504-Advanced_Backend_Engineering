from pydantic import BaseModel


class PatientCreate(BaseModel):
    name: str
    disease: str