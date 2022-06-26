with open('myersbriggs.txt', mode='w') as mb_questions:
    for question in mb_questions.readlines():
        user_response = input(question.lower())