#Exercise 4: Primitive Quiz 
# This program asks a quiz question and checks the answer

answer = input("What is the capital of France? ")

if answer.strip().lower() == "paris":
    print("Correct!")
else:
    print("Wrong! The correct answer is Paris.")
