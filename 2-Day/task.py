# Assignment Operator
score = 0
height = 1.8
is_winning = True

# User scores a point
score += 1
print(score)

# f-string
print("Your score is " + str(score))  # Not convenient
print(f"Your score is = {score}, your height is = {height}. You are winning: {is_winning}")
