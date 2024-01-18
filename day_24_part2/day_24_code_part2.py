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
        eq = []

        for i in range(len(data)):

            x_0, y_0, z_0, x_v_0, y_v_0, z_v_0 = data[i]
            x_r, y_r, z_r, x_v_r, y_v_r, z_v_r = sympy.symbols('x_r y_r z_r x_v_r y_v_r z_v_r')

            eq.extend([
                (x_r - x_0) * (y_v_0 - y_v_r) - (y_r - y_0) * (x_v_0 - x_v_r),
                (y_r - y_0) * (z_v_0 - z_v_r) - (z_r - z_0) * (y_v_0 - y_v_r)
            ])

            if i < 2:
                continue

            answers = [sol for sol in sympy.solve(eq) if all(x % 1 == 0 for x in sol.values())]

            if len(answers) == 1:
                break

        x, vx, y, vy, z, vz = answers[0].values()

        self.answer = x + y + z
