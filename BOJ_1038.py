import itertools

test_list = ['a','b','c']
comb_list = list(itertools.combinations((test_list),2 ))

res_list = [0]*100

for i in range(len(test_list)):
        res_list[i] += test_list[i]

def init_dec_list():
    None

def find_dec(_idx: int):
    res_dec_num = 0
    return res_dec_num

print(comb_list)


