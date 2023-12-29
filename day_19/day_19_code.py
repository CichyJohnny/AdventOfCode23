import re


class Workflow:
    def __init__(self, input):
        self.input = open(input, 'r')
        self.flow = {}
        self.ratings = {}
        self.As = []
        self.Rs = []

    def start(self):
        self.iterate()
        self.solve()

        return self.result()

    def iterate(self):
        flow = self.flow
        flow_list = []

        ratings = self.ratings
        ratings_list = []

        var = True
        for line in self.input:
            line = line.strip()

            if len(line) == 0:
                var = False
                continue

            if var:
                flow_list.append(line)

            else:
                ratings_list.append(line)

        for x in flow_list:
            x = re.split('{|}', x)[:-1]
            name = x[0]
            flow[name] = {}

            conditions = x[1].split(',')

            for i in conditions:
                i = i.split(':')

                if len(i) == 2:
                    flow[name][i[0]] = i[1]

                elif len(i) == 1:
                    flow[name]['True'] = i[0]

        i = 0
        for x in ratings_list:
            x = x[1:-1].split(',')
            ratings[i] = []

            for val in x:
                val = val.split('=')
                ratings[i].append(val[1])

            i += 1

    def solve(self):
        flow = self.flow
        ratings = self.ratings

        for rating in ratings.values():
            rating = list(map(int, rating))
            x, m, a, s = rating

            destination = 'in'
            while True:

                if destination == 'A':
                    self.As.append(rating)
                    break

                elif destination == 'R':
                    self.Rs.append(rating)
                    break

                conditions = flow[destination]

                for expression, direction in conditions.items():

                    if eval(expression, {'x': x, 'm': m, 'a': a, 's': s}):
                        destination = direction
                        break

    def result(self):
        answer = 0

        for x in self.As:
            answer += sum(x)

        return answer
