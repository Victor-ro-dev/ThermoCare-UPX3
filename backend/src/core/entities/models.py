from src.core.settings.db_configs import Base
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

class User(Base):

    '''Classe para representar a tabela 'users'.'''

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

    nursing_home_id = Column(Integer, ForeignKey("nursing_homes.id", ondelete="SET NULL"), nullable=True)

    nursing_home = relationship("NursingHome", back_populates="users")


class SensorTemp(Base):

    '''Classe para representar a tabela 'sensor_temp'.'''

    __tablename__ = "sensors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    location = Column(String(100), nullable=False)
    status = Column(String(10), nullable=True)  # 'Ativo' ou 'Inativo'
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())
    phone = Column(String(20), nullable=True)  # Telefone do sensor, se aplicável

    nursing_home_id = Column(Integer, ForeignKey("nursing_homes.id", ondelete="CASCADE"), nullable=False)

    sensor_data = relationship("SensorData", back_populates="sensor", cascade="all, delete-orphan")

    nursing_home = relationship("NursingHome", back_populates="sensors")


class NursingHome(Base):

    """Classe para representar a tabela 'nursing_home'."""

    __tablename__ = "nursing_homes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    cep = Column(String(9), nullable=False)
    logradouro = Column(String(255), nullable=False)  
    numero = Column(String(10), nullable=False)  
    bairro = Column(String(100), nullable=False) 
    cidade = Column(String(100), nullable=False)  
    estado = Column(String(2), nullable=False)  
    complemento = Column(String(255), nullable=True)  
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

    users = relationship("User", back_populates="nursing_home", uselist=False, cascade="all, delete-orphan")

    sensors = relationship("SensorTemp", back_populates="nursing_home", cascade="all, delete-orphan")


class SensorData(Base):

    """Classe para representar a tabela 'sensor_data'."""

    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(String(10), nullable=False)
    humidity = Column(String(10), nullable=False) 
    created_at = Column(DateTime, nullable=False, default=func.now())

    sensor_id = Column(Integer, ForeignKey("sensors.id", ondelete="CASCADE"), nullable=False)

    sensor = relationship("SensorTemp", back_populates="sensor_data")