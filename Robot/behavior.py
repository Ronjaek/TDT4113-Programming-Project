
class Behavior:

    def __init__(self, bbcon):
        self.bbcon = bbcon #pointer to the controller that uses this behavior
        self.sensob = [] #a list of all sensobs that this behavior uses
        self.motor_recommendations = None #list of recommendations
        self.motobs = [] #fylles ut av subkalsse
        self.halt = False
        self.active_flag = False
        self.priority = 1
        self.match_degree = 0
        self.weight = 0

    def halt_request(self, bool):
        self.halt = bool
        if bool:
            self.active_flag = False

    def consider_activation(self):  # Skal implementeres av subklasse
        """Test whether it should deactivate. When decativated notify bbcon so that sensors can be turned of """
        return

    def consider_deactivation(self):  # Skal implementeres av subklasse
        """Test whether it should deactivate. When decativated/ activated notify bbcon"""
        return

    def sense_and_act(self):  # Skal implementeres av subklasse
        return

    def update(self):  # Skal kalles hvert tick, eneste metode som skal kalles utenfra
        self.consider_deactivation() if self.active_flag else self.consider_activation()

        if self.active_flag:
            self.sense_and_act()

        self.weight = self.priority * self.match_degree


class Go(Behavior):

    def __init__(self, bbcon):
        super().__init__(bbcon)
        self.priority = bbcon.behavior_values["goPri"]  # dic fra bbcon

    def consider_activation(self):
        """test whether it should deactivate"""
        self.active_flag = True

    def consider_deactivation(self):
        """test whether it should deactivate"""
        self.active_flag = True

    def sense_and_act(self):
        self.motor_recommendations = [self.bbcon.behavior_values["forward"]]
        self.match_degree = 1


class AvoidCollision(Behavior):

    def __init__(self, bbcon, ultra_sonic):
        super().__init__(bbcon)
        self.priority = bbcon.behavior_values["collitionPri"]  # dic fra bbcon
        self.sensob = [ultra_sonic]

    def consider_activation(self):
        """test whether it should deactivate"""
        self.active_flag = True

    def consider_deactivation(self):
        """test whether it should deactivate"""
        self.active_flag = True

    def sense_and_act(self):
        distance = self.sensob[0].get_value()
        min_distance = self.bbcon.behavior_values["min_distance"]
        self.match_degree = 0
        self.motor_recommendations = None

        if distance <= min_distance:
            self.motor_recommendations = [self.bbcon.behavior_values["backwards"]]
            self.match_degree = 1


class AvoidWhiteline(Behavior):
    def __init__(self, bbcon, ir_sensor):
        super().__init__(bbcon)
        self.priority = bbcon.behavior_values["whitePri"] #dic fra bbcon
        self.sensob = [ir_sensor]

    def consider_activation(self):
        """test whether it should deactivate"""
        self.active_flag = True

    def consider_deactivation(self):
        """test whether it should deactivate"""
        self.active_flag = True

    def sense_and_act(self):
        sensor_array = self.sensob[0].get_value()
        white_scale = self.bbcon.behavior_values["white_scale"] #Take in number to compare sensor with
        self.match_degree = 0
        self.motor_recommendations = None
        for number in sensor_array:
            if number <= white_scale:
                self.motor_recommendations = [self.bbcon.behavior_values["turn"]]
                self.match_degree = 1
                break


class Stop(Behavior):
    def __init__(self, bbcon, camera_sensor):
        super().__init__(bbcon)
        self.priority = bbcon.behavior_values["cameraPri"] #dic fra bbcon
        self.sensob = [camera_sensor]
        self.stopped = False

    def consider_activation(self):
        """test whether it should deactivate"""
        self.active_flag = True

    def consider_deactivation(self):
        """test whether it should deactivate"""
        if self.halt:
            self.active_flag = False

    def sense_and_act(self):
        image = self.sensob[0].get_value()
        red_scale = self.bbcon.behavior_values["red_scale"] #Take in number to compare sensor with
        self.match_degree = 0
        self.motor_recommendations = None

        if self.stopped and image[0] >= red_scale:
            self.motor_recommendations = [self.bbcon.behavior_values["forward"]]
            self.stopped = False
            self.match_degree = 1
        elif image[0] >= red_scale:
            self.motor_recommendations = [self.bbcon.behavior_values["stop"]]
            self.stopped = True
            self.match_degree = 1






