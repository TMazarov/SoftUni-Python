def loading_bar(num):
    display_bars = number // 10

    result = "[" + "%" * display_bars + '.' * (10 - display_bars) + "]"

    if num < 100:
        return f'{num}% {result}\nStill loading...'
    else:
        return f'{num}% Complete!\n{result}'


number = int(input())
print(loading_bar(number))
