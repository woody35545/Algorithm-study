def solve():
    counts_of_numbers = [0] * 10

    N = (input())
    for i in range(1, int(N)+1):
        for j in range(len(str(i))):
            # 321
            for k in range(10):
                if (str(i))[j] == str(k):
                    counts_of_numbers[k] += 1

  #  for i in range(len(counts_of_numbers)):
      #  print(str(i) + ">> " + str(counts_of_numbers[i]) + "개 ")


    # ANSWER
    for i in range(len(counts_of_numbers)):
        print(str(counts_of_numbers[i]), end ="")
        if i != len(counts_of_numbers) -1 :
            print(" ", end ="")


solve()
