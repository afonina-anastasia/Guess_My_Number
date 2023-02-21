from random import randint

attempts = 10
target_number = randint(1, 100)


# print(a)
def guess():
    for i in range(attempts):
        try:
            guess_number = int(input("Enter your guess: "))
        except ValueError:
            print("Re-enter the number!")
            continue

        if target_number == guess_number:
            return "Correct"

        elif target_number > guess_number:
            print("More")
            continue

        elif target_number < guess_number:
            print("Less")
            continue

        else:
            break

    return f'The game is over, thank you! The guessed number was {target_number}'


print(guess())


