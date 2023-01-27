
# remain list
remain = [0] * 10
size_of_remain = 0

def isExist(_value):
    global remain
    for k in range(size_of_remain):
        if remain[k] == _value:
            return True

    return False

def solve():
    global remain,size_of_remain
    # init input
    for i in range(10):
        input_int = int(input())
        if not isExist(input_int % 42):
            remain[size_of_remain] = (input_int % 42)
            size_of_remain += 1
        else:
            None

    # init complete
    print(size_of_remain)

solve()


