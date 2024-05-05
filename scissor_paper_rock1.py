# import random
# spr_dict = {
#     "r": "rock",
#     "p": "paper",
#     "s": "scissor"
# }
# def print_info():
#     print("""
#     choose one f the following:
#     r: rock
#     p: paper
#     s: scissor
#         """)

# def get_user_choice():
#     user_input = None
#     while user_input not in list (spr_dict.keys()):
#         user_input = input("enter your choice: ")
#     user_choice = spr_dict[user_input]
#     return user_choice

# # def check_winner(user_choice, computer_choice):


# print_info()
# user_choice = get_user_choice()

# computer_choice = spr_dict[random.choice(list(spr_dict.keys()))]
# print("user_choice: ", user_choice)
# print("computer_choice: ", computer_choice)
# # check_winner(user_choice, computer_choice)


import random
spr_dict = {
    "r": "rock",
    "p": "paper",
    "s": "scissor"
}
def print_info():
    print("""
    choose one f the following:
    r: rock
    p: paper
    s: scissor
        """)

def get_user_choice():
    user_input = None
    while user_input not in list (spr_dict.keys()):
        user_input = input("enter your choice: ")
    user_choice = spr_dict[user_input]
    return user_choice

def check_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("it's a draw")
        return
    if computer_choice == "rock":
        if user_choice == "paper":
            print("you win")
        else:
            print("you lose")
    elif computer_choice == "paper":
        if user_choice == "scissor":
            print("you win")
        else:
            print("you lose")
    else:
        if user_choice == "rock":
            print("you win")
        else:
            print("you lose")
            
            
    print_info()
user_choice = get_user_choice()

computer_choice = spr_dict[random.choice(list(spr_dict.keys()))]
print("user_choice: ", user_choice)
print("computer_choice: ", computer_choice)
check_winner(user_choice, computer_choice)

def ask_to_play_again():
    user_input = None
    while user_input not in ["y", "n"]:
        user_input = input("Do you want to play again? (y/n):")
    if user_input == "y":
        return True
    else:
        return False


play_again = True
while play_again:
    print_info()
    user_choice = get_user_choice()
    computer_choice = spr_dict[random.choice(list(spr_dict.keys()))]
    print("\nComputer choice: ", computer_choice)
    print("User choice: ", user_choice)
    check_winner(computer_choice, user_choice)
    play_again = False
    play_again = ask_to_play_again()