import numpy as np


class Maze:
    def __init__(self, input):
        self.input = open(input, 'r')
        self.data = []
        self.hash = {}
        self.answer = 0

    def start(self):
        self.iterate()
        self.find_hashtags()
        self.calculate()
        self.save()

        return self.answer

    def save(self):
        data = self.data

        with open('day_11_output.txt', 'w') as f:
            for line in data:
                f.write(''.join(line) + '\n')

    def iterate(self):
        data = self.data

        for line in self.input:
            line = line.strip()
            line = list(line)
            data.append(line)

            if len(line) == line.count('.'):
                data.append(line)

        data = np.transpose(data).tolist()
        new_data = []

        for line in data:
            new_data.append(line)

            if len(line) == line.count('.'):
                new_data.append(line)

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
                    x = abs(hash[first][0] - hash[second][0])
                    y = abs(hash[first][1] - hash[second][1])
                    self.answer += x + y
