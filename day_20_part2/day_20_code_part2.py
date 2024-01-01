from math import lcm


class Signals:
    def __init__(self, input):
        self.input = open(input, 'r')
        self.data = {}
        self.conjunctions = {}
        self.i = 0
        self.before_before_rx = []
        self.answer = []

    def start(self):
        self.iterate()
        self.repeat()

        return lcm(*self.answer)

    def iterate(self):
        data = self.data

        for line in self.input:
            line = line.strip()
            line = line.split(' -> ')

            if line[0] == 'broadcaster':
                sign = None
                name = line[0]

            else:
                sign = line[0][0]
                name = line[0][1:]

                if sign == '&' and name not in self.conjunctions.keys():
                    self.conjunctions[name] = []

            direction = line[1].split(', ')

            data[name] = [sign, direction, 0]

        for input_key, values in data.items():
            for output_key in values[1]:
                if output_key in self.conjunctions.keys():
                    self.conjunctions[output_key].append(input_key)

    def repeat(self):

        before_rx = [x for x, y in self.data.items() if 'rx' in y[1]]
        self.before_before_rx = [x for x, y in self.data.items() if before_rx[0] in y[1]]

        while self.before_before_rx:
            self.i += 1
            self.solve()

    def solve(self):
        data = self.data

        queue = [('broadcaster', 0)]

        while queue:
            curr, sent = queue.pop(0)

            try:
                sign, current_queue, value = data[curr]
            except KeyError:
                continue

            if sign == '%':
                if sent == 0:
                    value = 1 - value

                elif sent == 1:
                    continue

            elif sign == '&':
                check_for = self.conjunctions[curr]
                input_values = []

                for input_key in check_for:
                    input_values.append(self.data[input_key][2])

                if 0 in input_values:
                    value = 1

                    if curr in self.before_before_rx:
                        self.answer.append(self.i)
                        self.before_before_rx.remove(curr)

                else:
                    value = 0

            data[curr][2] = value

            for x in current_queue:
                queue.append((x, value))
