#! /usr/bin/env python3


"""Does something """
#def sorter(v):
     

unique_words = dict()

while True:
    data = input("enter a line (press 'q' to quit)\n>")
    if data == 'q':
        break

    text = data.split()
    for word in text:
        unique_words[word] = unique_words.get(word, 0) + 1   #Similar to int(unique_words[word])
                                                             #.get allows for Exception Handling too
keylist = list(unique_words.keys())                          #Get a list of the keys in dictionary obj.
print()

print("words sorted by the word(key)")
keylist.sort()                                               #sorts the list in place, replacing it.
for eachkey in keylist:
    print("{:10} occured: {:10}".format(eachkey, unique_words.get(eachkey)))


print("words sorted by word count(value)")
keylist.sort(key=lambda x: unique_words[x], reverse=True)    #The item used to evaluate the sort is not numerical order, but the value in 
                                                             #unique_words[x]
for eachkey in keylist:
    print("{:10} occured: {:10}".format(eachkey, unique_words[eachkey]))


