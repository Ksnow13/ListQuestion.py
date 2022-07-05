
# Lesson 27 & 28 Question 4

import math
import FormatValues as FV


while True:

    Title = input(" Enter the title of the quiz: ")

    if Title == "":
        print("Cannot be blank ")

    else:
        break

while True:

    try:
        NumberOfQuestions = input(" Enter the number of questions: ")
        NumberOfQuestions = int(NumberOfQuestions)
    except:
        print("Must be a number ")
    else:
        if NumberOfQuestions < 1:
            print("Must be at least 1 ")
        else:
            break

AnswerKey_List = []

while True:

    while len(AnswerKey_List) != NumberOfQuestions:

        Key = input(" Enter the answer key (A,B,C,D) & (Q) to quit: ")

        if Key == "":
            print("Cannot be blank ")

        elif len(Key) > 1:
            print("Must be one character ")

        elif Key.upper() != "A" and Key.upper() != "B" and Key.upper() != "C" and Key.upper() != "D" and Key.upper() != "Q":
            print("Must be A,B,C,D ")

        elif Key.upper() == "A" or Key.upper() == "B" or Key.upper() == "C" or Key.upper() == "D":
            AnswerKey_List.append(Key.upper())

    break



print(AnswerKey_List)


while True:

    try:
        AmountOfQuzzies = input(" Enter the number of quizzes: ")
        AmountOfQuzzies = int(AmountOfQuzzies)
    except:
        print(" Must be a number ")
    else:
        break


StudentName_List = []

NumberCorrect = []

Marks = []


while len(StudentName_List) != AmountOfQuzzies:

    while True:

        StudentName = input(" Enter the Student Name: ")

        if StudentName == "":
            print("Cannot be blank ")

        else:
            break

    StudentName_List.append(StudentName)

    Answers = 0
    Correct = 0
    while Answers != len(AnswerKey_List):


        for i in range(0, len(AnswerKey_List)):

            #Answers = 0

            while True:



                StudentAnswers = input(" Enter they're answer: ")
                Answers += 1

                if StudentAnswers.upper() == AnswerKey_List[i]:
                    Correct += 1


                break
            print(Correct)
        break

    NumberCorrect.append(Correct)

    Mark = Correct / len(AnswerKey_List) * 100

    Marks.append(Mark)


print(StudentName_List)
print(NumberCorrect)
print(Marks)

print()
print("Quiz: {}".format(Title.title()))
print()
print("Student    #Correct    %Grade")
print("-"*29)



for (a, b, c) in zip(StudentName_List, NumberCorrect, Marks):

    print(" {}          {:<1d}       {:>6s}".format(a, b, (FV.FNumber2(c))))