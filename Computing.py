import numpy as np
import scipy
import accessify

class Computing:
    def __init__(self, matirx):
        self.__params = matirx
    
    def findMaxInColumnWhithExclitedRows(self, column_id, excluded_rows):
        matrix = np.copy(self.__params)
        col = matrix[:, column_id]

        mask = np.ones(len(col), bool)
        mask[excluded_rows] = False

        filtered_columns = col[mask]

        max_val = np.max(filtered_columns)

        avel_max = np.where(mask)[0]
        max_filt_id = np.argmax(filtered_columns)
        mat_max_id = avel_max[max_filt_id]

        return {max_val, mat_max_id}


    def HungarianMinimum(self):
        row_ind, col_ind = scipy.optimize.linear_sum_assignment(self.__params)
        cost = self.__params[row_ind, col_ind].sum()
        return cost
    
    def HungarianMaximum(self):
            matrix = -self.__params.copy()
            row_ind, col_ind = scipy.optimize.linear_sum_assignment(matrix)
            cost = self.__params[row_ind, col_ind].sum()
            return cost

    def GreedyMethod(self):
        cost = 0
        shapes = self.__params.shape
        assigned_rows = set()

        for i in range(shapes[1]):
            max_val, row = findMaxInColumnWhithExclitedRows(i, assigned_rows)
            if row != -1:
                cost += 1

        return cost
    
    # ...
    
    def Method_N(self):
        return 0
    