import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write our code below this line 👇


random_integer = random.randint(0, len(names) - 1)

print(f"{names[random_integer]} is going to by the meal today!")
