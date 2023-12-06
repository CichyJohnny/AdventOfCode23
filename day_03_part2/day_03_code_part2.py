class NeighboursNums:
    def __init__(self, path):
        self.file_path = path
        self.file = open(self.file_path, 'r')
        self.signs = ['*']
        self.mat = []
        self.possible_answers = []
        self.answers = []

    def start(self):
        self.matrix()
        self.iterate()
        return self.result()

    def matrix(self):
        mat = self.mat

        for line in self.file:
            mat.append([])
            text = line.strip()

            for char in text:
                mat[-1].append(char)

        self.file.close()

    def iterate(self):
        mat = self.mat

        for row in range(len(mat)):

            for char in range(len(mat[row])):
                x = mat[row][char]

                if x in self.signs:
                    self.lookfor(row, char)

    def lookfor(self, row, char):
        mat = self.mat
        vectors = [-1, 0, 1]

        for i in vectors:

            for j in vectors:

                if not i == j == 0:
                    a, b = row + i, char + j
                    check = mat[a][b]

                    if check.isnumeric():
                        self.calculate(a, b)

        if len(self.possible_answers) == 2:
            a, b = self.possible_answers
            answer = a * b
            self.answers.append(answer)

        self.possible_answers.clear()

    def calculate(self, row, char):
        mat = self.mat
        maxlength = len(mat[row])
        digits = [mat[row][char]]
        mat[row][char] = '.'

        x = 1
        while char - x >= 0 and mat[row][char - x].isnumeric() and mat[row][char - x] != '.':
            digits.insert(0, mat[row][char - x])
            mat[row][char - x] = '.'
            x += 1

        x = 1
        while char + x < maxlength and mat[row][char + x].isnumeric() and mat[row][char + x] != '.':
            digits.append(mat[row][char + x])
            mat[row][char + x] = '.'
            x += 1

        answer = int(''.join(digits))
        self.possible_answers.append(answer)

    def result(self):
        answer = sum(self.answers)
        return answer
