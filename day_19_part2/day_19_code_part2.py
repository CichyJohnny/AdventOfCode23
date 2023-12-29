import re


class Workflow:
    def __init__(self, input):
        self.input = open(input, 'r')
        self.flow = {}
        self.ranges = {key: (1, 4000) for key in "xmas"}

    def start(self):
        self.iterate()

        return self.solve(self.ranges)

    def iterate(self):
        flow = self.flow
        flow_list = []

        for line in self.input:
            line = line.strip()

            if len(line) == 0:
                break

            flow_list.append(line)

        for x in flow_list:
            x = re.split('{|}', x)

            conditions = x[1].split(',')
            leftover = conditions.pop()

            conditions_list = []
            for cond in conditions:
                key = cond[0]
                cmp = cond[1]

                sec = cond[2:].split(':')

                n = int(sec[0])
                target = sec[1]

                conditions_list.append((key, cmp, n, target))

            flow[x[0]] = (conditions_list, leftover)

    def solve(self, ranges, name="in"):
        if name == "R":
            return 0

        if name == "A":
            product = 1

            for low, high in ranges.values():
                product *= high - low + 1

            return product

        rules, leftover = self.flow[name]

        total = 0

        for key, cmp, n, target in rules:
            low, high = ranges[key]

            if cmp == '<':
                passed = (low, min(n - 1, high))
                left = (max(n, low), high)

            elif cmp == '>':
                passed = (max(n + 1, low), high)
                left = (low, min(n, high))

            if passed[0] <= passed[1]:
                copy = dict(ranges)
                copy[key] = passed

                total += self.solve(copy, target)

            if left[0] <= left[1]:
                ranges = dict(ranges)
                ranges[key] = left

            else:
                break

        else:
            total += self.solve(ranges, leftover)

        return total
