# PossibleChar.py

import cv2
import numpy as np
import math

class PossibleChar:

    def __init__(self, _contour):
        self.contour = _contour

        self.boundingRect = cv2.boundingRect(self.contour)

        [intX, intY, intWidth, intHeight] = self.boundRect

        self.BoundRectX = intX
        self.BoundRectY = intY
        self.BoundRectW = intWidth
        self.BoundRectH = intHeight

        self.BoundRectA = self.BoundRectW * self.BoundRectH

        self.intCenterX = (self.BoundRectX + self.BoundRectX + self.BoundRectW) / 2
        self.intCenterY = (self.BoundRectY + self.BoundRectY + self.BoundRectW) / 2

        self.fltRectDiagLength = math.sqrt((self.BoundRectW ** 2) + (self.BoundRectH ** 2))

        self.fltAspectRatio = float(self.BoundRectW) / float(self.BoundRectH)

# end class








