FRONT = 1
input_list = list(map(int, input()))

dict = {1:'도', 2:'개', 3:'걸', 4:'윷', 0:'모'}
move = {'도':1,'개':2, '걸':3, '윷':4, '모':5}

num_front = input_list.count(FRONT)

print(move[dict[num_front]] ,end = ' ')

