A_voted = 0
B_voted = 0

V = int(input())
vote = input()

for i in range(V):
    if(vote[i] == "A"):
        A_voted += 1
    else:
        B_voted += 1

if(A_voted > B_voted):
    print("A")
elif(A_voted == B_voted):
    print("Tie")
else:
    print("B")