#! /usr/bin/env python3

unique_words = dict()

#Get input from the user, separate into single words, put into a set.

while True:
    data = input("enter a line (press 'q' to quit)\n>")
    if data == 'q':
        break
    text = data.split()
    for word in text:
        if word not in unique_words:
            unique_words[word] = 0
        else:
            unique_words[word] = int(unique_words[word]) + 1


#Print number of unique words and the set of words.

print("There are " + str(len(unique_words)) +" words are unique")
print(unique_words)


