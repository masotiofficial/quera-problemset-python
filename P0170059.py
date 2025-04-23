# Problem link: https://quera.org/problemset/170059

positions = {
    1: (0, 0),
    2: (0, 1),
    3: (1, 0),
    4: (1, 1)
}

n = int(input())
m = int(input())

x_n, y_n = positions[n]
x_m, y_m = positions[m]

print(abs(x_n - x_m) + abs(y_n - y_m))