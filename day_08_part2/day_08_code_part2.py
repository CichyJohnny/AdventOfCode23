import json
import re
import math


class Maps:
    def __init__(self, input, output):
        self.data_file = output
        self.input = open(input, 'r')
        self.order = []
        self.data = {}
        self.answer = 0

    def start(self):
        self.iterate()
        self.solve()
        self.save()
        return self.result()

    def save(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.data, file, indent=4)

    def iterate(self):
        data = self.data
        data['order'] = []
        data['nodes'] = {}

        num = 1
        for line in self.input:

            if num == 1:
                self.order = list(line.strip())
                data['order'] = self.order

            elif num > 2:
                line = line.strip()
                sep = re.split(r'[, =()]', line)
                data['nodes'][sep[0]] = [sep[4], sep[6]]

            num += 1

    def solve(self):
        data = self.data
        current = []

        for key in data['nodes'].keys():
            if key[-1] == 'A':
                current.append(key)

        next_z = [self.mapa(x) for x in current]
        self.answer = math.lcm(*next_z)

    def mapa(self, current):
        data = self.data
        i = 0

        while current[-1] != 'Z':
            curr_order = i % len(self.order)
            direction = self.order[curr_order]

            if direction == 'L':
                direction = 0

            else:
                direction = 1

            current = data['nodes'][current][direction]
            i += 1
        else:
            answer = i
            return answer

    def result(self):

        return self.answer
