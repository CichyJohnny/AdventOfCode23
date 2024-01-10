class Garden:
    def __init__(self, input):
        self.input = open(input, 'r')
        self.data = []
        self.answer = 0

    def start(self):
        self.iterate()
        self.step(64)

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

    def step(self, num_of_steps):
        data = self.data
        height = len(data)
        width = len(data[0])

        queue = []

        for i in range(height):
            for j in range(width):
                if data[i][j] == 'O':
                    data[i][j] = '.'

                    x, y = i, j
                    queue.extend([(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)])

        in_range = []
        n = 0
        while n < num_of_steps:
            current_queue = queue.copy()
            queue.clear()

            for check in current_queue:
                i, j = check
                base_i, base_j = i % height, j % width

                if data[base_i][base_j] == '.' and (i, j) not in in_range:
                    in_range.append((i, j))
                    queue.extend([(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)])

                    if num_of_steps % 2 == 0:
                        if (((x + y) % 2 == 0 and (i + j) % 2 == 0) or
                                ((x + y) % 2 != 0 and (i + j) % 2 != 0)):

                            self.answer += 1

                    else:
                        if (((x + y) % 2 == 0 and (i + j) % 2 != 0) or
                                ((x + y) % 2 != 0 and (i + j) % 2 == 0)):

                            self.answer += 1

            n += 1
