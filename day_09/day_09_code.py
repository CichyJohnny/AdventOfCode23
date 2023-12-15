import json


class Prediction:
    def __init__(self, input, output):
        self.data_file = output
        self.input = open(input, 'r')
        self.data = {}
        self.max = 0
        self.answer = 0

    def start(self):
        self.iterate()
        self.solve()
        self.predict()
        self.save()
        return self.result()

    def save(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.data, file, indent=4)

    def iterate(self):
        data = self.data

        num = 1
        for line in self.input:
            data[num] = {}
            data[num][1] = [int(x) for x in line.split()]
            self.max = num
            num += 1

    def solve(self):
        data = self.data

        for i in range(1, self.max + 1):
            history = data[i][1]
            num = 2

            while not (history.count(history[0]) == len(history) and history[0] == 0):
                next_line = []

                for j in range(len(history) - 1):
                    next_line.append(history[j + 1] - history[j])

                history = next_line
                data[i][num] = history
                num += 1

            data[i]['max_line'] = num - 1

    def predict(self):
        data = self.data

        for i in range(1, self.max + 1):
            num_line = data[i]['max_line']
            last = 0

            for j in reversed(range(1, num_line)):
                last = data[i][j][-1] + last

            self.answer += last

    def result(self):

        return self.answer
