#!/usr/bin/env python3

# Created by Marwan Mashaly
# Created on December 2019
# This program checks if the string is a palindrome or not


def StringCheck(string1, str1):
    # This function reverses the string and returns it

    for letters in string1:
        str1 = letters + str1
        print("String in reverse Order :  ", str1)
    if(string1 == str1):
        return string1
    else:
        return str1


def main():
    # This function takes input and checks if it's a palindrome

    while True:
        string1 = input("Please enter your own String : ")
        print("")
        str1 = ""
        answer = StringCheck(string1, str1)
        if(answer == string1):
            print("")
            print("it's a palindrome")
        else:
            print("")
            print("it's not a palindrome")


if __name__ == "__main__":
    main()
