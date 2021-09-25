"""choose your own adventure project."""


__author__ = "730389123"


from random import randint
points: int = 0
player: str = ""


def main() -> None:
    """Program Entry Point."""
    greet()
    print("Points are gained in this game by scoring direct hits on enemy ships")
    print(f"You currently have: {points} points.")
    print("You wake up in the tavern")
    print("What do you do? Set sail immediatly(enter 1), Gather supplies(enter 2), go to sleep? (enter 3)")
    first_action: int = int(input(""))
    if first_action == 1:
        print("you go to your ship and set sail immediatly")
        ship(randint(1, 10))
        if first_action == 2:
            supplies(1)
            if first_action == 3:
                print("thank you for playing.")
                print(f"You earned: {points} points.")
    game_loop: int = int(input(""))
    while game_loop == 1:
        print("You wake up in the tavern")
        print(f"You currently have: {points} points.")
        print("What do you do? Set sail immediatly(enter 1), Gather supplies(enter 2), go to sleep? (enter 3)")
        second_action: int = int(input())
        if second_action == 1:
            print("you go to your ship and set sail immediatly")
            ship(randint(1, 10))
            if second_action == 2:
                supplies(1)
                if second_action == 3:
                    print("thank you for playing.")
        print("You return to port.")
        print("Do you set sail again?(Enter 1 for yes, Enter 2 for no")
        game_loop: int = int(input(""))

      
def greet() -> None:
    """Player Greeting."""
    print("Welcome to the Lake of Privateers!")
    player = str(input("What is your name?: "))
    print("This is a land of total freedom to sail the seas and fight for glory.")
    print("Be prepared to fight for survivial.")
    print("It is time to set sail " + player)


def ship(x: int) -> None:
    """Wrong Player action."""
    if x >= 8:
        print("You encounter a storm.")
        print("Since you collected no supplies your ship sinks instantly since you are unable to repair the damage.")
        print("try again next time.")
        if x < 8 and x >= 4:
            print("You sail out into the open seas.")
            print("Without any food onboard you quickly starve.")
            if x < 4:
                print("you are ambushed by other privateers and are unable to fight back since you have no cannon balls.")


def supplies(x: int) -> None:
    """Correct Player action."""
    print("you gather lots of supplies and then set sail.")
    action_begins: int = randint(1, 10)
    i: int = 0
    j: int = 1
    while i < j:
        if action_begins <= 5:
            print("You spot a marchant ship in the distance and approach to attack")
            print("You raise the Black Flag and aim you cannon. Select the elevantion (select a value from 1-5)")
            attack: int = int(input())
            if attack == distance(x):
                print("You score several hits and sink the merchant")
                points = points + 1
                i = i + 1
                if attack > distance(x):
                    print("you overshoot fire again!")
                    if attack < distance(x):
                        print("you undershoot firre again!")
            print("Do you want to keep sailing" + player + "?")
            print(f"You have {points} points.")
            loop: int = int(input(""))
            if loop == 1:
                j = j + 1
    if action_begins >= 9 and action_begins > 5:
        print("You are attacked by other privateers")
        print("You raise the Black Flag and aim you cannon. Select the elevantion (select a value from 1-5)")
        attack: int = int(input())
        if attack == distance(x):
            print("you score several hits and sink the pirates")
            points = points + 1
            i = i + 1
            if attack > distance(x):
                print("you overshoot fire again!")
                if attack < distance(x):
                    print("you undershoot firre again!")
            print("Do you want to keep sailing" + player + "?")
            print(f"You have {points} points.")
            loop: int = int(input(""))
            if loop == 1:
                j = j + 1
    if action_begins > 9:
        print("You are attacked by the kracken")
        print("You raise the Black Flag and aim you cannon. Select the elevantion (select a value from 1-5)")
        attack: int = int(input())
        if attack == distance(x):
            print("you score several hits but the beast is still alive")
            points = points + 1
            i = i + 1
            j = 3
            if attack > distance(x):
                print("you overshoot fire again!")
                if attack < distance(x):
                    print("you undershoot firre again!")
            print("Do you want to keep sailing" + player + "?")
            print(f"You have {points} points.")
            loop: int = int(input(""))
            if loop == 1:
                j = j + 1


def distance(x: int) -> int:
    """Distance to target."""
    x == randint(1, 5)
    return x


if __name__ == "__main__":
    main()