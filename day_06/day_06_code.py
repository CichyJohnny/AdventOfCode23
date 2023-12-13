import json
import numpy as np
from math import floor, ceil


class Race:
    def __init__(self, input, output):
        self.data_file = output
        self.input = open(input, 'r')
        self.data = {}
        self.answer = []

    def start(self):
        self.iterate()
        self.save()
        self.solve()
        return self.result()

    def save(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.data, file, indent=4)

    def iterate(self):
        data = self.data

        for line in self.input:
            sep = line.strip().split()

            for num in range(len(sep[1:])):
                key = sep[0][:-1]
                val = int(sep[1 + num])

                if num + 1 not in data.keys():
                    data[num + 1] = {key: val}

                else:
                    data[num + 1].update({key: val})

    def solve(self):
        data = self.data

        for race in list(data.values()):
            time = race['Time']
            distance = race['Distance']
            coefficients = [-1, time, -distance]
            a, b = np.roots(coefficients)

            if a == floor(a):
                a -= 1
            else:
                a = floor(a)

            if b == ceil(b):
                b += 1
            else:
                b = ceil(b)

            self.answer.append(a - b + 1)

    def result(self):
        answer = 1

        for num in self.answer:
            answer *= num

        return int(answer)
