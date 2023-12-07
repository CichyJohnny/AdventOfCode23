class FirstAndLast:
    def __init__(self, path):
        self.file = open(path, 'r')
        self.words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        self.reversed_words = ['eno', 'owt', 'eerht', 'ruof', 'evif', 'xis', 'neves', 'thgie', 'enin']
        self.answers = []

    def start(self):
        self.reading()

        return self.result()

    def reading(self):

        for line in self.file:

            num1 = self.gofromleft(line)
            num2 = self.gofromright(line)

            num = int(num1 + num2)
            self.answers.append(num)

    def gofromleft(self, line):
        num1 = ''
        sequence = ''
        var = False

        for char in line:

            if char.isnumeric():
                num1 = char
                break

            else:
                sequence += char

                for word in self.words:

                    if word in sequence:
                        num1 = str(self.words.index(word) + 1)
                        var = True
                        break
            if var:
                break

        return num1

    def gofromright(self, line):
        num2 = ''
        sequence = ''
        var = False
        line = line[::-1]

        for char in line:

            if char.isnumeric():
                num2 = char
                break

            else:
                sequence += char

                for word in self.reversed_words:

                    if word in sequence:
                        num2 = str(self.reversed_words.index(word) + 1)
                        var = True
                        break
            if var:
                break

        return num2

    def result(self):
        answer = sum(self.answers)

        return answer
