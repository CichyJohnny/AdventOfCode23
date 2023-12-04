import re, json, os.path

input = open('day_02_input.txt', 'r')


class Games:
    def __init__(self):
        self.data_file = 'day_02_output.json'
        self.data = self.load_json()
        self.answer = 0


    def start(self, input):
        self.iterate(input)
        self.save_json()
        self.check()
        self.result()

    def load_json(self):
        if os.path.exists(self.data_file):

            with open(self.data_file, 'r') as file:
                data = json.load(file)

            return data

        return {}

    def save_json(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.data, file, indent=4)

    def iterate(self, file):

        for line in file:
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
                        print(color)
                        var = False
                    if color[0] == 'green' and color[1] > 13:
                        print(color)
                        var = False
                    if color[0] == 'blue' and color[1] > 14:
                        print(color)
                        var = False

            if var:
                self.answer += int(game)
                print(game)
        print(self.answer)

    def result(self):
        answer = self.answer
        return answer
