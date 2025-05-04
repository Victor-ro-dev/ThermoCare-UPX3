from abc import ABC, abstractmethod


class SensorServiceInterface(ABC):
    """Interface for sensor service."""

    @abstractmethod
    async def add_sensor(self, sensor_data: dict) -> dict:
        """Add a new sensor."""
        pass
    
    @abstractmethod
    async def get_all_sensor_by_nursing_id(self, sensor_id: str) -> dict:
        """Get a sensor by its ID."""
        pass