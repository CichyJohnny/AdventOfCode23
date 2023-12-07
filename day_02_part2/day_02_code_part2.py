import re
import json
import os.path


class Games:
    def __init__(self, input, output):
        self.data_file = output
        self.input = open(input, 'r')
        self.data = self.load_json()
        self.answer = 0

    def start(self):
        self.iterate()
        self.save_json()
        self.check()
        return self.result()

    def load_json(self):
        if os.path.exists(self.data_file):

            with open(self.data_file, 'r') as file:
                data = json.load(file)

            return data

        return {}

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
            sum_of_red = 1
            sum_of_green = 1
            sum_of_blue = 1

            for set in self.data[game]:

                for color in self.data[game][set].items():
                    name_of_color = color[0]
                    number = color[1]

                    if name_of_color == 'red':
                        sum_of_red = max(sum_of_red, number)

                    if name_of_color == 'green':
                        sum_of_green = max(sum_of_green, number)

                    if name_of_color == 'blue':
                        sum_of_blue = max(sum_of_blue, number)

            value = sum_of_red * sum_of_green * sum_of_blue
            self.answer += value

    def result(self):
        answer = self.answer
        return answer
