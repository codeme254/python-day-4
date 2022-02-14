#randomisation and python lists
import random

# generating a random integer
random_integer = random.randint(1, 10)#generates a random integer between 1 and 10 with 1 and 10 inclusive
print(random_integer)
# what if we wanted to create a random floating point number?
random_float = random.random()#gives an output between 0 and 1  but not including 1
print(random_float)
# what if we wanted a random floating number between 0 and 5
random_float = random.random()*5
print(random_float)

# code exercise: coin toss program: tails or heads depending on which number was generated, 1 is heads and 0 is tails
random_determiner = random.randint(0, 1)
if random_determiner == 0:
    print("Tails")
elif random_determiner == 1:
    print("Heads")

# PYTHON LISTS
# sometimes we want to store grouped pieces of data
# in python we use lists, 
states_of_america = ["Delaware", "Pennsylvania", "Alabama", "Texas"]
print(states_of_america[0])#Delaware
print(states_of_america[1])#Pennsylvannia
# using negative indexes starts counting from the last item of the list
print(states_of_america[-1]) #Texas
#we can also change/modify elements in the list
states_of_america[1] = "Pennsylvannia"
# we can also add items to the end of the list as shown
states_of_america.append("Tennessee")
print(states_of_america)
# we can also extend lists with lists
states_of_america.extend(["Louisiana", "Kentucky", "Vermont"])
print(states_of_america)
# ['Delaware', 'Pennsylvannia', 'Alabama', 'Texas', 'Tennessee', 'Louisiana', 'Kentucky', 'Vermont']

# Coding Challenge---Banker Roulette-who will pay the bill
names_string = input("Give everybody's name seperated by a comma: ")
names = names_string.split(",")
person_to_pay = names[random.randint(0, len(names)-1)]
print(f"{person_to_pay} will pay the bill.")
# choice() function picks an element at random from a list
print(f"{random.choice(names)} might pay next time.")

# Index errors and working with nested lists
# Index errors occur when we refer to indexes that are not in the range of our lists
fruits = ['strawberries','nectarines', 'apples', 'grapes', 'peaches', 'cherries', 'pears']
vegetables = ['spinach', 'kale', 'tomatoes', 'celery', 'potatoes']
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
# prints this nested list
# [['strawberries', 'nectarines', 'apples', 'grapes', 'peaches', 'cherries', 'pears'], 
# ['spinach', 'kale', 'tomatoes', 'celery', 'potatoes']]

