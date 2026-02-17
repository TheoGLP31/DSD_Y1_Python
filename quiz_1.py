import matplotlib.pyplot, pandas, numpy, math, random

NUM_QUESTIONS = 20
correctly_answered = 0
SUPPORTED_TYPES = ["+", "-", "x", "÷", "^"]
scores = numpy.array()

def check_int(number):
    try:
        number = float(number)
        return number
    except:
        return ""

for i in range(NUM_QUESTIONS):
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    rand_type = random.randint(0, len(SUPPORTED_TYPES) - 1)
    flag = True
    while flag:
        guess = check_int(input(f"{i + 1}. {num_1} {SUPPORTED_TYPES[rand_type]} {num_2} = (rounded to 2d.p.)?"))
        if guess == "":
            print("Please enter a valid number.")
            flag = True
        else:
            correct_answer = 0
            if SUPPORTED_TYPES[rand_type] == "+":
                correct_answer = round((num_1 + num_2), 2)
            elif SUPPORTED_TYPES[rand_type] == "-":
                correct_answer = round((num_1 - num_2), 2)
            elif SUPPORTED_TYPES[rand_type] == "x":
                correct_answer = round((num_1 * num_2), 2)
            elif SUPPORTED_TYPES[rand_type] == "÷":
                correct_answer = round((num_1 / num_2), 2)
            else:
                correct_answer = round((num_1 ** num_2), 2)

            if guess == correct_answer:
                print("Whoop Whoop!!")
                correctly_answered += 1
                flag = False
            else:
                flag = False

def end_results():
    choice = input("Would you like to view your results (Y/N)? ")
    if choice == "Y":
        correct_perc = (correctly_answered / NUM_QUESTIONS) * 100
        print(f"You answered: {correctly_answered} out of {NUM_QUESTIONS} questions correctly ({correct_perc}%).")
        numpy.append(scores, [correctly_answered, correct_perc])
        if len(scores) == 0:
            print()

end_results()