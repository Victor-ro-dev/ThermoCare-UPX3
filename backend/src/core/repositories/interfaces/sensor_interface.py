from abc import ABC, abstractmethod
from typing import List, Optional
from src.core.entities.models import SensorTemp

class SensorInterface(ABC):

    """Interface for sensor repository."""
    @abstractmethod
    def add_sensor(self, sensor: SensorTemp) -> SensorTemp:
        """Add a new sensor."""
        pass

    @abstractmethod
    def get_sensor_by_id(self, sensor_id: str) -> Optional[SensorTemp]:
        """Get a sensor by its ID."""
        pass
    
    @abstractmethod
    def get_all_sensors_by_nursing_home(self, nursing_home_id: str) -> List[SensorTemp]:
        """Get all sensors by nursing home ID."""
        pass
    