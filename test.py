arr = [2,1,1,4,5,2,3]

L = 3
M = 2


all_sum = 0
sum_ = 0
u_number = list()
l_idx = 0

for my_len in [L, M]:

    for idx, v in enumerate(arr):

        while len(u_number) == my_len or v in u_number:
            u_number = u_number[1:]

        u_number.append(v)

        if len(u_number) >= my_len:
            if sum(u_number) > sum_:
                sum_ = sum(u_number)
                l_idx = idx - my_len + 1

    arr[l_idx:l_idx+my_len] = [0] * my_len
    all_sum += sum_
    u_number = list()
    l_idx = 0
    sum_ = 0



