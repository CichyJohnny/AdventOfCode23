class HashAlgorithm:
    def __init__(self, input):
        self.input = open(input, 'r')
        self.data = ''
        self.answer = 0

    def start(self):
        self.iterate()
        self.solve()

        return self.answer

    def iterate(self):
        data = self.input.read()
        data = data.split(',')

        self.data = data

    def solve(self):
        data = self.data

        for string in data:

            current_value = 0
            for char in string:

                current_value += ord(char)
                current_value *= 17
                current_value = current_value % 256

            self.answer += current_value
