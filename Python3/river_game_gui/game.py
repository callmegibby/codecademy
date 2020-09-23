'''
game.py 

-------

    These are used for waiting or killing a runtime:
    <https://www.w3schools.com/python/python_conditions.asp>

    GUI Library 
    <https://docs.python.org/3/library/tkinter.html>


import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self,
                              text="QUIT",
                              fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")


root = tk.Tk()
app = Application(master=root)
app.mainloop()

'''

import sys

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
    # elif ...
    # if else ... bye

elif age <= 18:
    print("you are too young")
    print("End Game")
    sys.exit

# if yes ..
if wants_to_play == "yes":
    print("You are staring with", health, "health")
    print("Let's play!")
    left_or_right = input("First choice... Left or Right (left/right)? ")
    # if else ... bye
else:
    print("End Game")
    sys.exit

# if left ...
if left_or_right == "left":
    print(
        "Nice, you follow the path and reach a lake... Do you swim across or go around (left/right)? "
    )
    # collecting input
    swim_or_around = input(
        "Awesome, do you want to swim across the lake or go around? (swim/around) "
    )
else:
    print("End Game")
    sys.exit
# if right ...

if left_or_right == "right":
    print("You fell of a cliff")
    # collecting input
    swim_or_around = input(
        "UH HA HA, do you want to swim across the lake or go around? (swim/around) "
    )
else:
    print("End Game")
    sys.exit

# if swim ...
if swim_or_around == "swim":
    print(
        "You made it across but lost 5 health to sharks. You see a house and a river. Do you go inside the house or swim down river? (house/river) "
    )
    # collecting input
    house_or_river = input("Final attempt, choose wisley...(house/river) ")
else:
    print("End Game")
    sys.exit

# if around ...
if swim_or_around == "around":
    print("You made it safely to the house, Congrats!")
    house_or_river = input("Final attempt, choose wisley...(house/river) ")
else:
    print("End Game")
    sys.exit

# if house ...
if house_or_river == "house":
    print("You made it safely to the house, Congrats!")
    # end game
else:
    print("End Game")
    sys.exit

# if river ...
if house_or_river == "river":
    print("You have drowned")
    # end game
else:
    print("End Game")
    sys.exit