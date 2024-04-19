# Write your code below this line 👇
def prime_checker(number):
    if number <= 1:
        return print("It's not a prime number.")
    if number == 2:
        return print("It's a prime number.")
    if number % 2 == 0:
        return print("It's not a prime number.")
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return print("It's not a prime number.")
        return print("It's a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
