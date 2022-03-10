N = int(input())

cute_voted = 0
not_cute_voted = 0
for i in range(N):
     vote = int(input())
     if (vote == 1):
         cute_voted += 1
     else:
         not_cute_voted += 1

if(cute_voted > not_cute_voted):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")