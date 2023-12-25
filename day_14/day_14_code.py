class Platform:
    def __init__(self, input):
        self.input = open(input, 'r')
        self.data = []
        self.answer = 0

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
        data = self.data
        height = len(data)
        width = len(data[0])

        for row in range(height):

            for col in range(width):

                if data[row][col] == 'O':
                    self.roll(row, col)

    def roll(self, row, col):
        data = self.data
        data[row][col] = 'O'

        if row > 0 and not data[row - 1][col] in ['#', 'O']:
            data[row][col] = '.'

            self.roll(row - 1, col)

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

        with open('day_14_output.txt', 'w') as f:

            for line in data:
                f.write(''.join(line) + '\n')