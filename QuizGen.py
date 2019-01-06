# Written to work on Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16)
# Code Writen by JbCoder (GitHub)
# Contributions to this code are welcome! Go to https://github.com/JbCoder/PyQuiz
# Make sure to add your GitHub username to the contributors.txt file.
import random, os
# setup
c = 0
score = 0
number_of_questions = 6
questions_printed = []
i = open("Questions.txt", "r")
i = i.read()
lines = i.split("\n")
questions = lines[::2]
total_questions = len(questions)
answers = lines[1::2]
print("Quiz Generated!")
print("You will be asked " + str(number_of_questions) + " questions. Good Luck!")
while c < number_of_questions:
	current_question = random.randint(-1, len(questions)-1)
	if current_question in questions_printed:
		# if the randomly selected question has already been asked then find a different questions to ask. 
		c += -1
	else:
		questions_printed.append(current_question)
		ans = input(questions[current_question]).lower()
		if ans == answers[current_question].lower():
			print("Correct!")
			score += 1
		else:
			print("Incorrect!")
	c += 1
print("You scored " + str(score) + "/" + str(number_of_questions))
os.system("pause")
#print(questions)
#print(answers)