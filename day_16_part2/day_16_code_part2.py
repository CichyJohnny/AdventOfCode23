import sys

sys.setrecursionlimit(10**6)


class LaserBeams:
    def __init__(self, input):
        self.input = open(input, 'r')
        self.data = []
        self.memory = set()
        self.excluded = []
        self.answer = []

    def start(self):
        self.iterate()
        self.solve()

        return max(self.answer)

    def iterate(self):
        data = self.data

        for line in self.input:
            line = list(line.strip())
            data.append(line)

    def solve(self):
        data = self.data
        height = len(data)
        width = len(data[0])

        for i in range(height):  # Left edge
            self.track('r', i, 0)
            self.result()

        for j in range(width):  # Bottom edge
            self.track('u', height - 1, j)

            self.result()

        for i in range(height):  # Right edge
            self.track('l', i, width - 1)

            self.result()

        for j in range(width):  # Top edge
            self.track('d', 0, j)

            self.result()

    def track(self, dir='r', i=0, j=0):
        data = self.data
        height = len(data)
        width = len(data[0])

        if (i < 0) or (i == height) or (j < 0) or (j == width):
            return

        if (dir, i, j) in self.excluded:
            return

        self.excluded.append((dir, i, j))

        self.memory.add((i, j))

        if data[i][j] == '.':
            if dir == 'r':
                self.track(dir, i, j + 1)

            elif dir == 'l':
                self.track(dir, i, j - 1)

            elif dir == 'u':
                self.track(dir, i - 1, j)

            elif dir == 'd':
                self.track(dir, i + 1, j)

        elif data[i][j] == '\\':
            if dir == 'r':
                self.track('d', i + 1, j)

            elif dir == 'l':
                self.track('u', i - 1, j)

            elif dir == 'u':
                self.track('l', i, j - 1)

            elif dir == 'd':
                self.track('r', i, j + 1)

        elif data[i][j] == '/':
            if dir == 'r':
                self.track('u', i - 1, j)

            elif dir == 'l':
                self.track('d', i + 1, j)

            elif dir == 'u':
                self.track('r', i, j + 1)

            elif dir == 'd':
                self.track('l', i, j - 1)

        elif data[i][j] == '|':
            if dir == 'r' or dir == 'l':
                self.track('u', i - 1, j)
                self.track('d', i + 1, j)

            elif dir == 'u':
                self.track(dir, i - 1, j)

            elif dir == 'd':
                self.track(dir, i + 1, j)

        elif data[i][j] == '-':
            if dir == 'u' or dir == 'd':
                self.track('l', i, j - 1)
                self.track('r', i, j + 1)

            elif dir == 'l':
                self.track(dir, i, j - 1)

            elif dir == 'r':
                self.track(dir, i, j + 1)

    def result(self):
        answer = len(self.memory)
        self.memory.clear()
        self.excluded.clear()

        self.answer.append(answer)
