input_H, input_M, input_S = map(int, input().split(" "))
new_S = int(input())

add_to_hour = int(new_S / 3600)
add_to_min = int((new_S - 3600 * add_to_hour) / 60)
add_to_sec = new_S - (add_to_hour * 3600 + add_to_min * 60)

res_H = input_H + add_to_hour
res_M = input_M + add_to_min
res_S = input_S + add_to_sec

if (res_S >= 60):
    res_M += 1
    res_S = res_S - 60

if (res_M >= 60):
    res_H += 1
    res_M = res_M - 60

if (res_H >= 24):
    res_H = res_H % 24
print(f"{res_H} {res_M} {res_S}", end="")
