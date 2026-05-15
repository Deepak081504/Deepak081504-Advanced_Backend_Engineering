import shutil
from app.models.file import File


def save_file(db, uploaded_file):

    file_location = f"app/uploads/{uploaded_file.filename}"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)

    new_file = File(
        filename=uploaded_file.filename,
        filetype=uploaded_file.content_type,
        filepath=file_location
    )

    db.add(new_file)
    db.commit()
    db.refresh(new_file)

    return new_file