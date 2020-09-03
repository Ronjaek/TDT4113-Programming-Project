"""Motbo klasse  mjn"""


class Motob:

    def __init__(self, motors, bbcon):
        self.motors = motors
        self.values = []
        self.bbcon = bbcon

    def update(self, values):
        """Motta en ny motor recommendation, load it into the value slot and operationalize"""
        self.values = values
        print("Motob value: ", self.values)
        self.operationalize()

    def operationalize(self):
        """konverter en motor recommendation til en eller fler motor motor settings, som sendes til riktig motor"""
        if self.values[0] == self.bbcon.behavior_values['turn'][0] and self.values[1] == self.bbcon.behavior_values['turn'][1]:
            self.motors.set_value(self.values, self.bbcon.behavior_values['turn_duration'])
        elif self.values[0] == self.bbcon.behavior_values['stop'][0] and self.values[1] == self.bbcon.behavior_values['stop'][1]:
            self.motors.set_value(self.values, self.bbcon.behavior_values['stop_duration'])
        else:
            self.motors.set_value(self.values, self.bbcon.behavior_values['motor_duration'])
