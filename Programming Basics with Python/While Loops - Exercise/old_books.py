desired_book = input()

books_checked = 0
found_desired_book = False

while True:

    current_book = input()

    if current_book == desired_book:
        found_desired_book = True
        break

    if current_book == "No More Books":
        break

    books_checked += 1

if found_desired_book:
    print(f"You checked {books_checked} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {books_checked} books.")
