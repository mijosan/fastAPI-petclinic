from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
import jwt
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext

from user.exceptions import InvalidCredentialsException, OperationNotPermittedException

SECRET_KEY = "secret_key"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(tz=timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt

def verify_password(plain_password, hashed_password):
    
    return pwd_context.verify(plain_password, hashed_password)

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        return payload
    except jwt.ExpiredSignatureError:
        raise InvalidCredentialsException(detail="Token has expired")
    except jwt.PyJWTError:
        raise InvalidCredentialsException()

def extract_user_info(payload: dict):
    user_id: str = payload.get("sub")
    role: str = payload.get("role")
    if user_id is None or role is None:
        raise InvalidCredentialsException()
    
    return {"user_id": user_id, "role": role}

def role_checker(token_data: dict, allowed_roles: list):
    if token_data["role"] not in allowed_roles:
        raise OperationNotPermittedException

def verify_token(allowed_roles: list):
    def verifier(token: str = Depends(oauth2_scheme)):
        payload = decode_token(token)
        token_data = extract_user_info(payload)
        role_checker(token_data, allowed_roles)
        
        return token_data
    return verifier