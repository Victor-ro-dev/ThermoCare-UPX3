from pydantic import BaseModel, EmailStr
from typing import Optional

class SensorTempSchema(BaseModel):
    id: Optional[int] = None
    name: str
    location: str
    nursing_home_id: Optional[int] = None

    class Config:
        from_attributes = True

class NursingHomeSchema(BaseModel):
    id: Optional[int] = None
    name: str
    cep: str
    logradouro: str
    numero: str
    bairro: str
    cidade: str
    estado: str
    complemento: Optional[str] = None

    class Config:
        from_attributes = True

class UserSchema(BaseModel):
    id: Optional[int] = None
    username: str
    email: EmailStr
    password_hash: str
    nursing_home_id: Optional[int] = None

    class Config:
        from_attributes = True

class UserLoginSchema(BaseModel):
    id : Optional[int] = None
    email: EmailStr
    password: str

    class Config:
        from_attributes = True

class UserCreateSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
    password_confirmation: str  
    nursing_home_id: Optional[int] = None