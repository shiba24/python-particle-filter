import numpy as np


class Robot(object):
    """
    Robot class, parent of all the algorithms for update 
    of the belief with the Bayes filtering.
    """
    def __init__(self):
        pass

    def update_belief(self):
        pass

    def update_prediction(self):
        pass

    def motion_model(self):
        pass

    def measurement_model(self):
        pass        

    def control(self, x, u):
        # you may add some noise here
        return x, u

    def gauss_likelihood(self, x, sigma):
        p = 1.0 / np.sqrt(2.0 * np.pi * sigma ** 2) * np.exp(-x ** 2 / (2 * sigma ** 2))
        return p


