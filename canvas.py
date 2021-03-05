import numpy as np
from PIL import Image


class Canvas:

    def __init__(self, a, b, color):
        self.color = color  # color indicates a numpy array of RGB pixels
        self.b = b  # horizontal length
        self.a = a  # vertical length

        self.data = np.zeros((self.a, self.b, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, filename):
        img = Image.fromarray(self.data, "RGB")
        img.save(filename)
