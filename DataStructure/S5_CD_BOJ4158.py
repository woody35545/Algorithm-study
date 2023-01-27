import sys


def solve():
    while (True):
        N, M = [int(x) for x in sys.stdin.readline().rstrip().split(" ")]
        if (N == 0 and M == 0):
            break
        else:
            As_CD = [0] * N
            Bs_CD = [0] * M

            for i in range(N):
                As_CD[i] = int(sys.stdin.readline().rstrip())
            for i in range(M):
                Bs_CD[i] = int(sys.stdin.readline().rstrip())

            As_CD_set = set(As_CD)
            Bs_CD_set = set(Bs_CD)

            print(len(As_CD_set & Bs_CD_set))
            # exit_code_1, exit_code_2 = [int(x) for x in sys.stdin.readline().rstrip().split(" ")]
            # if (exit_code_1 == 0 and exit_code_2 == 0):
            #    break


solve()
