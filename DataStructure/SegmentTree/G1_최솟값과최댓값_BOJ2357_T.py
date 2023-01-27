N, M = map(int,input().split(" "))
nums = [0]*(N+1)
for i in range(1,N+1):
    nums[i] = int(input())

#print(nums)

def solve(a,b):
    sliced_nums = nums[a: b+1]
    sliced_nums.sort()
    min = sliced_nums[0]
    max = sliced_nums[-1]
    return min,max

for j in range(M):
    a,b = map(int,input().split(" "))
    min,max = solve(a,b)
    print(str(min) + " " + str(max))