'''
Class to add mathematical matrix functions in Python
'''

class Matrix():
    def __init__(self, matrix: list):
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

    def __helper_matrixmultiply(self, zip_content: list) -> float:
        '''
        multiply a various number of tuple with two values each tuple
        i. e. the first tuple x*y and second tuble a * b and makes an
        addition of each product. It represents one single operation of
        a matrix multiply 
        '''
        sum = 0
        for element in zip_content:
            sum = sum + (element[0] * element[1])
        return sum

    def __multiply_operator(self, multiplikator) -> Matrix:
        '''
        multiply with other Matrix, Scalar or other factors
        '''
        if isinstance(multiplikator, (int, float)):
            new_matrix = list()
            for column_number in range(0, self.columns):
                new_row = list()
                for row_number in range(0, self.rows):
                    new_row.append(self.data[column_number][row_number] * multiplikator)
                new_matrix.append(new_row)
            return Matrix(new_matrix)
        elif isinstance(multiplikator, Matrix):
            if not self.columns == multiplikator.rows:
                raise ValueError
            new_matrix = list()
            for b_column in range(multiplikator.columns):
                new_column = list()
                for a_row in range(0, self.rows):
                    new_column.append(
                        self.__helper_matrixmultiply(
                            zip(
                                [self.data[a_row][i] for i in range(0, self.columns)],
                                [multiplikator[b_column][j] for j in range(0, multiplikator.rows)]
                            )
                        )
                    )
                new_matrix.append(new_column)
            return Matrix(new_matrix)
        else:
            raise NotImplementedError

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

    def __mul__(self, b_matrix: Matrix) -> Matrix:
        return self.__multiply_operator(b_matrix)

    def __rmul__(self, b_matrix) -> Matrix:
        return self.__multiply_operator(b_matrix)