#! /usr/bin/env python3

unique_words = set()

while True:
    data = input("enter a line (press 'q' to quit)\n>")
    if data == 'q':
        break
    text = data.split()
#    words = set(text)
    
    unique_words.update(text)

#Create list of unique words
word_list = list(unique_words)

#Sort unique words list
#word_list.sort()


print("There are " + str(len(unique_words)) +" words are unique")
print(sorted(word_list))



