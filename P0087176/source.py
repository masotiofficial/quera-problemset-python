# Problem link: https://quera.org/problemset/87176

def game(number):
    digit_one = number // 10
    digit_two = number % 10

    return max(digit_one, digit_two) - min(digit_one, digit_two)