same_height = 5
diff_height = 10

input_state = input()

temp = ""

total_height = 0
for i in range(len(input_state)):
    if (i == 0):
        total_height += 10
    elif (input_state[i] == temp):
        total_height += same_height
    else:
        total_height += diff_height
    temp = input_state[i]

print(total_height)