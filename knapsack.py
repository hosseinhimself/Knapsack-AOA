import numpy as np

class model:
    def __init__(self, n, W):
        '''self.v = np.array([5, 28, 52, 82, 77,  4, 58, 46, 79,  1, 62, 31, 65, 19, 93, 86, 39, 2, 64, 87, 43, 69, 79, 87, 78, 95, 83, 83, 54, 10])
        self.w = np.array([1397,  947,  451,  147,  896,  918,  242,  696, 1419,  495, 1299, 737,  372,  513, 1200, 1445, 1029,  697, 1118, 1011,  995, 1246, 427, 1270, 1140,  737, 1415,  935, 1211, 757])
        self.n = len(self.v)'''
        self.n = n
        self.v = np.random.randint(10,100,size = self.n)
        self.w = np.random.randint(200,1500,size = self.n)
        self.W = W #np.random.randint(np.min(self.w),sum(self.w))

def createRandomSolution(model):
    return np.random.randint(0,2,size = model.n)

def cost(x, model):
    Violation = max(sum(model.w * x) / model.W - 1, 0)
    alpha = 10000;
    z = sum(model.v * (1 - x)) + alpha * Violation
    return z
    