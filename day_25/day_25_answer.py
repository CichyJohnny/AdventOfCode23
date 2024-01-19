from day_25_code import GraphSeparation

# In day_25_input.txt put your unique input
input = 'day_25_input.txt'

answer = GraphSeparation(input).start()

print(answer)

# The method is much slower because of sympy library, but I like the simplicity it adds
