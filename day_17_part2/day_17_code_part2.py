from heapq import heappop, heappush as push


class FindMinPath:
    def __init__(self, input):
        self.input = open(input, 'r')
        self.data = {}
        self.answer = 0
        self.excluded = set()

    def start(self):
        self.iterate()
        self.find(4, 10, [*self.data][-1], 0)

        return self.answer

    def iterate(self):
        data = {(i, j): int(value)
                for i, string in enumerate(open('day_17_input_part2.txt'))
                for j, value in enumerate(string.strip())}
        self.data = data

    def find(self, min_step, max_step, end, x):
        data = self.data
        excluded = self.excluded

        queue = [(0, 0, (0, 0), (1, 0)), (0, 0, (0, 0), (0, 1))]  # (value, counter, position, direction)

        while queue:
            value, _, position, direction = heappop(queue)

            if position == end:
                self.answer = value
                return

            if (position, direction) not in excluded:

                excluded.add((position, direction))

                # Directions perpendicular to the current direction
                for d in [(direction[1], -direction[0]), (-direction[1], direction[0])]:
                    for i in range(min_step, max_step + 1):
                        new_pos = (position[0] + d[0] * i, position[1] + d[1] * i)

                        if new_pos in data:
                            v = sum(data[(position[0] + d[0] * j, position[1] + d[1] * j)] for j in range(1, i + 1))

                            push(queue, (value + v, (x := x + 1), new_pos, d))
