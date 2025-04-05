# Problem link: https://quera.org/problemset/175884

def calculate_floor(string):
    floor = 0

    for char in string[:4]:
        if char == 'U':
            floor += 1
        else:
            floor -= 1

    return floor