import random
def play(player , arti):
    if player == arti:
        return 0
    elif player == 0 and arti == 2:
        return -1
    elif player == 1 and arti == 0:
        return -1
    elif player == 2 and arti == 1:
        return -1
    else:
        return 1
player = int(input("Enter 0 for snake, 1 for water, and 2 for gun="))
arti = random.randint(0,2)
if player == 0:
    print("you choose snake")
elif player == 1:
    print("you choose water")
else:
    print("you choose gun")
if arti == 0:
    print("computer choose snake")
elif arti == 1:
    print("computer choose water")
else:
    print("computer choose gun")
point = play(player , arti)
if point == 0:
    print("match draw")
elif point == -1:
    print("you lose")
else:
    print("you won")