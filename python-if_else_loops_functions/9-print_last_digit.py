def print_last_digit(number):
    last_digit = abs(number)
    while last_digit > 9:
        last_digit %= 10
    print(last_digit, end='')
    return last_digit
