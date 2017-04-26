#! /usr/bin/env python3

unique_words = set()

while True:
    data = input("enter a line (press 'q' to quit)\n>")
    if data == 'q':
        break
    text = data.split()
#    words = set(text)
    
    unique_words.update(text)

print("There are " + str(len(unique_words)) +" words are unique")
print(unique_words)


