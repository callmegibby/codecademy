"""
This program generates passages that are generated in mad-lib format
Author: Katherin 
"""

# The template for the story

STORY = ("This morning %s woke up feeling %s. 'It is going to be a _ day!' Outside, a bunch of _s were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %s very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %s ruled the world.")

print "Mad Libs has started!"

name = raw_input("Jake")

adj1 = raw_input("brave")
adj2  = raw_input("lazy")
adj3 = raw_input("plump")
verb = raw_input("awake")
noun1 = raw_input("cat")
noun2 = raw_input("chair")
animal = raw_input("dog")
food = raw_input ("pizza")
fruit = raw_input("mango")
superhero = raw_input("superman")
country = raw_input("na")
dessert = raw_input("pie")
year = raw_input("1999")
print STORY % (name, adj1, adj2, animal, food, verb, noun1, fruit, adj3, name, name, superhero, country, name, country, name, dessert, name, year,noun2)



















