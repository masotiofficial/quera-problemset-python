# Problem link: https://quera.org/problemset/129726

def separator(numbers):
    return (
        [x for x in numbers if x % 2 == 0],
        [x for x in numbers if x % 2 != 0]
    )
