# import art
# import game_data
# import random
#
#
# def generate_data():
#     return game_data.data[random.randint(0, 49)]
#
#
# def check_win(a, b, user):
#     check = ""
#     if a > b:
#         check = "A"
#     else:
#         check = "B"
#     if check == user:
#         return True
#     else:
#         return False
#
#
# def check_game_score(res):
#     if res:
#         return 1
#     else:
#         return 0
#
#
# def game():
#     print(art.logo)
#     a = generate_data()
#     b = generate_data()
#     print(a["follower_count"], b["follower_count"])
#     print(f"Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}")
#     print(art.vs)
#     print(f"Compare B: {b["name"]}, a {b["description"]}, from {b["country"]}")
#     user = input("Who has more followers? Type 'A' or 'B'")
#     res = check_win(a=a['follower_count'], b=b['follower_count'], user=user)
#     return res
#
#
# end_game = False
# while not end_game:
#     check_game_score(game())
#
#
#
#
from art import logo
from art import vs
from game_data import data
import random


def format_data(account):
    """Formate the account data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_follower, b_follower):
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower = account_a["follower_count"]
    b_follower = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower, b_follower)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")








