# cd Downloads
#python py4hrs.py

#print Hello world
print("Hello world")

#print triangle
print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")

#print with variables
character_name= "Jon snow"
character_age= "85"
print("My name is " + character_name + " ,")
print("I like my name.")
print("My age is " + character_age + " ,")
print("But i dont like my age.")

#print with changed variables
character_name= "Jon"
character_age= "55"
print("My name is " + character_name + " ,")
print("I like my name.")
print("My age is " + character_age + " ,")

#print The Umbrella Academy in seperate lines
print("\n The\n Umbrella\n Academy")

#print The Umbrella Academy in seperate lines as a variables
phrase = "\n The\n Umbrella\n Academy\n"
print(phrase + "is cool")

#print The Umbrella Academy in capital letters
phrase = "The Umbrella Academy"
print(phrase.upper())

#print The Umbrella Academy in capital letters and check if its capitalized
phrase = "The Umbrella Academy"
print(phrase.upper().isupper())

#print The Umbrella Academy and check its length
phrase = "The Umbrella Academy"
print(len(phrase))

#print The Umbrella Academy and find the third letter in it
phrase = "The Umbrella Academy"
print(phrase[3])

#print The Umbrella Academy and check the index of the letter r in it
phrase = "The Umbrella Academy"
print(phrase.index("r"))

#print The Umbrella Academy and check the index of the letter a in it
#note that there are two a in the sentence yet python give you the index of only the first letter
phrase = "The Umbrella Academy"
print(phrase.index("a"))

#print The Umbrella Academy and check the index of the letter a in it
#note that there are two a in the sentence yet python give you the index of only the first letter
phrase = "The Umbrella Academy"
print(phrase.index("lla"))


# The Umbrella Academy is replaced into The raining Academy
phrase = "The Umbrella Academy"
print(phrase.replace("Umbrella", "raining"))

#using numbers
print(5)
print(6.7)
print(6+5)
print(6-5)
print(6*5)
print(6/5)
print(6*5-3)
print(6*(5-3))
print(6%2)

my_num = 5
print(my_num)

#absolute
my_num = -5
print(abs(my_num))

my_num = 5
print(str(my_num) + " is my fav no")

#power
print(pow(5, 2))

#maximum
print(max(5, 2))

#minimum
print(min(5, 2))

#rounding off
print(round(3.7))

#additional math funcs
from math import*

#rounding off to lowest
print(floor(8.7))

#rounding off to highest
print(ceil(8.7))

#square root
print(sqrt(169))

#getting input from users
name = input("Enter your Name: ")
age = input("Enter your Age: ")
print("Hello " + name + "!!! \n You are " + age + " now")

#buliding a basic calc
num1 = input("Enter a random number")
num2 = input("Enter an another random number")
result = float(num1) + float(num2)
print(result)

#mad lib game

color = input("Enter a color: ")
plural_noun = input("Enter a plural noun ")
crush =  input("Enter your crush name ")
print("Roses are " + color)
print(plural_noun + " are violet")
print("I love " + crush)

#lists
friends = ["David", "Theo", "Tesla", "Raavan", "Alphonse"]
print(friends)
friends.reverse()
print(friends)
friends.sort()
print(friends)
print(friends[3])
print(friends[-2])
print(friends[1:3])
print(friends[1:])
more_friends = ["Ram", "Seeta", "Shiv", "Parvati"]
friends.extend(more_friends)
print(friends)
friends.append("Bheem")
print(friends)
friends.insert(0, "Adam")
print(friends)
friends.remove("Bheem")
print(friends)
friends.pop()
print(friends)
friends.clear()
print(friends)

mixed_lists = ["David", "1", 2, "Raavan", True, "Alphonse", "Alphonse"]
print(mixed_lists)
print(mixed_lists.index("David"))
print(mixed_lists.count("Alphonse"))

mixed_lists2 = mixed_lists.copy()
print(mixed_lists2)

#tuples
#note that tuples are same as lists except it cant be changed once its been created
coordinates = [1, 2]
print(coordinates)
coordinates2 = [(1, 2), (4, 5), (7, 8)]
print(coordinates2)

#functions
def say_hola():
    print("Hola world!!!")
say_hola()

def say_Bonjour(bonjour_name):
    print("Hola " + bonjour_name + "!!!")
say_Bonjour("steve")

def say_Bonjour(bonjour_name, bonjour_age):
    print("Hola " + bonjour_name + "!!! You are " + bonjour_age)
say_Bonjour("tony", "5")

def say_Bonjour(bonjour_name, bonjour_age):
    print("Hola " + bonjour_name + "!!! You are " + str(bonjour_age))
say_Bonjour("tony", 5)

def cube(num):
    return num*num*num
print(cube(2))

def avg(avg_num):
    return (avg_num+avg_num)/2
print(avg(4))

def avg(avg_num1, avg_num2):
    return (avg_num1 + avg_num2)/2
print(avg(4, 5))

#IF statements

is_male = True
if is_male:
    print("You are a male")

is_male = False
if is_male:
    print("You are a male")
else:
    print("You are not a male")

is_male = True
is_tall = False
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither a male nor tall")

is_male = True
is_tall = False
if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are either not a male or not tall")

is_male = True
is_tall = False
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("you are not a male but tall")
else:
    print("You are neither a male nor tall")


def max_num(max_num1, max_num2, max_num3):
    if max_num1 >=max_num2 and max_num1 >= max_num3:
        return max_num1
    elif max_num2 >= max_num1 and max_num2 >= max_num3:
        return max_num2
    else:
        print(max_num3)

print(max_num(5, 8, 7))

#buliding a better calc

better_calc_num1 = float(input("Enter the  first number: "))
better_calc_op = input("Enter an Operator: ")
better_calc_num2 = float(input("Enter the second number: "))

if better_calc_op == "+":
    print(better_calc_num1 + better_calc_num2)
elif better_calc_op == "-":
    print(better_calc_num1 - better_calc_num2)
elif better_calc_op == "*":
    print(better_calc_num1 * better_calc_num2)
elif better_calc_op == "/":
    print(better_calc_num1 / better_calc_num2)
else:
    print("Invalid Operator")

#dictionaries
monthcoversions = {
    "jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
}
print(monthcoversions)
print(monthcoversions["Feb"])
print(monthcoversions.get("Feb"))
print(monthcoversions.get("Fen", "Not a Valid Key"))

#While loops
i = 1
while i <= 10:
    print(i)
    i += 1
print("Loop over")

#The guessing game
Secret_word = "Apple"
Guess = ""
Guess_count = 0
Gues_limit = 3
out_of_guesses = False

while Guess != Secret_word and not(out_of_guesses):
    if Guess_count < Gues_limit:
        Guess = input("Enter the Secret word: ")
        Guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("out of guesses, You Lose!!!")
else:
    print("Hola, You win!")

#for loops

for letters in "The Umbrella Academy":
    print(letters)

friends_forloop = ["Bheem", "Parvati", "Lucifer"]
for friends_forloop_list in friends_forloop:
    print(friends_forloop_list)

friends_forloop = ["Bheem", "Parvati", "Lucifer"]
for friends_index in range(len(friends_forloop)):
    print(friends_forloop[friends_index])

for index in range(10):
    print(index)

for index in range(3, 10):
    print(index)

for index in range(10):
    if index == 0:
        print("first iteration")
    else:
        print("not a first iteration")

for index in range(10):
    if index == 0:
        print("first iteration")
    else:
        print(index)

#exponential finc
print(2**3)
print(2^3)

def raised_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raised_to_power(5, 2))

#2d lists
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid)
print(number_grid[1][2])
print(number_grid[0][0])

#nested loop (loop inside a loop)
nested_number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in nested_number_grid:
    print(row)

for row1 in nested_number_grid:
    for col in row1:
        print(col)

#buliding a translator

def translate(phrase):
    translation = ""
    for translate_letter in phrase:
        if translate_letter.lower() in "aeiou":
            if translate_letter.isupper():
                translation = translation + "Z"
            else:
                translation = translation + "z"
        else:
                translation = translation + translate_letter
    return(translation)

print(translate(input("Enter a Phrase: ")))

#try and except
try:
    try_number = int(input("Enter a number: "))
    print(try_number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")

try:
    answer = 10/0
    try_number = int(input("Enter a number: "))
    print(try_number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")

#open a file
interview_q = open("py4hrs.txt", "r")
interview_q.read()
interview_q.close()
# r for read
# a for append
# w for write
