#! /usr/bin/env python3


def solve(a0, a1, a2, b0, b1, b2):
    alist = [a0, a1, a2]
    blist = [b0, b1, b2]
    total = [0,0]

    for num in range(0,3):

        if alist[num] > blist[num]:
            print(total[0])
            total[0] += 1
            print(total[0])
        elif alist[num] < blist[num]:
            print(total[1])
            total[1] += 1
            print(total[1])
        else:
            print("values are equal, no points")

    return total

a0, a1, a2, b0, b1, b2 = [1, 2, 3, 4, 2, 6]
results = solve(a0, a1, a2, b0, b1, b2)
print(results)
