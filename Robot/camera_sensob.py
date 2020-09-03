"""A subclass of Sensob"""
from sensob import Sensob
from camera import Camera


class CameraSensob(Sensob):

    def __init__(self):
        super().__init__()
        self.camera_obj = Camera()
        self.sensors = [self.camera_obj]

    def rgb(self, img):
        rgb_list = [0, 0, 0]

        for x in range(40, 80):
            for y in range(40, 50):
                band = img.getpixel((x, y))
                rgb_list[0] += band[0]
                rgb_list[1] += band[1]
                rgb_list[2] += band[2]

        tot = sum(rgb_list)

        rgb_list[0] = rgb_list[0] / tot
        rgb_list[1] = rgb_list[1] / tot
        rgb_list[2] = rgb_list[2] / tot

        return rgb_list

    def update(self):
        """Overwrite the update-method in the superclass Sensob"""
        self.value = self.rgb(self.sensors[0].update())
        print("Camera", self.value)
        return self.value
