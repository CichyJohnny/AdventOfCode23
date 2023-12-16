import json
import re


class Garden:
    def __init__(self, input, output):
        self.data_file = output
        self.input = open(input, 'r')
        self.data = {}
        self.answer = float('inf')
        self.perc = 0

    def start(self):
        self.iterate()
        for i in range(0, len(self.data['seeds']), 2):
            self.perc += int(self.data['seeds'][i+1])
        self.calculate()
        self.save_json()
        return self.result()

    def save_json(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.data, file, indent=4)

    def iterate(self):
        data = self.data
        data['steps'] = []

        for text in self.input:
            text = text.strip()

            if text:
                sep = re.split(' |:', text)

                if not sep[0].isnumeric():

                    if sep[0] == 'seeds':
                        seeds = sep[2:]
                        data[sep[0]] = seeds

                    else:
                        data['steps'].append([])

                else:
                    nums = [int(i) for i in sep]
                    data['steps'][-1].append(nums)

    def calculate(self):
        data = self.data
        ranges = list(map(int, data['seeds']))

        num = 0
        for i in range(0, len(ranges), 2):
            first = ranges[i]
            last = ranges[i] + ranges[i + 1]

            for val in range(first, last):
                print(f'{num / self.perc * 100}%')
                num += 1
                x = int(val)

                for step in data['steps']:

                    for r in step:
                        source = x >= r[1] and x < r[1] + r[2]

                        if source:
                            destination = r[0] - r[1]
                            x = x + destination
                            break

                self.answer = min(self.answer, x)

    def result(self):
        answer = self.answer
        return answer
