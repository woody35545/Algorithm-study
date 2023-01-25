N = int(input())
sebatdons = list(map(int,input().split(" ")))
sebatdons_sorted = sorted(sebatdons)

for i in range(N):
    idx = sebatdons_sorted.index(sebatdons[i])
    print(f"{idx} {len(sebatdons)-idx-1}")
