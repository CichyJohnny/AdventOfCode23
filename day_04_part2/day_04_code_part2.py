import json
import os.path


class Cards:
    def __init__(self, input, output):
        self.data_file = output
        self.input = open(input, 'r')
        self.data = self.load_json()
        self.last = 0
        self.answer = 0

    def start(self):
        self.iterate()
        self.calculate()
        self.save_json()
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
            game = line.strip()

            sep_temp = game.split(': ')
            sep_temp[1] = sep_temp[1].split(' | ')
            sep_temp[1][0] = sep_temp[1][0].split()
            sep_temp[1][1] = sep_temp[1][1].split()

            sep_temp[1][0] = [int(i) for i in sep_temp[1][0]]
            sep_temp[1][1] = [int(i) for i in sep_temp[1][1]]

            sep = sep_temp

            id = sep[0].split()[1]
            self.data[id] = {}
            self.data[id]['winning'] = sep[1][0]
            self.data[id]['your_nums'] = sep[1][1]
            self.data[id]['copies'] = 1
            self.data[id]['num_of_wins'] = 0

        self.last = int(id)


    def calculate(self):
        data = self.data

        for game in data:
            current_game = data[game]

            for winning_number in current_game['winning']:

                if winning_number in current_game['your_nums']:
                    current_game['num_of_wins'] += 1

            for i in range(int(game) + 1, int(game) + current_game['num_of_wins'] + 1):

                if i <= self.last:
                    data[str(i)]['copies'] += current_game['copies']



    def result(self):
        data = self.data

        for game in data:
            self.answer += data[game]['copies']

        answer = self.answer
        return answer
