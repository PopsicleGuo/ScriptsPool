import numpy as np


class Vectors:
    def __init__(self, vector_a, vector_b):
        self.__vector_a = vector_a
        self.__vector_b = vector_b

    def vector_array(self):
        self.__vector_a = np.array(self.__vector_a)
        self.__vector_b = np.array(self.__vector_b)

    def cross(self):
        return np.cross(self.__vector_a, self.__vector_b)


obj_01 = Vectors([1,2,3], [4,5,6])

print("The cross result is {}".format(obj_01.cross()))
