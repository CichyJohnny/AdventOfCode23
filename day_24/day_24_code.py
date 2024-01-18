import sympy


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
        x_0, y_0, z_0, x_v_0, y_v_0, z_v_0 = first
        x_1, y_1, z_1, x_v_1, y_v_1, z_v_1 = second

        px, py = sympy.symbols('px py')
        roots = sympy.solve([y_v_0 * (px - x_0) - x_v_0 * (py - y_0),
                             y_v_1 * (px - x_1) - x_v_1 * (py - y_1)])

        if not roots:
            return

        x = roots[px]
        y = roots[py]

        minimum = 7
        maximum = 27
        if minimum <= x <= maximum and minimum <= y <= maximum:
            if ((x - x_0) * x_v_0 >= 0 and
                (x - x_1) * x_v_1 >= 0 and
                (y - y_0) * y_v_0 >= 0 and
                    (y - y_1) * y_v_1 >= 0):

                self.answer += 1
