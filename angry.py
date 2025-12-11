import time
from smiley import Smiley
from blinkable import Blinkable


class Angry(Smiley, Blinkable):
    def __init__(self):
        super().__init__(complexion=self.RED)

        self.draw_features()
        self.draw_eyes()

    def draw_features(self):
        """
        Draws the mouth feature on a smiley
        """
        features = [1, 6, 10, 13, 49, 54, 42, 43, 44, 45]
        for idx in features:
            self.pixels[idx] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws open or closed eyes on a smiley
        :param wide_open: Render eyes wide open or shut
        """
        eyes = [26, 29]
        for idx in eyes:
            if wide_open:
                self.pixels[idx] = self.BLANK
            else:
                self.pixels[idx] = self.my_complexion

    def blink(self, delay=0.25):

        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()
