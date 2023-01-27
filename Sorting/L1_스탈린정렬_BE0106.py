# [23.01.06] 어디서 틀린 것인지 계속 고민했는데 결과 출력문에서 테스트케이스 하나가 끝날 때마다 줄바꿈하여 출력하도록 했더니 정답처리 되었다..

A = []  # global var for recursive method
def check_sorted(pList) -> int:
    #print("> check_sorted()")
    #print("> > pList: " + str(pList))
    for i in range(len(pList)-1):
        #print("> > pList[" + str(i) + "] = " + str(pList[i]) + ", pList[" + str(i + 1) + "] = " + str(pList[i + 1]))
        if pList[i] > pList[i+1]:
            #print("> > pList[" +str(i)+ "] > pList[" + str(i+1) + "] // " + str(pList[i]) + " > " + str(pList[i+1]))
            #print("> > sort needed!\n")
            return False

    #print("> > pList[" + str(i) + "] < pList[" + str(i + 1) + "] // " + str(pList[i]) + " < " + str(pList[i+1]))
    #print("> > sort complete!\n")
    return True

def sort(pList):
    for i in range(len(pList)-1):
        if pList[i] > pList[i+1]:
            pList.pop(i+1)
            break

    # after sorting phase finish, check if there's more element to sort
    if not check_sorted(pList):
        # if exists, sort again by recursive function call
        sort(pList)

def solve():
    global A
    sort(A)

    for i in range(len(A)):
        if i != len(A) -1:
            print(A[i], end=" ")
        else:
            print(A[i])
    # initialize A for next testing
    A = []


T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int, input().split(" ")))
    solve()

