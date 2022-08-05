
import numpy as np


class DotProduct:

    def normalize(self, vec):
        normalized_v = vec / np.sqrt(np.sum(vec ** 2))  ## convert a vector to unit vector
        return normalized_v                             ## ||a|| = sqrt(x ** 2 + y ** 2)
                                                        ## the result is still a vector

    def set_a_vector(self, input_array):
        return np.array(input_array)

    def dot(self, a, b):  ## Testing
        value = 0.0
        for i in range(len(a)):
            result = a[i] * b[i]
            value = value + result

        return value

    def get_theta_value(self, input_a, input_b):
        val_01 = self.normalize(input_a)
        val_02 = self.normalize(input_b)
        #cosTheta = np.dot(val_01, val_02) ## Used the numpy dot method to calculate the cosine theta

        cosTheta = self.dot(val_01, val_02)  ## Used my own dot method
        return cosTheta

    def projection(self, prep_vector, oth_vector):
        # b prep == k * a(head)
        k = self.get_vec_length(prep_vector) * self.get_theta_value(oth_vector, prep_vector)
        print("The k value is {}".format(k))
        b_prep = k * self.normalize(oth_vector)
        return b_prep

    def get_vec_length(self, vector):
        return np.sqrt(np.sum(vector ** 2))


instance = DotProduct()
a = instance.set_a_vector([1, 1, 0])
b = instance.set_a_vector([1, 0, 0])

print("The cos theta value is: {}".format(instance.get_theta_value(a, b)))

print("The b prep is: {}".format(instance.projection(b, a)))


## The cos theta value is: 0.9965457582448797

## The cos theta value is: 0.9965457582448797