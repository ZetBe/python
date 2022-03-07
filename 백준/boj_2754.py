#2754 학점계산
a = input()
if a == 'A+':
    grade = 4.3
elif a == 'A0':
    grade = 4.0
elif a == 'A-':
    grade = 3.7
elif a == 'B+':
    grade = 3.3
elif a == 'B0':
    grade = 3.0
elif a == 'B-':
    grade = 2.7
elif a == 'C+':
    grade = 2.3
elif a == 'C0':
    grade = 2.0
elif a == 'C-':
    grade = 1.7
elif a == 'D+':
    grade = 1.3
elif a == 'D0':
    grade = 1.0
elif a == 'D-':
    grade = 0.7
elif a == 'F':
    grade = 0.0
print(grade)
