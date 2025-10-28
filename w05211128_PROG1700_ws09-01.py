
import time

print("STEP 1 – COUNTDOWN MACHINE 🚀")

# Counting down from 10 to 1
count = 10
while count > 0:
    print(f"Launching in... {count} 🚀")
    time.sleep(1)  # adds dramatic 1-second pause
    count -= 1

print("LIFTOFF!!! 🌕✨\n")

#  THE GUESSING GAME 2
import random

print("STEP 2 – GUESSING GAME 🎲")

play_again = "y"

while play_again.lower() == "y":
    secret = random.randint(1, 10)
    guess = 0
    attempts = 0
    max_attempts = 5
    score = 10

    print("\nI'm thinking of a number between 1 and 10...")
    while guess != secret and attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret:
            print("Too low! 📉")
        elif guess > secret:
            print("Too high! 📈")
        else:
            print(f"You got it in {attempts} tries! 🎉")
            score = score - (attempts - 1)
            print(f"Your score: {score}")
            break

        if attempts == max_attempts:
            print("Game Over 😢 The number was:", secret)

    play_again = input("Play again? (Y/N): ")

print("\nThanks for playing! 🎮\n")

#  LOOP YOUR OWN ADVENTURE
# Idea: 🥤 Bubble Tea Simulator

print("STEP 3 – BUBBLE TEA SIMULATOR 🧋")

import random
sips = 5

while sips > 0:
    print("You take a sip... 🧋")
    time.sleep(1)
    sips -= 1

    
    event = random.choice(["boba pearl!", "brain freeze!", "sweet flavor!", "crushed ice!"])
    print(f"You encounter a {event}")

print("Cup empty. Refill time! 🧊🧋")


# REFLECTION answers 

# 1. What bug or mistake caused your first infinite loop today?
#     I forgot to decrease the loop counter in my first test, so it never ended.
#      I fixed it by adding 'count -= 1' inside the while loop.

# 2. How did you fix it?
#     I checked my logic and realized the loop condition never changed.
#      Once I updated the variable correctly, it stopped looping forever.

# 3. Which loop activity did you enjoy most, and why?
#     The Bubble Tea Simulator! It was funny seeing random “boba pearl” or “brain freeze” messages.

# 4. How might while loops be useful in a game or app you’d build someday?
#     While loops can make games run continuously (like menus, battles, or score counters)
#      until the player wins or quits. They’re perfect for anything that repeats or checks conditions.
