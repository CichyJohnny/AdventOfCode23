import sys


sys.setrecursionlimit(1000000)
class Maze:
    def __init__(self, input, output):
        self.data_file = output
        self.input = open(input, 'r')
        self.data = []
        self.max = 0
        self.answer = 0

    def start(self):
        self.iterate()
        self.findentry()
        self.save()
        print(self.data)
        return self.result()

    def save(self):
        with open(self.data_file, 'w') as file:
            for i in range(len(self.data)):
                file.write(''.join(self.data[i]) + '\n')

    def iterate(self):
        data = self.data

        for line in self.input:
            line = line.strip()
            data.append(list(line))
        print(data)

    def findentry(self):
        data = self.data
        height, width = len(data), len(data[0])

        for i in range(height):

            for j in range(width):

                if data[i][j] == 'S':
                    self.firstmaploop(i, j)
                    break


    def firstmaploop(self, i, j):
        data = self.data
        height, width = len(data), len(data[0])
        sml = self.secondmaploop

        if i > 0:
            if data[i - 1][j] == '|':
                sml(i - 1, j, '| up')
            elif data[i - 1][j] == '7':
                sml(i - 1, j, '7 up')
            elif data[i - 1][j] == 'F':
                sml(i - 1, j, 'F up')

        if i < height - 1:
            if data[i + 1][j] == '|':
                sml(i + 1, j, '| down')
            elif data[i + 1][j] == 'L':
                sml(i + 1, j, 'L down')
            elif data[i + 1][j] == 'J':
                sml(i + 1, j, 'J down')


        if j > 0:
            if data[i][j - 1] == '-':
                sml(i, j - 1, '- left')
            elif data[i][j - 1] == 'F':
                sml(i, j - 1, 'F down')
            elif data[i][j - 1] == 'L':
                sml(i, j - 1, 'L up')

        if j < width - 1:
            if data[i][j + 1] == '-':
                sml(i, j + 1, '- right')
            elif data[i][j + 1] == 'J':
                sml(i, j + 1, 'J up')
            elif data[i][j + 1] == '7':
                sml(i, j + 1, '7 down')

    def secondmaploop(self, i, j, lastsymbol, index=0):
        data = self.data
        index += 1
        data[i][j] = str(index)
        sml = self.secondmaploop




        if lastsymbol == '| up' or lastsymbol == 'J up' or lastsymbol == 'L up':
            if data[i - 1][j] == '|':
                sml(i - 1, j, '| up', index=index)
            elif data[i-1][j] == '7':
                sml(i - 1, j, '7 up', index=index)
            elif data[i-1][j] == 'F':
                sml(i - 1, j, 'F up', index=index)

        elif lastsymbol == '| down' or lastsymbol == 'F down' or lastsymbol == '7 down':
            if data[i + 1][j] == '|':
                sml(i + 1, j, '| down', index=index)
            elif data[i + 1][j] == 'J':
                sml(i + 1, j, 'J down', index=index)
            elif data[i + 1][j] == 'L':
                sml(i + 1, j, 'L down', index=index)

        elif lastsymbol == '- left' or lastsymbol == '7 up' or lastsymbol == 'J down':
            if data[i][j - 1] == '-':
                sml(i, j - 1, '- left', index=index)
            elif data[i][j - 1] == 'L':
                sml(i, j - 1, 'L up', index=index)
            elif data[i][j - 1] == 'F':
                sml(i, j - 1, 'F down', index=index)

        elif lastsymbol == '- right' or lastsymbol == 'F up' or lastsymbol == 'L down':
            if data[i][j + 1] == '-':
                sml(i, j + 1, '- right', index=index)
            elif data[i][j + 1] == 'J':
                sml(i, j + 1, 'J up', index=index)
            elif data[i][j + 1] == '7':
                sml(i, j + 1, '7 down', index=index)


    def result(self):

        return self.answer
