class Garden:
    def __init__(self, input):
        self.input = open(input, 'r')
        self.data = []
        self.starting_position = (0, 0)
        self.num_of_steps = 26501365
        self.answer = 0

    def start(self):
        self.iterate()
        self.assumptions()
        self.infinity_grid_counter()

        return self.answer

    def iterate(self):
        data = self.data

        for line in self.input:
            line = list(line.strip())
            data.append(line)

        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == 'S':
                    data[i][j] = '.'
                    self.starting_position = (i, j)

    def assumptions(self):
        assert len(self.data) == len(self.data[0])  # The grid is a square
        size = len(self.data)
        x, y = self.starting_position

        assert x == y == size // 2  # The starting point is in the middle

        assert self.num_of_steps % size == size // 2  # Number of steps is equal to (x + 0.5) * size

    def make_steps(self, x, y, num_of_steps):
        data = self.data
        size = len(data)

        queue = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        in_range = []
        answer = 0
        n = 0
        while n < num_of_steps:
            current_queue = queue.copy()
            queue.clear()

            for check in current_queue:
                i, j = check

                if 0 <= i < size and 0 <= j < size:

                    if data[i][j] == '.' and (i, j) not in in_range:
                        in_range.append((i, j))
                        queue.extend([(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)])

                        if num_of_steps % 2 == 0:
                            if (((x + y) % 2 == 0 and (i + j) % 2 == 0) or
                                    ((x + y) % 2 != 0 and (i + j) % 2 != 0)):

                                answer += 1

                        else:
                            if (((x + y) % 2 == 0 and (i + j) % 2 != 0) or
                                    ((x + y) % 2 != 0 and (i + j) % 2 == 0)):

                                answer += 1

            n += 1

        return answer

    def infinity_grid_counter(self):
        fill = self.make_steps

        size = len(self.data)
        grid_width = self.num_of_steps // size - 1

        sr, sc = self.starting_position

        odd_squares = (grid_width // 2 * 2 + 1) ** 2
        even_squares = ((grid_width + 1) // 2 * 2) ** 2

        odd_points = self.make_steps(size // 2, size // 2, size * 2 + 1)
        even_points = self.make_steps(size // 2, size // 2, size * 2)
        full_squares = odd_squares * odd_points + even_squares * even_points

        corner_t = fill(size - 1, sc, size - 1)
        corner_r = fill(sr, 0, size - 1)
        corner_b = fill(0, sc, size - 1)
        corner_l = fill(sr, size - 1, size - 1)
        corners = corner_t + corner_r + corner_b + corner_l

        small_tr = fill(size - 1, 0, size // 2 - 1)
        small_tl = fill(size - 1, size - 1, size // 2 - 1)
        small_br = fill(0, 0, size // 2 - 1)
        small_bl = fill(0, size - 1, size // 2 - 1)
        smalls = (grid_width + 1) * (small_tr + small_tl + small_br + small_bl)

        large_tr = fill(size - 1, 0, size * 3 // 2 - 1)
        large_tl = fill(size - 1, size - 1, size * 3 // 2 - 1)
        large_br = fill(0, 0, size * 3 // 2 - 1)
        large_bl = fill(0, size - 1, size * 3 // 2 - 1)
        larges = grid_width * (large_tr + large_tl + large_br + large_bl)

        self.answer = full_squares + corners + smalls + larges
