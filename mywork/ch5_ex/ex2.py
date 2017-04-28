#! /usr/bin/env python3

def positive(*input, num=0):
    print(input, num)
    counter = 0
    over_num = []
    for number, value in enumerate(input):
        if number > num:
            counter += 1
            over_num.append(value)
    print(over_num)
    return counter, over_num


     
limit = 2
res, over_list = positive(5, -10, 10, -20, 30, num=limit)
print("There are {} over the limit. They are {}".format(res, over_list))
