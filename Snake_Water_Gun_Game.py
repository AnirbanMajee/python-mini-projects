import random


# Snake Water Gun or Rock Paper Scissors
def game(com, you):
    # If two values are equal, declare a tie!
    if com == you:
        return None

    # Check for all possibilities when computer chose s
    elif com == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True

    # Check for all possibilities when computer chose w
    elif com == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True

    # Check for all possibilities when computer chose g
    elif com == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True


print("Computer's Turn : snake(s) water(w) or gun(g) ? ")
rand_no = random.randint(1, 3)
#print(rand_no)
if rand_no == 1:
    com = "s"
elif rand_no == 2:
    com = "w"
elif rand_no == 3:
    com = "g"


you = input("Your's  Turn : snake(s) water(w) or gun(g) ? ")

a = game(com, you)

print(f"Computer choose {com}")
print(f"You choose {you}")

if a == None:
    print("The game is tie")

elif a == True:
    print("You win")

elif a == False:
    print("Com win")
