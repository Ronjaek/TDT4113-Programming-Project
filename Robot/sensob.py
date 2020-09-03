"""Class Sensob"""


class Sensob:
    """An interface between sensors and the bbcon´s behaviors"""

    def __init__(self):
        """The main instance variable of a sensob is its associated sensor(s) and its value"""
        self.sensors = []  # inneholder instanser av sensor_wrapper
        self.value = None

    def update(self):
        """Force the sensob to fetch the relevant sensor value(s) and convert to sensob value"""

        # no need to uptade more than once each timestep
        # fetch relevant sensor value(s) and convert them into one value

        pass  # pass to the update - method in one of the subclasses

    def get_value(self):
        """return the sensob value"""
        return self.value

    def reset(self):
        """Reset the sensob, by resetting the associated sensor(s)"""

        for sensor in self.sensors:
            sensor.reset()  # every sensor has a reset method
