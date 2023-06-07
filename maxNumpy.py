import numpy as np 

class MaxVal:
    def __init__(self, array_1):
        self.A = array_1

    def MaximumValues(self):
        '''Rturn the maximum value of the arrary '''
        return max(self.A)

op_obj = MaxVal(np.array([8,9,10]))
print(op_obj.MaximumValues())
