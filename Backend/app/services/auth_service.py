from sqlalchemy.orm import Session
from app.models.user import User
from app.utils.hashing import hash_password, verify_password
from app.utils.token import create_access_token


def register_user(db: Session, user_data):
    user = User(
        name=user_data.name,
        email=user_data.email,
        password=hash_password(user_data.password),
        role=user_data.role
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def login_user(db: Session, user_data):
    user = db.query(User).filter(User.email == user_data.email).first()

    if not user:
        return None

    if not verify_password(user_data.password, user.password):
        return None

    token = create_access_token({
        "id": user.id,
        "role": user.role
    })

    return token