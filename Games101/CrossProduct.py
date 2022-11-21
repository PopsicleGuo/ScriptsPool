import numpy as np


class Vectors:
    def __init__(self, vec):
        self._vector = np.array(vec)

    @property
    def vector(self):
        return self._vector

    @vector.setter
    def vector(self, new_vec):
        self._vector = np.array(new_vec)

    ''' Use numpy cross product to calculate item  '''
    @classmethod
    def cross(cls, vector_1, vector_2):
        return np.cross(vector_1, vector_2)

    @staticmethod
    def get_vectors_distance(start_point, end_point):
        """ A method to get a distance length between two vectors """
        return np.sqrt((start_point[0]-end_point[0])**2 + (start_point[1]-end_point[1])**2 + (start_point[2]-end_point[2])**2)

    def __str__(self):
        print(f'Vector is {self._vector}')

    def __repr__(self):
        print(f'Vectors({self._vector})')


class CrossProduct(Vectors):
    """  Write down the math formula of cross product """

    @classmethod
    def cross(cls, a, b):
        """
            # ||a * b|| = ||a||||b||sine theta
            # cross(a, b) = (ya*zb - za*yb, za*xb - xa*zb, xa*yb - ya*xb )
        """
        third_vector = (a[1]*b[2] - a[2]*b[1],
                     a[2]*b[0] - a[0]*b[2],
                     a[0]*b[1] - a[1]*b[0])
        return third_vector


class DotProduct(Vectors):
    """ A Dot product module """

    @classmethod
    def normalize(cls, vec):
        normalized = vec / np.sqrt(np.sum(vec ** 2))  # convert a vector to unit vector
        return normalized                             # ||a|| = sqrt(x ** 2 + y ** 2)
                                                      # the result is still a vector

    @classmethod
    def dot(cls, vec_01, vec_02):  # Get a dot result for vectors
        value = 0.0
        for i in range(len(vec_01)):
            result = vec_01[i] * vec_02[i]
            value = value + result
        return value

    def get_theta_value(self, input_a, input_b):
        val_01 = self.normalize(input_a)
        val_02 = self.normalize(input_b)
        #cosTheta = np.dot(val_01, val_02)  # Used the numpy dot method to calculate the cosine theta
        cos_theta = self.dot(val_01, val_02)  # Used my own dot method
        return cos_theta

    def projection(self, prep_vector, oth_vector):
        """  b prep == k * a(head)  """
        k = self.get_vec_length(prep_vector) * self.get_theta_value(oth_vector, prep_vector)
        print("The k value is {}".format(k))
        b_prep = k * self.normalize(oth_vector)
        return b_prep

    @classmethod
    def get_vec_length(cls, input_vec):
        return np.sqrt(np.sum(input_vec ** 2))


if __name__ == '__main__':
    vec_a = Vectors([1, 2, 3])
    vec_b = Vectors([4, 5, 6])

    print(f"The numpy cross result is {Vectors.cross(vec_a, vec_b)}")

    vector = CrossProduct.cross([1,2,3], [4,5,6])
    print(f"My own cross result is {vector}")
