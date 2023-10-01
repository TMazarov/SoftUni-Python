failed_threshold = int(input())

failed_times = 0
solved_problems = 0
grades_total = 0
last_problem = ""
has_failed = True


while failed_times < failed_threshold:
    question = input()

    if question == "Enough":
        has_failed = False
        break

    grade = int(input())

    if grade <= 4:
        failed_times += 1

    grades_total += grade
    solved_problems += 1
    last_problem = question

if has_failed:
    print(f"You need a break, {failed_threshold} poor grades.")
else:
    print(f"Average score: {grades_total / solved_problems:.2f}")
    print(f"Number of problems: {solved_problems}")
    print(f"Last problem: {last_problem}")