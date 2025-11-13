y
import random

moves = ["rock", "paper", "scissors", "lizard", "spock"]
wins = {
    ("rock","scissors"),("rock","lizard"),
    ("paper","rock"),("paper","spock"),
    ("scissors","paper"),("scissors","lizard"),
    ("lizard","spock"),("lizard","paper"),
    ("spock","scissors"),("spock","rock")
}

aliases = {"r":"rock","p":"paper","s":"scissors","l":"lizard","sp":"spock"}

def get_move(prompt):
    while True:
        x = input(prompt).lower().strip()
        if x in moves: return x
        if x in aliases: return aliases[x]
        print("Invalid move. Try again.")

def decide(p,c):
    if p==c: return "tie"
    return "player" if (p,c) in wins else "cpu"

def play_match():
    while True:
        try:
            n=int(input("Best of (odd): "))
            if n%2==0 or n<=0: raise ValueError
        except ValueError:
            print("Enter an odd positive number."); continue
        score={"player":0,"cpu":0,"ties":0}
        hist=[]; win_goal=n//2+1; r=0
        while score['player']<win_goal and score['cpu']<win_goal:
            r+=1
            p=get_move("Your move (r/p/s/l/sp): ")
            c=random.choice(moves)
            res=decide(p,c)
            score[res]+=1 if res!="tie" else 0
            if res=="tie": score['ties']+=1
            hist.append({'r':r,'p':p,'c':c,'res':res})
            print(f"Round {r}: You {p} vs CPU {c} → {res.upper()}")
        winner="player" if score['player']>score['cpu'] else "cpu"
        print(f"Match over! Winner: {winner.upper()} {score}")
        # Enhancement: Analytics (most used move)
        from collections import Counter
        pmove=Counter([h['p'] for h in hist]).most_common(1)[0]
        cmove=Counter([h['c'] for h in hist]).most_common(1)[0]
        print(f"Your most used: {pmove[0]} ({pmove[1]}) | CPU: {cmove[0]} ({cmove[1]})")
        if input("Play again? (y/n): ").lower()!='y': break

if __name__=='__main__':
    play_match()

# Reflection:
# 1) Most useful function: get_move() – keeps input clean & reusable.
# 2) Fixed: rejecting even numbers in best-of input.
# 3) Lists for moves, sets for rule pairs, dict for scores – all simple.
# 4) Next step: save match history to file.
