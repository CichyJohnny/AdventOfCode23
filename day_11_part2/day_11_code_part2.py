
import numpy as np


class Maze:
    def __init__(self, input):
        self.input = open(input, 'r')
        self.data = []
        self.hash = {}
        self.x_cords = []
        self.y_cords = []
        self.answer = 0

    def start(self):
        self.iterate()
        self.find_hashtags()
        self.calculate()
        return self.answer

    def iterate(self):
        data = self.data

        i = 0
        for line in self.input:
            line = line.strip()
            line = list(line)
            data.append(line)

            if len(line) == line.count('.'):
                self.x_cords.append(i)

            i += 1

        data = np.transpose(data).tolist()
        new_data = []

        i = 0
        for line in data:
            new_data.append(line)

            if len(line) == line.count('.'):
                self.y_cords.append(i)

            i += 1

        data = np.transpose(new_data).tolist()
        self.data = data

    def find_hashtags(self):
        data = self.data
        height = len(data)
        width = len(data[0])

        index = 1
        for row in range(height):

            for col in range(width):

                if data[row][col] == '#':
                    data[row][col] = str(index)
                    self.hash[index] = (row, col)
                    index += 1

    def calculate(self):
        hash = self.hash
        max_index = max(hash.keys())

        for first in range(1, max_index + 1):

            for second in range(first, max_index + 1):

                if first != second:
                    x1 = hash[first][0]
                    x2 = hash[second][0]
                    y1 = hash[first][1]
                    y2 = hash[second][1]
                    new_x = 0
                    new_y = 0

                    for new_rows in self.x_cords:
                        if x1 < new_rows < x2 or x2 < new_rows < x1:
                            new_x += 1000000 - 1

                    for new_cols in self.y_cords:
                        if y1 < new_cols < y2 or y2 < new_cols < y1:
                            new_y += 1000000 - 1

                    x = abs(hash[first][0] - hash[second][0]) + new_x
                    y = abs(hash[first][1] - hash[second][1]) + new_y
                    self.answer += x + y

        print(self.x_cords, self.y_cords)
