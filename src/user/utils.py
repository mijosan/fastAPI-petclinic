from fastapi import HTTPException
import jwt
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from pydantic import ValidationError

SECRET_KEY = "secret_key"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)
    
def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(tz = timezone.utc) + timedelta(minutes=15)
        
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except (jwt.PyJWTError, ValidationError):
        raise HTTPException(
            status_code=401, detail="Could not validate credentials"
        )
        
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)