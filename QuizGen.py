# Written to work on Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16)
# Code Writen by JbCoder (GitHub)
# Contributions to this code are welcome! Go to https://github.com/JbCoder/PyQuiz
# Make sure to add your GitHub username to the contributors.txt file.
import random, os, click
def quiz(number_of_questions):
	# setup
	questions_completed = 0
	score = 0
	questions_printed = []
	q_and_a = open("Questions.txt", "r")
	q_and_a = q_and_a.read()
	lines = q_and_a.split("\n")
	questions = lines[::2]
	total_questions = len(questions)
	answers = lines[1::2]
	print("Quiz Generated!")
	print("You will be asked " + str(number_of_questions) + " questions. Good Luck!")
	while questions_completed < number_of_questions:
		current_question = random.randint(-1, len(questions)-1)
		# pick a question at random
		if current_question in questions_printed:
			# if the randomly selected question has already been asked then find a different questions to ask. 
			continue
		else:
			questions_printed.append(current_question)
			# add the current question to list of done questions to avoid repetition
			ans = input(questions[current_question]).lower()
			if ans == answers[current_question].lower():
				print("Correct!")
				score += 1
			else:
				print("Incorrect!")
			questions_completed += 1
	print("You scored " + str(score) + "/" + str(number_of_questions))
	if click.confirm('Do you want to save your score?', default=True):
		name = input("Please type a sensible nickname: ")
		scorefile = open("Scores.txt", "a")
		scorefile.write(name + " : " + str(score) + "/" + str(number_of_questions) + "\n")
		print("Score Added!")
	os.system("pause")
	#print(questions)
	#print(answers)	
quiz(6)