'''
game.py 

-------

    These are used for waiting or killing a runtime:
    <https://www.w3schools.com/python/python_conditions.asp>

import time 
<<<<<<< HEAD
=======
import sys
>>>>>>> 222fd1f375acf3db5de58860c3238d375a32a178
from time import sleep 

a = 200
b = 33
if b > a:
  print("b is greater than a")
<<<<<<< HEAD

    elif a < b:
    print("a and b are equal")

        else:
        print("a is greater than b")
=======
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
>>>>>>> 222fd1f375acf3db5de58860c3238d375a32a178

'''

# Introduction
print("Welcome to my first game!")

# What is your name?
name = input("What is your name?")

# What is your age?
age = int(input("What is your age?"))

# init health value
health = 10

# if you are this many years (int) old
if age >= 18:
    print("You are old enough to play!")
    wants_to_play = input("Do you want to play?").lower()
    # if else ... bye
<<<<<<< HEAD
elif: age <=18
    print("you are too young")

else:
    (SystemExit)

=======
else:
    (SystemExit)

>>>>>>> 222fd1f375acf3db5de58860c3238d375a32a178
# if yes ..
if wants_to_play == "yes":
    print("You are staring with", health, "health")
    print("Let's play!")
    left_or_right = input("First choice... Left or Right (left/right)?")
    # if else ... bye
else:
    (SystemExit)

# if left ...
if left_or_right == "left":
    print(
        "Nice, you follow the path and reach a lake... Do you swim across or go around (left/right)?"
    )
    # collecting input
    swim_or_around = input(
        "Awesome, do you want to swim across the lake or go around? (swim/around)"
    )

# if right ...
if left_or_right == "right":
    print("You fell of a cliff")
    # collecting input
    swim_or_around = input(
        "Awesome, do you want to swim across the lake or go around? (swim/around)"
    )

# if swim ...
if swim_or_around == "swim":
    print(
        "You made it across but lost 5 health to sharks. You see a house and a river. Do you go inside the house or swim down river? (house/river)"
    )
    # collecting input
    house_or_river = input("Final attempt, choose wisley...(house/river)")

# if around ...
if swim_or_around == "around":
    print("You made it safely to the house, Congrats!")
    house_or_river = input("Final attempt, choose wisley...(house/river)")
<<<<<<< HEAD
=======
    # do something
>>>>>>> 222fd1f375acf3db5de58860c3238d375a32a178

# if house ...
if house_or_river == "house":
    print("You made it safely to the house, Congrats!")
<<<<<<< HEAD
    # end game
=======
    # do something
>>>>>>> 222fd1f375acf3db5de58860c3238d375a32a178

# if river ...
if house_or_river == "river":
    print("You have drowned")
<<<<<<< HEAD
    # end game
=======
    # do something
>>>>>>> 222fd1f375acf3db5de58860c3238d375a32a178
