class FindMaxPath:
    def __init__(self, input):
        self.input = open(input, 'r')
        self.data = []
        self.graph = {}
        self.nodes = []
        self.answer = 0

    def start(self):
        self.iterate()
        self.make_graph()
        self.brute_force_path()

        return self.answer

    def iterate(self):
        data = self.data

        for line in self.input:
            data.append(list(line.strip()))

        start = (0, data[0].index('.'))
        end = (len(data) - 1, data[-1].index('.'))
        self.nodes.extend([start, end])

        for i in range(len(data)):
            for j in range(len(data[0])):
                total = 0

                if data[i][j] != '#':

                    for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        if (0 <= i+x < len(data) and 0 <= j+y < len(data[0])) and data[i+x][j+y] != '#':
                            total += 1

                if total >= 3:
                    self.nodes.append((i, j))

    def make_graph(self):
        data = self.data
        nodes = self.nodes

        graph = {pt: {} for pt in nodes}

        dirs = {
            '^': [(-1, 0), (1, 0)],
            'v': [(1, 0), (-1, 0)],
            '<': [(0, -1), (0, 1)],
            '>': [(0, 1), (0, -1)],
            '.': [(-1, 0), (1, 0), (0, -1), (0, 1)]
        }

        for sr, sc in nodes:
            stack = [(0, sr, sc)]
            seen = {(sr, sc)}

            while stack:
                n, r, c = stack.pop()

                if n != 0 and (r, c) in nodes:
                    graph[(sr, sc)][(r, c)] = n
                    continue

                for dr, dc in dirs[data[r][c]]:
                    nr = r + dr
                    nc = c + dc

                    if (0 <= nr < len(data) and 0 <= nc < len(data[0])
                            and data[nr][nc] != '#' and (nr, nc) not in seen):
                        stack.append((n + 1, nr, nc))
                        seen.add((nr, nc))

        self.graph = graph

    def brute_force_path(self):
        graph = self.graph

        start = tuple(graph.keys())[0]
        end = tuple(graph.keys())[1]


        stack = [(0, start, set())]
        while stack:
            n, rc, exc = stack.pop()

            if rc in exc:
                continue
            exc.add(rc)

            if rc == end:
                self.answer = max(self.answer, n)

            directions = graph[rc]

            for next, length in directions.items():
                stack.append((n + length, next, set(exc)))
