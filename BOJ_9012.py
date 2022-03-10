N = int(input())

stack = [""] * 50
max_size = 50
size = 0
top = -1


def push(_value):
    global stack, max_size, size, top
    if (size < max_size):
        stack[size] = _value
        size += 1
        top = size - 1


def pop():
    global size, top
    return_value = stack[top]
    size -= 1
    top = size - 1
    return return_value


def reset_stack():
    global stack, size, top
    stack = [""] * 50
    size = 0
    top = -1


for i in range(N):
    reset_stack()
    input_line = input()
    Close_Before_Open = False
    for j in range(len(input_line)):
        if (input_line[j] == "("):
            push(input_line[j])
        elif (input_line[j] == ")"):
            if (size != 0):
                pop()
            else:
                Close_Before_Open = True

    if (size == 0 and not Close_Before_Open):
        print("YES")
    else:
        print("NO")
