print ("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

health = 10

if age >= 18:
    print ("You are old enough to play!")
    
    wants_to_play = input("Do you want to play? ").lower()
if wants_to_play == "yes":
    print ("you are staring with", health, "health")
    print ("Let's play!")
    
    left_or_right = input("First choice... Left or Right (left/right)?")
if left_or_right == "left":
    ans = ("Nice, you follow the path and reach a lake... Do you wim across or go around (across/around)?")
