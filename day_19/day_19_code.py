class Digging:
    def __init__(self, input):
        self.input = open(input, 'r')
        self.data = {}
        self.answer = 0

    def start(self):
        self.iterate()
        self.count_enclosed_tiles()

        return self.answer

    def iterate(self):
        data = self.data

        loc = (0, 0)
        for line in self.input:
            line = line.split()

            steps = int(line[1])
            direction = line[0]

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
