class Signals:
    def __init__(self, input):
        self.input = open(input, 'r')
        self.data = {}
        self.conjunctions = {}
        self.high_signals = 0
        self.low_signals = 0
        self.answer = 0

    def start(self):
        self.iterate()
        self.repeat(1000)

        return self.answer

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

    def repeat(self, n):
        for i in range(n):
            self.solve()

            if_repeated = []
            for values in self.data.values():
                if_repeated.append(values[2])

            if 1 not in if_repeated:
                num_after_cycle = i + 1

                break

        else:
            num_after_cycle = n

        times_cycled = n // num_after_cycle
        times_left = n % num_after_cycle

        self.answer = (self.high_signals * self.low_signals) * times_cycled ** 2

        self.high_signals, self.low_signals = 0, 0

        for i in range(times_left):
            self.solve()

        self.answer += self.high_signals * self.low_signals

    def solve(self):
        data = self.data

        queue = [('broadcaster', 0)]

        high_signals = 0
        low_signals = 1

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

                else:
                    value = 0

            data[curr][2] = value

            if value == 1:
                high_signals += len(current_queue)
            else:
                low_signals += len(current_queue)

            for x in current_queue:
                queue.append((x, value))

        self.high_signals += high_signals
        self.low_signals += low_signals
