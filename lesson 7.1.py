class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for el in self.matrix:
            for i in el:
                print(f"{i:4}", end="")
            print()
        return '\n'.join(map(str, self.matrix))

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for y in range(len(other.matrix[i])):
                self.matrix[i][y] = self.matrix[i][y] + other.matrix[i][y]
        return Matrix.__str__(self)


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix_1.__add__(matrix_2))
