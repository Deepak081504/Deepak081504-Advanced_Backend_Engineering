from fastapi import APIRouter, UploadFile, File
import shutil

router = APIRouter(prefix="/upload", tags=["Upload"])


@router.post("/")
def upload_file(file: UploadFile = File(...)):

    allowed = ["image/png", "image/jpeg"]

    if file.content_type not in allowed:
        return {"message": "Invalid File Type"}

    with open(f"app/uploads/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": file.filename}