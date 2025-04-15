from math import pi


# Problem link: https://quera.org/problemset/33473

def get_func(shapes):
    calculate_areas = []

    for shape in shapes:
        if shape == 'square':
            calculate_areas.append(lambda x: x * x)
        elif shape == 'circle':
            calculate_areas.append(lambda r: pi * r * r)
        elif shape == 'rectangle':
            calculate_areas.append(lambda x, y: x * y)
        elif shape == 'triangle':
            calculate_areas.append(lambda x, y: 0.5 * x * y)

    return calculate_areas
