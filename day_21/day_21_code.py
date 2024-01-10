class Garden:
    def __init__(self, input):
        self.input = open(input, 'r')
        self.data = []
        self.answer = 0

    def start(self):
        self.iterate()
        self.make_n_steps(64)
        self.result()

        return self.answer

    def iterate(self):
        data = self.data

        for line in self.input:
            line = list(line.strip())
            data.append(line)

        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == 'S':
                    data[i][j] = 'O'

    def make_n_steps(self, n):
        for _ in range(n):
            self.step()

    def step(self):
        data = self.data
        height = len(data)
        width = len(data[0])

        queue = []

        for i in range(height):
            for j in range(width):
                if data[i][j] == 'O':
                    queue.extend([(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)])
                    data[i][j] = '.'

        while queue:
            x, y = queue.pop(0)
            if 0 <= x < height and 0 <= y < width:
                if data[x][y] == '.':
                    self.data[x][y] = 'O'

    def result(self):
        data = self.data

        for line in data:
            self.answer += line.count('O')
