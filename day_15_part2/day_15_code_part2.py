class HashAlgorithm:
    def __init__(self, input):
        self.input = open(input, 'r')
        self.data = ''
        self.answer = 0
        self.boxes = {i: {} for i in range(256)}

    def start(self):
        self.iterate()
        self.solve()
        self.calculate()

        return self.answer

    def iterate(self):
        data = self.input.read()
        data = data.split(',')

        self.data = data

    def solve(self):
        data = self.data
        boxes = self.boxes

        for string in data:
            current_value = 0

            if string[-2] == '=':
                label = string[:-2]

                for char in label:
                    current_value += ord(char)
                    current_value *= 17
                    current_value = current_value % 256

                boxes[current_value][label] = int(string[-1])

            elif string[-1] == '-':
                label = string[:-1]

                for char in label:
                    current_value += ord(char)
                    current_value *= 17
                    current_value = current_value % 256

                if label in boxes[current_value].keys():
                    boxes[current_value].pop(label)

    def calculate(self):
        boxes = self.boxes

        for num_box, box in boxes.items():

            for slot, lens in enumerate(box.values()):
                ans = (num_box + 1) * (slot + 1) * lens

                self.answer += int(ans)
