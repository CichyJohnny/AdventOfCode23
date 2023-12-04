class FirstAndLast:
    def reading(file):
        answer = 0
        for line in file:
            nums = []
            for char in line:
                if char.isnumeric():
                    nums.append(char)
            answer += int(nums[0] + nums[-1])
        return answer
