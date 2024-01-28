def check_pwd(pwd):
    is_valid = True

    if not (6 <= len(pwd) <= 10):
        print('Password must be between 6 and 10 characters')
        is_valid = False
    if not pwd.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False
    if sum(d.isdigit() for d in pwd) < 2:
        print('Password must have at least 2 digits')
        is_valid = False

    if is_valid:
        return "Password is valid"


password = input()
result = check_pwd(password)

if result is not None:
    print(result)
