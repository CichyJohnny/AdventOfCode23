class Collisions:
    def __init__(self, input):
        self.input = open(input, 'r')
        self.data = []
        self.answer = 0

    def start(self):
        self.iterate()
        self.trajectory()

        return self.answer

    def iterate(self):
        for line in self.input:
            line = line.strip().replace(' @ ', ', ')
            arr = list(map(int, line.split(', ')))

            self.data.append(arr)

    def trajectory(self):
        data = self.data

        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                first = data[i]
                second = data[j]

                self.equations(first, second)

    def equations(self, first, second):
        x_0, y_0, z_0, x_velocity_0, y_velocity_0, z_velocity_0 = first
        x_1, y_1, z_1, x_velocity_1, y_velocity_1, z_velocity_1 = second

        a0, a1 = y_velocity_0, y_velocity_1
        b0, b1 = -x_velocity_0, -x_velocity_1
        c0, c1 = (y_velocity_0 * x_0 - x_velocity_0 * y_0), (y_velocity_1 * x_1 - x_velocity_1 * y_1)

        if a0 * b1 == a1 * b0:
            return

        xx = (c0 * b1 - c1 * b0) / (a0 * b1 - a1 * b0)
        yy = (c1 * a0 - c0 * a1) / (a0 * b1 - a1 * b0)

        minimum = 200000000000000
        maximum = 400000000000000
        if minimum <= xx <= maximum and minimum <= yy <= maximum:
            if ((xx - x_0) * x_velocity_0 >= 0 and
                (xx - x_1) * x_velocity_1 >= 0 and
                (yy - y_0) * y_velocity_0 >= 0 and
                    (yy - y_1) * y_velocity_1 >= 0):

                self.answer += 1
