class Bricks:
    def __init__(self, input):
        self.input = open(input, 'r')
        self.data = []
        self.answer = 0

    def start(self):
        self.iterate()
        self.fall()
        self.supports()

        return self.answer

    def iterate(self):
        for line in self.input:
            line = line.strip().split('~')
            start, end = list(map(int, line[0].split(','))), list(map(int, line[1].split(',')))
            self.data.append((start + end))

        self.data = sorted(self.data, key=lambda x: x[2])

    def overlap(self, x, y):
        condition = (max(x[0], y[0]) <= min(x[3], y[3]) and
                     max(x[1], y[1]) <= min(x[4], y[4]))

        return condition

    def fall(self):
        data = self.data

        for index, brick in enumerate(data):
            max_z = 1

            for check in data[:index]:

                if self.overlap(brick, check):
                    max_z = max(max_z, check[5] + 1)

            brick[5] -= brick[2] - max_z
            brick[2] = max_z

    def supports(self):
        data = sorted(self.data, key=lambda x: x[2])

        k_supports_v = {i: set() for i in range(len(data))}
        v_supports_k = {i: set() for i in range(len(data))}

        for j, upper in enumerate(data):

            for i, lower in enumerate(data[:j]):

                overlap = self.overlap(lower, upper)

                if overlap and upper[2] == lower[5] + 1:
                    k_supports_v[i].add(j)
                    v_supports_k[j].add(i)

        total = 0
        for i in range(len(data)):

            if all(len(v_supports_k[j]) >= 2 for j in k_supports_v[i]):
                total += 1

        self.answer = total
