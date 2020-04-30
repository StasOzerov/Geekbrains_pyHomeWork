'''
Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.

Примеры матриц вы найдете в методичке.

Следующий шаг — реализовать перегрузку метода str()
для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода add() для реализации
операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
'''

class Matrix:

    def __init__(self, matrix):
        List = []
        for i in matrix:
            List.append([j for j in i])  # заполнение каждой строки матрицы
        self.matrix = List

    def __len__(self):
        return len(self.matrix) * len(self.matrix[0])

    def __str__(self):
        return '\n'.join([''.join(['\t%.f\t' % i for i in row]) for row in self.matrix])

    def __add__(self, other):
        result = []  # будущая матрица
        numbers = []  # строка матрицы
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summa = other.matrix[i][j] + self.matrix[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.matrix[0]):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)



matrix_A = Matrix([[56, 67, 0, 0], [8, 10.8, 0, 0], [9, 0, 0, 0]])
matrix_B = Matrix([[56, 67, 0, 0], [8, 10.8, 0, 0], [9, 0, 0, 0]])

print('matrix_A:\n', matrix_A, '\n')
print('Длина матрицы matrix_A =', len(matrix_A), '\n')
print('matrix_B:\n', matrix_B, '\n')
print('Длина матрицы matrix_B =', len(matrix_B), '\n')

matrix_C = matrix_A + matrix_B
print('matrix_C:\n', matrix_C, '\n')
