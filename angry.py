from smiley import Smiley
import time

class Angry(Smiley):
    def __init__(self):
        super().__init__(complexion=self.RED)

        self.draw_mouth()
        self.draw_eyes()


    def draw_mouth(self):
        """
        Draws the mouth feature on a smiley
        """
        mouth = [49, 54, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLACK


    def draw_eyes(self, wide_open=True):
        """
        Draws open or closed eyes on a smiley
        :param wide_open: Render eyes wide open or shut
        """
        eyes = [9, 10, 13, 14, 18, 21]
        color = self.BLACK if wide_open else self.complexion()
        for pixel in eyes:
            self.pixels[pixel] = color


    def blink(self, delay=0.25):
        """
        Blinks the eyes of the sad smiley twice.

        :param delay: Delay between closing and opening the eyes
        """
        for blink in range(2):
            self.draw_eyes(wide_open=False)
            self.show()
            time.sleep(delay)

            self.draw_eyes(wide_open=True)
            self.show()
            time.sleep(delay)