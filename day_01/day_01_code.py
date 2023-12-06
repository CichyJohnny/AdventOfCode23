class FirstAndLast:
    def __init__(self, path):
        self.file = open(path, 'r')

    def reading(self):
        answer = 0

        for line in self.file:
            nums = []

            for char in line:

                if char.isnumeric():
                    nums.append(char)

            answer += int(nums[0] + nums[-1])

        return answer
