name = str(input("give me your name "))
age = int(input("give me your age "))
testscore = float(input("give me your test score "))

passedText = f"You have {"passed" if testscore>=10 else "failed"}"

print(passedText)