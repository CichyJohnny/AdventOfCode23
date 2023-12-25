import numpy as np


class Mirrors:
    def __init__(self, input):
        self.input = open(input, 'r')
        self.data = {}
        self.answer = 0

    def start(self):
        self.iterate()
        self.solve()

        return self.answer

    def iterate(self):
        data = self.data

        i = 0
        data[i] = []
        for line in self.input:

            if len(line) == 1:
                i += 1
                data[i] = []

            else:
                data[i].append(list(line.strip()))

    def solve(self):
        data = self.data

        for matrix in data.values():
            hor = self.look_horizontally(matrix)
            ver = self.look_vertically(matrix)

            self.answer += max(hor, ver)

    def look_horizontally(self, matrix):
        ans = 0

        for line in range(len(matrix) - 1):
            mid = len(matrix) // 2

            if len(matrix) % 2 == 1 and len(matrix) // 2 == line:
                left_side = matrix[:line + 1]
                right_side = (matrix[line:])[::-1]

                var = self.how_many_differences(left_side, right_side)

                if var:
                    ans = max(ans, 100 * (line + 1))

            if line < mid:
                left_side = matrix[:line + 1]
                right_side = (matrix[line + 1:2*(line + 1)])[::-1]

                var = self.how_many_differences(left_side, right_side)

                if var:
                    ans = max(ans, 100 * (line + 1))

            if line >= mid:
                left_rows = len(matrix) - line - 1
                left_side = matrix[line + 1:]
                right_side = (matrix[line - left_rows + 1:line + 1])[::-1]

                var = self.how_many_differences(left_side, right_side)

                if var:
                    ans = max(ans, 100 * (line + 1))

        return ans

    def look_vertically(self, matrix):
        matrix = np.transpose(matrix).tolist()
        ans = 0

        for line in range(len(matrix) - 1):
            mid = len(matrix) // 2

            if len(matrix) % 2 == 1 and len(matrix) // 2 == line:
                left_side = matrix[:line + 1]
                right_side = (matrix[line:])[::-1]

                var = self.how_many_differences(left_side, right_side)

                if var:
                    ans = max(ans, 1 * (line + 1))

            if line < mid:
                left_side = matrix[:line + 1]
                right_side = (matrix[line + 1:2 * (line + 1)])[::-1]

                var = self.how_many_differences(left_side, right_side)

                if var:
                    ans = max(ans, 1 * (line + 1))

            if line >= mid:
                left_rows = len(matrix) - line - 1
                left_side = matrix[line + 1:]
                right_side = (matrix[line - left_rows + 1:line + 1])[::-1]

                var = self.how_many_differences(left_side, right_side)

                if var:
                    ans = max(ans, 1 * (line + 1))

        return ans

    def how_many_differences(self, left, right):
        n = len(left)
        m = len(left[0])

        diff = 0
        for row in range(n):

            for char in range(m):
                if left[row][char] != right[row][char]:
                    diff += 1

                if diff > 1:
                    return False

        if diff == 1:
            return True

        return False
