-import random
import simplegui

# Mapping names to numbers and vice versa
choices = ["rock", "Spock", "paper", "lizard", "scissors"]
player_score = 0
comp_score = 0

def name_to_number(name):
    try:
        return choices.index(name)
    except ValueError:
        print("Error: Not a valid name")
        return None

def number_to_name(number):
    try:
        return choices[number]
    except IndexError:
        print("Error: Not a valid number")
        return None

def rpsls(player_choice): 
    global player_score, comp_score
    print("------------")   
    print("Player chooses " + player_choice)
    
    player_number = name_to_number(player_choice)
    if player_number is None:
        return
    
    comp_number = random.randrange(5)
    comp_choice = number_to_name(comp_number)
    
    print("Computer chooses " + comp_choice)
    
    diff = (comp_number - player_number) % 5
    if diff in [1, 2]:
        print("Computer Wins")
        comp_score += 1
    elif diff in [3, 4]:
        print("Player Wins")
        player_score += 1
    else:
        print("Player and computer tie!")

    print_scores()

def get_input(inp):
    if inp in choices:       
        rpsls(inp)
    else:
        print("Error: Invalid Input")

def reset_score():
    global player_score, comp_score
    player_score = 0
    comp_score = 0
    print("Scores reset!")

def print_scores():
    print(f"Player Score: {player_score}, Computer Score: {comp_score}")

def play_rounds(n):
    for _ in range(n):
        player_choice = random.choice(choices)
        rpsls(player_choice)

# Create frame and register input field
frame = simplegui.create_frame("Rock-paper-scissors-lizard-Spock", 200, 200)
frame.add_input("Enter your choice: ", get_input, 200)    
frame.add_button("Reset Scores", reset_score)
frame.add_button("Play 5 Rounds", lambda: play_rounds(5))
frame.start()

# Test calls
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
