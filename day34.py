
def reverse_number(number):
    rev = 0

    a = number % 10
    rev = rev * 10 + a
    number = number // 10

    b = number % 10
    rev = rev * 10 + b
    number = number // 10

    c = number % 10
    rev = rev * 10 + c

    return rev