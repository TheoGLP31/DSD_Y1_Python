"""
'Tis but a quiz.
"""

quiz = {
    "1":"true",
    "2":"c",
    "3":"c"
}

print("Question 1: \n 'Roger Bacon wanted for war crimes'. True or False?")
q1_answer = input("A: ")

print("Question 2: \n How much money is Roger Bacon in debt? \n A: £200,000 \n B: £400,000 \n C: £600,000 \n D: £1,000,000")
q2_answer = input("A: ")

print("Question 3: \n What is the correct name of Roger Bacon? \n A: Great Grandchild to Napolean the Pig \n B: Great Great Grandchild to Napolean the Pig \n C: Great Great Great Grandchild to Napolean the Pig \n D: Great Great Great Great Grandchild to Napoleon the Pig")
q3_answer = input("A: ")

score = 0

if q1_answer.lower() == quiz["1"]:
    score += 1
if q2_answer.lower() == quiz["2"]:
    score += 1
if q3_answer.lower() == quiz["3"]:
    score += 1

print(f"You got {score}/3. You are {"great" if score == 3 else "good" if score == 2 else "bad"} at Roger Bacon common knowledge.")