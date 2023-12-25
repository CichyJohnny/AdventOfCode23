class HotSprings:
    def __init__(self, input):
        self.input = open(input, 'r')
        self.data = {}
        self.answer = 0

    def start(self):
        self.iterate()
        self.solve()

        return self.answer

    def iterate(self):
        data = self.data

        i = 0
        for line in self.input:
            line = line.strip().split()
            data[i] = [line[0], line[1].split(',')]
            i += 1

    def solve(self):
        data = self.data

        for line in data.values():
            string = line[0]
            string += '.'

            search_values = [int(i) for i in line[1]]
            search_values.append(0)

            n = len(string)
            m = len(search_values)
            m_max = max(search_values)

            dp = [[[None for _ in range(m_max + 1)] for _ in range(m)] for _ in range(n)]

            for i in range(n):
                x = string[i]

                for j in range(m):

                    for k in range(search_values[j] + 1):

                        if i == 0:

                            if j != 0:
                                dp[i][j][k] = 0

                                continue

                            if x == '#':
                                if k != 1:
                                    dp[i][j][k] = 0

                                else:
                                    dp[i][j][k] = 1

                                continue

                            if x == '.':
                                if k != 0:
                                    dp[i][j][k] = 0
                                else:
                                    dp[i][j][k] = 1

                                continue

                            if x == '?':
                                if k not in [0, 1]:
                                    dp[i][j][k] = 0

                                else:
                                    dp[i][j][k] = 1

                                continue

                        if k != 0:
                            ans_dot = 0

                        elif j > 0:
                            ans_dot = dp[i-1][j-1][search_values[j-1]]
                            ans_dot += dp[i-1][j][0]

                        else:
                            if string[:i].count('#') == 0:
                                ans_dot = 1

                            else:
                                ans_dot = 0

                        if k == 0:
                            ans_pound = 0

                        else:
                            ans_pound = dp[i-1][j][k-1]

                        if x == '.':
                            dp[i][j][k] = ans_dot

                        elif x == '#':
                            dp[i][j][k] = ans_pound

                        else:
                            dp[i][j][k] = ans_dot + ans_pound

            self.answer += dp[-1][-1][0]
