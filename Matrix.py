'''
Class to add mathematical matrix functions in Python
'''

class Matrix():
    def __init__(self, matrix: list) -> Matrix:
        '''
        A matrix initialsed as a list or list of lists.
        Each list represents a column of a matrix.
        '''
        self.data = list()
        self.columns = 0
        self.rows = 0
        if isinstance(matrix, list):
            for column in matrix:
                if not isinstance(column, list):
                    #When the Matrix has only one column (or vector)
                    self.data.append(column)
                    self.columns = 1
                    break
                else:
                    if not len(matrix[0]) == len(column):
                        #Checks if all columns have the same rows
                        raise ValueError
                    #add data of the column
                    self.data.append(column)
                    #add the number of columns
                    self.columns = self.columns +1
            #add the number of rows to the functions
            self.rows = len(self.data[0]) + 1
        
    def __add__(self, b_matrix: Matrix) -> Matrix:
        if not (self.columns == b_matrix.columns and self.rows == b_matrix.rows):
            raise ValueError
        new_matrix = list()
        for column_number in range(0, self.columns):
            new_row = list()
            for row_number in range(0, self.rows):
                new_row.append(self.data[column_number][row_number] + b_matrix[column_number][row_number])
            new_matrix.append(new_row)
        return Matrix(new_matrix)