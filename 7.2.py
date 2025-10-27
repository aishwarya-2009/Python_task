def exam_score(student_answers,correct_answers):
    score=0
    for s,c in zip(student_answers,correct_answers):
        if s==c:
            score+=1
    percentage=(score/len(correct_answers))*100
    return score,percentage
student=['A','B','C','D','A']
answer_key=['A','C','C','D','B']
print(exam_score(student,answer_key))
