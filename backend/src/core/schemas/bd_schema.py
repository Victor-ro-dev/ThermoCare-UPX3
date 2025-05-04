from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum

class LastSensorDataSchema(BaseModel):
    id: int
    temperature: str
    humidity: str
    class Config:
        from_attributes = True

class SensorWithLastDataSchema(BaseModel):
    id: int
    name: str
    location: str
    status: str
    phone: Optional[str] = None
    last_data: Optional[LastSensorDataSchema] = None

    class Config:
        from_attributes = True

class SensorDataSchema(BaseModel):
    id: Optional[int] = None
    temperature: str
    humidity: str
    created_at: str
    sensor_id: int

    class Config:
        from_attributes = True

class SensorStatus(str, Enum):
    on = "Ativo"
    off = "Inativo"
class SensorTempSchema(BaseModel):
    id: Optional[int] = None
    name: str
    location: str
    status: Optional[SensorStatus] = SensorStatus.on
    phone: str
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

class ProfileSchema(BaseModel):
    username: str
    email: EmailStr
    

    class Config:
        from_attributes = True

class NursingProfileSchema(BaseModel):
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