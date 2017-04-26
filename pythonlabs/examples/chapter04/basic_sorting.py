#!/usr/bin/env python3
numberList = [3, 1, -10, 54, 75, 29]
wordList = ["Hello", "Goodbye", "goodbye", "hello"]
print("Basic sorting of a list.")
print("  Unsorted:", numberList, wordList)
numberList.sort()
wordList.sort()
print("  Sorted:", numberList, wordList, "\n")
numberList = [3, 1, -10, 54, 75, 29]

print("Basic sorting of a list in reverse.")
print("  Unsorted:", numberList, wordList)
numberList.sort(reverse=True)
wordList.sort(reverse=True)
print("  Sorted:", numberList, wordList, "\n")