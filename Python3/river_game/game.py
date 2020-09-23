print("Welcome to my first game!")
name = input("What is your name?")
age = int(input("What is your age? "))
health = 10

if age >= 18:
    print("You are old enough to play!")

    wants_to_play = input("Do you want to play? ").lower()
if wants_to_play == "yes":
    print("You are staring with", health, "health")
    print("Let's play!")

    left_or_right = input("First choice... Left or Right (left/right)?")
if left_or_right == "left":
    print(
        "Nice, you follow the path and reach a lake... Do you swim across or go around (left/right)?"
    )
if left_or_right == "right":
    print("You fell of a cliff")

    swim_or_around = input(
        "Aweomse, do you want to swim across the lake or go around? (swim/around"
    )
if swim_or_around == "swim":
    print(
        "You made it across but lost 5 health to sharks. You see a house and a river. Do you go inside the house or swim down river? (house/river"
    )
if swim_or_around == "around":
    print("You made it safley to the house, Congrats!")

    house_or_river = input("Final attempt, choose wisley...(house/river")
if house_or_river == "house":
    print("You made it safley to the house, Congrats!")
if house_or_river == "river":
    print("You have drowned")
