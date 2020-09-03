"""A subclass of Sensob"""
from sensob import Sensob
from ultrasonic import Ultrasonic


class UltrasonicSensob(Sensob):
    """Calculate the distance to the nearest obstacle by looking at the time differences"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.sensors = [Ultrasonic()]

    def update(self):
        """Overwrite the update-method in the superclass Sensob"""
        for sensor in self.sensors:
            sensor.update()

        self.value = self.sensors[0].get_value()
        print("Ultrasonic", self.value)
        return self.value

