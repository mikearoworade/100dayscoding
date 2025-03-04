# for in loop
fruits = ['Apple', 'Banana', 'Cherry']
for fruit in fruits:
    print(fruit)
print()

student_score = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 65, 89]

# sum function
total_exam_score = sum(student_score)
print(total_exam_score)

total_score = 0
for score in student_score:
    total_score += score
print(total_score)
print()

# max function
print(max(student_score))

max_score = 0
for score in student_score:
    if score > max_score:
        max_score = score
print(max_score)
