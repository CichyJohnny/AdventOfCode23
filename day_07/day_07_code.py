import json
from collections import Counter


class Cards:
    def __init__(self, input, output):
        self.data_file = output
        self.input = open(input, 'r')
        self.order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
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

        num = 1
        for line in self.input:
            sep = line.split()
            data[num] = {
                'cards': sep[0],
                'bid': int(sep[1]),
                'order': 0
            }
            num += 1

    def solve(self):
        data = self.data

        for num in range(len(data)):
            cards = data[num + 1]['cards']

            if max(Counter(cards).values()) == 5:
                data[num + 1]['order'] = 6

            elif max(Counter(cards).values()) == 4:
                data[num + 1]['order'] = 5

            elif max(Counter(cards).values()) == 3 and min(Counter(cards).values()) == 2:
                data[num + 1]['order'] = 4

            elif max(Counter(cards).values()) == 3:
                data[num + 1]['order'] = 3

            elif max(Counter(cards).values()) == 2 and list(Counter(cards).values()).count(2) == 2:
                data[num + 1]['order'] = 2

            elif max(Counter(cards).values()) == 2:
                data[num + 1]['order'] = 1

            else:
                data[num + 1]['order'] = 0

            mapa = []
            for char in cards:
                x = self.order.index(char)
                mapa.append(x)

            data[num + 1]['mapa'] = mapa

    def result(self):
        data = list(self.data.values())
        sorted_data = sorted(data, key=lambda x: (-x['order'], x['mapa']))
        sorted_data.reverse()

        for i in range(len(list(sorted_data))):
            self.answer += sorted_data[i]['bid'] * (i + 1)

        return self.answer
