from day_02_code import Games

# In day_02_input.txt put your unique input
file = open('day_02_input.txt', 'r')

answer = Games().start(file)

print(answer)