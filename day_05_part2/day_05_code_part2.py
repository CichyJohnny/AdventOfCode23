import json
import re


class Garden:
    def __init__(self, input, output):
        self.data_file = output
        self.input = open(input, 'r')
        self.data = {}
        self.answer = float('inf')

    def start(self):
        self.iterate()
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

        for seed in data['seeds']:
            x = int(seed)

            for step in data['steps']:

                for r in step:
                    source = x >= r[1] and x < r[1] + r[2]

                    if source:
                        destination = x + r[0] - r[1]
                        x = destination
                        break

            self.answer = min(x, self.answer)

    def result(self):
        answer = self.answer
        return answer
