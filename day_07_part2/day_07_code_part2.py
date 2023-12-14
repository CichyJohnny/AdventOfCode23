import json
from collections import Counter


class Race:
    def __init__(self, input, output):
        self.data_file = output
        self.input = open(input, 'r')
        self.order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
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
            keys = list(Counter(cards).keys())
            if 'J' in keys:

                for exchange in keys:
                    new_cards = [exchange if x == 'J' else x for x in cards]
                    val = Counter(new_cards).values()

                    if max(val) == 5:
                        data[num + 1]['order'] = max(6, data[num + 1]['order'])

                    elif max(val) == 4:
                        data[num + 1]['order'] = max(5, data[num + 1]['order'])

                    elif max(val) == 3 and min(val) == 2:
                        data[num + 1]['order'] = max(4, data[num + 1]['order'])

                    elif max(val) == 3:
                        data[num + 1]['order'] = max(3, data[num + 1]['order'])

                    elif max(val) == 2 and list(val).count(2) == 2:
                        data[num + 1]['order'] = max(2, data[num + 1]['order'])

                    elif max(val) == 2:
                        data[num + 1]['order'] = max(1, data[num + 1]['order'])

                    else:
                        data[num + 1]['order'] = 0

            else:
                val = Counter(cards).values()

                if max(val) == 5:
                    data[num + 1]['order'] = 6

                elif max(val) == 4:
                    data[num + 1]['order'] = 5

                elif max(val) == 3 and min(val) == 2:
                    data[num + 1]['order'] = 4

                elif max(val) == 3:
                    data[num + 1]['order'] = 3

                elif max(val) == 2 and list(val).count(2) == 2:
                    data[num + 1]['order'] = 2

                elif max(val) == 2:
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
