import re
import json


class Games:
    def __init__(self, input, output):
        self.data_file = output
        self.input = open(input, 'r')
        self.data = {}
        self.answer = 0

    def start(self):
        self.iterate()
        self.save_json()
        self.check()
        return self.result()

    def save_json(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.data, file, indent=4)

    def iterate(self):

        for line in self.input:
            text = line.strip()
            sep = re.split(': |; ', text)
            sets = sep[1:]

            id = sep[0].split()[1]
            self.data[id] = {}

            for i in range(len(sets)):
                set = re.split(' |, ', sets[i])
                colors = {}

                for j in range(int(len(set) / 2)):
                    colors[set[j * 2 + 1]] = int(set[j * 2])

                self.data[id][i + 1] = colors

    def check(self):
        for game in self.data:
            var = True

            for set in self.data[game]:

                for color in self.data[game][set].items():

                    if color[0] == 'red' and color[1] > 12:
                        var = False

                    if color[0] == 'green' and color[1] > 13:
                        var = False

                    if color[0] == 'blue' and color[1] > 14:
                        var = False

            if var:
                self.answer += int(game)

    def result(self):
        answer = self.answer
        return answer
