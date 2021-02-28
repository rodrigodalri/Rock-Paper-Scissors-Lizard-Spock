import random
from enum import IntEnum

class Action(IntEnum):
    """[summary]

    Args:
        IntEnum ([type]): [description]
    """
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4

victories = {
    Action.Scissors: [Action.Lizard, Action.Paper],
    Action.Paper: [Action.Spock, Action.Rock],
    Action.Rock: [Action.Lizard, Action.Scissors],
    Action.Lizard: [Action.Spock, Action.Paper],
    Action.Spock: [Action.Scissors, Action.Rock]
}

def get_user_selection():
    """[summary]

    Returns:
        [type]: [description]
    """
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Action(selection)
    return action

def get_computer_selection():
    """[summary]

    Returns:
        [type]: [description]
    """
    selection = random.randint(0, len(Action) - 1)
    return Action(selection)

def determine_winner(user_action, computer_action) -> int:
    """[summary]

    Args:
        user_action ([type]): [description]
        computer_action ([type]): [description]

    Returns:
        int: [description]
    """
    defeats = victories[user_action]
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
        return 0
    elif computer_action in defeats:
        print(f"{user_action.name} beats {computer_action.name}! You win!")
        return 1
    else:
        print(f"{computer_action.name} beats {user_action.name}! You lose.")
        return -1

def main():
    """[summary]
    """
    print("-------------------------------------------------")
    print("Welcome to Rock Paper Scissors Lizard Spock game!")
    print("Scoring Rules:")
    print("Win = 1 point")
    print("Tie = 0 point")
    print("Loss = -1 point")
    print("-------------------------------------------------")
    rounds_played = 0
    points = 0
    
    while True:
        try:
            user_action = get_user_selection()
        except ValueError as e:
            range_str = f"[0, {len(Action) - 1}]"
            print(f"Invalid selection. Enter a value in range {range_str}")
            continue

        rounds_played += 1
        
        computer_action = get_computer_selection()
        result = determine_winner(user_action, computer_action)
        points += result

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            print(f"Congratulations, you made {points} points in {rounds_played} rounds played!")
            break
    
if __name__== "__main__":
    main()