print("Welcome to the ultimate quiz game!")
print("Please enter ur details to move on to the quiz.")

name=input("Enter your name: ")
age=int(input("Enter your age: "))
grade=input("Enter your grade: ")

score=0

print("Now lets move on to the quiz!")

print("Question 1: Which keyword is used to define a function in Python?")
q1=input("a) func\nb) def\nc) function\nd) define\nYour answer: ")
if q1.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is b) def.")   

print("Question 2: What is the capital of France?")
q2=input("a) London\nb) Berlin\nc) Paris\nd) Madrid\nYour answer: ")
if q2.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is c) Paris.") 

print("Question 3: What is the largest planet in our solar system?")
q3=input("a) Earth\nb) Saturn\nc) Jupiter\nd) Uranus\nYour answer: ")
if q3.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is c) Jupiter.") 

print("Your final score is:", score)
print("Your percentage score is:", (score/3)*100, "%")

if score == 3:
    print("Excellent! Your a genius!")
elif score == 2:
    print("Good job! You have a good understanding of the topics.Try to get more!!")
elif score == 1:
    print("You need to work hard! Keep learning and practicing.")   
else:
    print("Better luck next time!")