"""A subclass of Sensob"""
from sensob import Sensob
from reflectance_sensors import ReflectanceSensors


class ReflectanceSensob(Sensob):
    """Calculate the distance to the nearest obstacle by looking at the time differences"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.sensors = [ReflectanceSensors()]

    def update(self):
        """Overwrite the update-method in the superclass Sensob"""
        for sensor in self.sensors:
            sensor.update()

        self.value = self.sensors[0].get_value()
        print("Reflectance", self.value)
        return self.value
