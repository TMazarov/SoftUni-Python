student_name = input()

years_counter = 0
total_grades = 0
average_grade = 0
failed_years = 0

while True:
    annual_grade = float(input())
    years_counter += 1

    if annual_grade < 4:
        failed_years += 1
        if failed_years == 2:
            print(f"{student_name} has been excluded at {years_counter} grade")
            break
        years_counter -= 1
    else:
        total_grades += annual_grade

    if years_counter == 12:
        average_grade = total_grades / 12
        print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
        break
