a = int(input("Input a number: "))
b = int(input("Input another number: "))
c = int(input("Input a third number: "))


if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)



year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")  



n = int(input("Enter an integer: "))
string = str(n)

if string[0] == "-":
    print('-' + string[:0:-1])
else:
    print(string[::-1])



word = input("Enter a word: ")

if word[::] == word[::-1]:
    print("String is a palindrome")
else:
    print("String is not a palindrome")