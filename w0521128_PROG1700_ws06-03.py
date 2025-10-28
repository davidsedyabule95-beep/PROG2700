
import random
import time

#  NUMBER GUESSER
print("STEP 1 – NUMBER GUESSER 🎯")

secret = random.randint(1, 10)
guess = 0
tries = 0
max_tries = 5

while guess != secret and tries < max_tries:
    try:
        guess = int(input("Guess a number (1–10): "))
        tries += 1

        if guess < secret:
            print("Too low! 📉")
        elif guess > secret:
            print("Too high! 📈")
        else:
            print(f"You got it in {tries} tries! 🎉")

    except ValueError:
        print("Please enter a valid number!")

if tries == max_tries and guess != secret:
    print(f"Out of tries! The number was {secret}. 😅")
print()


#   COIN FLIPPER
print("STEP 2 – COIN FLIPPER 🪙")

heads = 0
tails = 0
count = 0

# Ask user for number of flips
flips = int(input("How many times should I flip the coin? "))

while count < flips:
    flip = random.choice(["Heads", "Tails"])
    print(f"Flip {count + 1}: {flip}")

    if flip == "Heads":
        heads += 1
    else:
        tails += 1

    count += 1
    time.sleep(0.2)

percent_heads = (heads / flips) * 100
percent_tails = (tails / flips) * 100
print(f"Heads: {heads} ({percent_heads:.1f}%) | Tails: {tails} ({percent_tails:.1f}%)")

if percent_heads >= 70 or percent_tails >= 70:
    print("Wow! One side dominated the flips! 😮")
print()


#   COUNTDOWN TIMER
print("STEP 3 – COUNTDOWN TIMER ⏱️")

try:
    start = int(input("Enter a starting number for countdown: "))
except ValueError:
    start = 10
    print("Invalid input! Defaulting to 10.")

while start >= 0:
    print(f"{start} 🔻")
    time.sleep(1)
    start -= 1

print("Blast off! 🚀\n")


#  PATTERN GENERATOR
print("STEP 4 – PATTERN GENERATOR ")

rows = 1
char = input("Enter a symbol or emoji for your pattern (e.g., * or 💫): ") or "💫"
limit = int(input("Enter how many rows you want: ") or 5)

while rows <= limit:
    print(char * rows)
    rows += 1


print("\nInverted pattern:")
rows = limit
while rows > 0:
    print(char * rows)
    rows -= 1
print("Pattern complete!\n")


# Reflection answers

# 1. Which challenge did you find most fun or surprising?
#    I enjoyed the number guesser because it felt interactive and made me think about logic flow.
#
# 2. What is one common mistake that caused infinite loops today?
#     Forgetting to update the loop variable (like not increasing count or changing a flag).
#
# 3. How could while loops be used in a real-world app?
#    For login systems, countdown timers, or keeping programs running until a user chooses to exit.
#
# 4. Which activity helped you best understand “loop conditions”?
#     The coin flipper, because I had to decide when to stop based on counts and percentages.
#
# -------------------------------------------------------------
print("✅ End of While Loop Challenge Lab – All steps complete!")
