#! /usr/bin/env python3

def duplicates(list1, list2):
    results = []
    for element in list1:
        if element in list2:
            results.append(element)
    return results


def compare_list(list1, list2):
    """Takes two list, then determines intersection. Return a new list of like values"""       
    return list(set(list1) & set(list2))
    

alist = [1, 2, 3, 4, 5]
blist = [2, 4, 6, 8, 10]
clist = [1, 3, 5, 7, 9]

fmt = "|Are in both: {:8}|"

compared = compare_list(alist, blist)
for value in compared:
    print(fmt.format(value))
