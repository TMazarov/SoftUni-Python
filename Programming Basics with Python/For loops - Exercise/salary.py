# facebook - 150
# instagram - 100
# reddit - 50

open_websites = int(input())
salary = int(input())

for website in range(open_websites):
    current_open_website = input()

    if current_open_website == "Facebook":
        salary -= 150
    elif current_open_website == "Instagram":
        salary -= 100
    elif current_open_website == "Reddit":
        salary -= 50

    if salary <= 0:
        print('You have lost your salary.')
        break
else:
    print(salary)
