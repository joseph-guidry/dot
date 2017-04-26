#!/usr/bin/env python3
import pickle
def main():
    grades = {'bob': {'exam1':93, 'exam2':79, 'exam3':99 },
              'sue': {'exam1':95, 'exam2':93, 'exam3':98}}

    with open('grades', 'wb') as file:
        pickle.dump(grades, file)

    with open('grades', 'rb') as file:
        data = pickle.load(file)
    
    print("Grades")
    for key, value in grades.items():
        print(key, ":", value)

    print("\nData")
    for key, value in data.items():
        print(key, ",", value)

    print("\ndata 'is' grades:", data is grades)
    print("data '==' grades:", data == grades)
    
if __name__ == "__main__": main()