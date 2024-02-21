# Homework Lesson 5 - Workshop - Homework

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

# Challenge 1
# Make a number Positive
#
# Create a variable called my_number and set it to any integer value.
# Write code to make the number positive if it's negative, and keep it
# as is if it's already positive or zero.
#
# Example:
# Input: -3 => Output: 3
# Input: 5 => Output: 5


my_number = int(input("Enter an integer: "))
string = str(my_number)

if string[0] == "-":
    print(string[:0:-1])
else:
    print(string[::-1])


# ---------------------------------------------------------------------

# Challenge 2
# BinGo!
#
# If the number is divisible of 3, print “Bin”
# If the number is divisible of 7, print “Go”
# For numbers which are divisible of 3 and 7, print “BinGo”
# Otherwise, print the original number: “{number} is just a number”

num = input("Enter a number: ")

if num % 3 == 0 and num % 7 == 0:
    print("Bingo")
elif num % 7 == 0:
    print("Go")
elif num % 3 == 0:
    print("Bin")
else:
    print(f"{num} is just a number")



# ---------------------------------------------------------------------

# Challenge 3
# Find the middle number
#
# Given three different numbers x, y, and z, find the number that is neither
# the smallest nor the largest and print it.
#
# Example:
# x = 1, y = 5, z = 3 => Output: 3
    
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
z = int(input("Enter one last number: "))

if ((x < y and y < z) or (z < y and y < x)):
    print(y)
elif ((y < x and x < z) or (z < x and x < y)):
    print(x)
else:
    print(z)


# ---------------------------------------------------------------------

# Challenge 4
# Palindrome Numbers
#
# Ask a user to input a number.
# Write a program to check if the given number is a palindrome.
# It should print True if the number is a palindrome and False if it is not.
#
# Palindrome number: 121, 898

number = input("Enter a number: ")

if number == number[::-1]:
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")

# ---------------------------------------------------------------------

# Challenge 5
# Reverse a string
#
# You're part of a team working on analyzing customer reviews for a new video game.
# Due to a software glitch, some reviews have been recorded in reverse with punctuation
# at the beginning instead of the end. Your task is to correct these reviews so that they
# are in the correct order and the punctuation is appropriately placed at the end of the
# sentence or word.
#
# Example: "tcefreP!" -> Perfect!

reverse_words = "tcefreP!"

print(reverse_words[6::-1] + reverse_words[:6:-1])