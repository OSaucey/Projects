"""
quizMaker.py -- Quiz Maker

Make an application which takes various questions form a file, picked randomly, and puts together a quiz for students. Each quiz can be different and then reads a key to grade the quizzes.

TODO: Allow for percentange of questions.
      Work on implementation :(
"""

# Used to generate random number for question selection and shuffle answers.
from random import sample, shuffle
# If using Python2, rename raw_input() to input(); no change for Python3.
try:
    input = raw_input
except NameError:
    pass

# Read in the quiz file, ignoring blank lines.
with open('quizQuestions.txt', 'r') as quiz_file:
    lines = [line.strip() for line in quiz_file.readlines() if line.strip() != '']

# Store the questions, answer choices, and correct answer.
"""
Questions
    |
    |-> Question
    |        |
    |        |-> Question
    |        |
    |        |-> Answers
    |        |    |
    |        |    |-> Answer
    |        |    |-> Answer
    |        |    |-> Answer
    |        |    |-> Answer
    |        |
    |        |-> Correct
    |
    |-> Question
    |        |
    |        |-> Question
    |        |
    |        |-> Answers
    |        |    |
    |        |    |-> Answer
    |        |    |-> Answer
    |        |    |-> Answer
    |        |    |-> Answer
    |        |
    |        |-> Correct
    |
    .
    .
    .
    |
"""

questions = ['']    # Index matches question number for creating full list.
total_questions = 0
for line in lines:
    if line.startswith('*@'):
        questions[total_questions][2] = line.strip('*@')
        questions[total_questions][1].append(line.strip('*@'))
    elif line.startswith('*'):
        questions[total_questions][1].append(line.strip('*'))
    else:
        total_questions = total_questions + 1
        questions.append([line, [''], ''])

# Pick a certain number of questions randomly and ask the user them.
question_total = 3
if question_total > total_questions:
    question_total = total_questions
chosen_questions = sample(questions[1:], question_total)

total_correct = 0
print('This test has %d questions. Good Luck!' % (question_total))
for question in chosen_questions:
    answers = question[1][1:]
    shuffle(answers)
    question[1][1:] = answers
    print('')
    print(question[0])
    
    for current, answer in enumerate(question[1]):
        if current > 0:
            print('    %s) %s' % (current, answer))
    
    choice = ''
    while (not choice.isdigit()) or (int(choice) < 1) or (int(choice) > current):
        choice = input('Enter the correct answer: ')
    print('')
    if question[1][int(choice)] == question[2]:
        print('Correct!')
        print('')
        total_correct = total_correct + 1
    else:
        print('WRONG! The correct choice was: %s' % (question[2]))

print('')
print('The quiz is done. You scored %s/%s (%d%%).' % (total_correct,
    question_total, ((total_correct * 100)/question_total)))
