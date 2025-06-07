print("Welcome to the Quiz Game!")

score = 0
total_questions = 4  # Update this if you add more questions

answer = input("Do you want to play? (yes/no): ")

if answer.lower() == "yes":
    print("Great! Let's start the quiz.\n")

    answer = input("1. What is the best programming language? ")
    if answer.lower() == "python":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect. The correct answer is Python.\n")

    answer = input("2. What does CPU stand for? ")
    if answer.lower() == "central processing unit":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect. The correct answer is Central Processing Unit.\n")

    answer = input("3. What does GPU stand for? ")
    if answer.lower() == "graphics processing unit":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect. The correct answer is Graphics Processing Unit.\n")

    answer = input("4. What is the capital of France? ")
    if answer.lower() == "paris":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect. The correct answer is Paris.\n")

    percentage = (score / total_questions) * 100
    print(f"You got {score} out of {total_questions} questions correct.")
    print(f"Your final score: {percentage:.2f}%")
else:
    print("Goodbye! Your score is", score, "!")

