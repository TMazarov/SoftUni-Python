n = int(input())


for i in range(n):
    secret_number = int(input())

    if secret_number == 88:
        print('Hello')
    elif secret_number == 86:
        print('How are you?')
    elif secret_number < 88 and secret_number != 88 and secret_number != 86:
        print('GREAT!')
    elif secret_number > 88:
        print('Bye.')

