import sys
sys.setrecursionlimit(100000)


class Maze:
    def __init__(self, input):
        self.input = open(input, 'r')
        self.data = []
        self.max = 0
        self.path = []
        self.answer = 0

    def start(self):
        self.iterate()
        self.find_entry()
        self.clear_trash_pipes()
        self.count_enclosed_tiles(self.path)
        return self.result()

    def iterate(self):
        data = self.data

        for line in self.input:
            line = line.strip()
            data.append(list(line))

    def find_entry(self):
        data = self.data
        height, width = len(data), len(data[0])

        for i in range(height):

            for j in range(width):

                if data[i][j] == 'S':
                    self.path.append((i, j))
                    self.first_map_loop(i, j)
                    break

    def first_map_loop(self, i, j):
        data = self.data
        sml = self.second_map_loop

        if data[i - 1][j] == '|':
            sml(i - 1, j, '| up')

        elif data[i - 1][j] == '7':
            sml(i - 1, j, '7 up')

        elif data[i - 1][j] == 'F':
            sml(i - 1, j, 'F up')

        elif data[i + 1][j] == '|':
            sml(i + 1, j, '| down')

        elif data[i + 1][j] == 'L':
            sml(i + 1, j, 'L down')

        elif data[i + 1][j] == 'J':
            sml(i + 1, j, 'J down')

        elif data[i][j - 1] == '-':
            sml(i, j - 1, '- left')

        elif data[i][j - 1] == 'F':
            sml(i, j - 1, 'F down')

        elif data[i][j - 1] == 'L':
            sml(i, j - 1, 'L up')

        elif data[i][j + 1] == '-':
            sml(i, j + 1, '- right')

        elif data[i][j + 1] == 'J':
            sml(i, j + 1, 'J up')

        elif data[i][j + 1] == '7':
            sml(i, j + 1, '7 down')

    def second_map_loop(self, i, j, last_symbol, index=0):
        data = self.data
        sml = self.second_map_loop

        index += 1
        self.max = max(index, self.max)

        data[i][j] = index
        self.path.append((i, j))

        if last_symbol == '| up' or last_symbol == 'J up' or last_symbol == 'L up':
            if data[i - 1][j] == '|':
                sml(i - 1, j, '| up', index=index)

            elif data[i-1][j] == '7':
                sml(i - 1, j, '7 up', index=index)

            elif data[i-1][j] == 'F':
                sml(i - 1, j, 'F up', index=index)

        elif last_symbol == '| down' or last_symbol == 'F down' or last_symbol == '7 down':
            if data[i + 1][j] == '|':
                sml(i + 1, j, '| down', index=index)

            elif data[i + 1][j] == 'J':
                sml(i + 1, j, 'J down', index=index)

            elif data[i + 1][j] == 'L':
                sml(i + 1, j, 'L down', index=index)

        elif last_symbol == '- left' or last_symbol == '7 up' or last_symbol == 'J down':
            if data[i][j - 1] == '-':
                sml(i, j - 1, '- left', index=index)

            elif data[i][j - 1] == 'L':
                sml(i, j - 1, 'L up', index=index)

            elif data[i][j - 1] == 'F':
                sml(i, j - 1, 'F down', index=index)

        elif last_symbol == '- right' or last_symbol == 'F up' or last_symbol == 'L down':
            if data[i][j + 1] == '-':
                sml(i, j + 1, '- right', index=index)

            elif data[i][j + 1] == 'J':
                sml(i, j + 1, 'J up', index=index)

            elif data[i][j + 1] == '7':
                sml(i, j + 1, '7 down', index=index)

    def clear_trash_pipes(self):
        data = self.data
        height = len(data)
        width = len(data[0])

        for row in range(height):

            for col in range(width):

                try:
                    if data[row][col] in '|-FL7FJ':
                        data[row][col] = '.'

                except TypeError:
                    continue

    def count_enclosed_tiles(self, loop):
        area = 0
        n = len(loop)

        for i in range(n):
            j = (i + 1) % n  # Next tuple inside loop

            area += loop[i][0] * loop[j][1]
            area -= loop[j][0] * loop[i][1]

        area = abs(area) // 2
        self.answer = area - (n // 2 + 1)

    def result(self):
        answer = self.answer

        return answer
