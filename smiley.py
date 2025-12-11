from sense_hat import SenseHat


class Smiley:
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    BLANK = (0, 0, 0)

    def __init__(self, complexion=YELLOW):
        # We have encapsulated the SenseHat object
        self.sense_hat = SenseHat()

        Y = self.YELLOW
        O = self.BLANK
        B = self.BLUE
        R = self.RED

        self.complexion = complexion
        self.my_complexion = self.complexion
        X = self.complexion

        self.pixels = [self.complexion] * 64

        self.pixels_yellow = [
            O, X, X, X, X, X, X, O,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            O, X, X, X, X, X, X, O,
        ]

        self.pixels_blue = [
            O, B, B, B, B, B, B, O,
            B, B, B, B, B, B, B, B,
            B, B, B, B, B, B, B, B,
            B, B, B, B, B, B, B, B,
            B, B, B, B, B, B, B, B,
            B, B, B, B, B, B, B, B,
            B, B, B, B, B, B, B, B,
            O, B, B, B, B, B, B, O,
        ]

    def dim_display(self, dimmed=True):
        """
        Set the SenseHat's light intensity to low (True) or high (False)
        :param dimmed: Dim the display if True, otherwise don't dim
        """
        self.sense_hat.low_light = dimmed

    def complexion(self):
        return self.my_complexion

    def show(self):
        """
        Show the smiley on the screen as yellow.
        """
        return self.sense_hat.set_pixels(self.pixels)
