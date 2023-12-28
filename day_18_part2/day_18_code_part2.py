class Digging:
    def __init__(self, input):
        self.input = open(input, 'r')
        self.data = {}
        self.answer = 0

    def start(self):
        self.iterate()
        self.count_enclosed_tiles()

        return self.answer

    def from_hex_to_decimal(self, x):
        x = x[::-1]
        dec = 0
        ids = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

        for i in range(len(x)):
            dec += ids.index(x[i]) * 16**i

        return dec

    def iterate(self):
        data = self.data

        loc = (0, 0)
        for line in self.input:
            line = line.split()

            x = line[2][2:-1]
            steps = self.from_hex_to_decimal(x[:-1])

            dirs = ['R', 'D', 'L', 'U']
            direction = dirs[int(x[-1])]

            data[loc] = line[2]

            if direction == 'R':
                loc = (loc[0], loc[1] + steps)

            elif direction == 'L':
                loc = (loc[0], loc[1] - steps)

            elif direction == 'U':
                loc = (loc[0] - steps, loc[1])

            elif direction == 'D':
                loc = (loc[0] + steps, loc[1])

    def count_enclosed_tiles(self):
        loop = list(self.data.keys())

        area = 0
        n = len(loop)

        length = 0
        for i in range(n):
            j = (i + 1) % n  # Next tuple inside loop

            length += abs(loop[i][0] - loop[j][0]) + abs(loop[i][1] - loop[j][1])
            area += loop[i][0] * loop[j][1]
            area -= loop[j][0] * loop[i][1]

        area = abs(area) // 2

        self.answer = area + length // 2 + 1
