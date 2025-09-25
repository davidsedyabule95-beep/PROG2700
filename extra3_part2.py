
score = int(input("Enter your score (0–100): "))

if score == 100:
    print("Perfect!")
elif score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
elif score >= 50:
    print("Pass")
elif score < 40:
    print("Retake exam required")
else:
    print("Fail")
