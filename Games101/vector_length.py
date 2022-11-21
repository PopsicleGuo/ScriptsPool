import numpy as np


class Vectors:
    def __init__(self):
        self._vector = None

    def set_object_location(self, vector):
        self._vector = vector

    def length(self, vec_outside):
        return np.sqrt((self._vector[0]-vec_outside[0])**2 + (self._vector[1]-vec_outside[1])**2 + (self._vector[2]-vec_outside[2])**2)




obj = Vectors()
obj.set_object_location([-221, 578, 294])
result = obj.length([-263, 581, 278])
print(result)