from copy import deepcopy


class Platform:
    def __init__(self, input):
        self.input = open(input, 'r')
        self.data = []
        self.answer = 0
        self.memory = []

    def start(self):
        self.iterate()
        self.tilt()
        self.calculate()
        self.save()
        return self.answer

    def iterate(self):
        data = self.data

        for line in self.input:
            line = list(line.strip())
            data.append(line)

    def tilt(self):
        times = 10**9
        x = 1
        y = 0

        for i in range(times):
            self.cycle()

            if self.data not in self.memory:
                app = deepcopy(self.data)
                self.memory.append(app)

            else:
                x = i
                y = self.memory.index(self.data)

                break

        for i in range((times - y - 1) % (x - y)):
            self.cycle()

    def cycle(self):
        data = self.data
        height = len(data)
        width = len(data[0])

        for row in range(height):
            for col in range(width):
                if data[row][col] == 'O':
                    self.roll(row, col, 'North')  #

        for row in range(height):
            for col in range(width):
                if data[row][col] == 'O':
                    self.roll(row, col, 'West')

        for row in reversed(range(height)):
            for col in reversed(range(width)):
                if data[row][col] == 'O':
                    self.roll(row, col, 'South')

        for row in reversed(range(height)):
            for col in reversed(range(width)):
                if data[row][col] == 'O':
                    self.roll(row, col, 'East')

    def roll(self, row, col, dir):
        data = self.data

        data[row][col] = 'O'

        if dir == 'North' and row > 0 and not data[row - 1][col] in ['#', 'O']:
            data[row][col] = '.'

            self.roll(row - 1, col, dir)

        elif dir == 'West' and col > 0 and not data[row][col - 1] in ['#', 'O']:
            data[row][col] = '.'

            self.roll(row, col - 1, dir)

        elif dir == 'South' and row + 1 < len(data) and not data[row + 1][col] in ['#', 'O']:
            data[row][col] = '.'

            self.roll(row + 1, col, dir)

        elif dir == 'East' and col + 1 < len(data[0]) and not data[row][col + 1] in ['#', 'O']:
            data[row][col] = '.'

            self.roll(row, col + 1, dir)

    def calculate(self):
        data = self.data
        height = len(data)
        width = len(data[0])

        for row in range(height):

            for col in range(width):

                if data[row][col] == 'O':
                    self.answer += len(data) - row

    def save(self):
        data = self.data

        with open('day_14_output_part2.txt', 'w') as f:

            for line in data:
                f.write(''.join(line) + '\n')
