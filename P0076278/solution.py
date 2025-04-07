# Problem link: https://quera.org/problemset/76278

def calculator(n, m, li):
    new_li = []

    for i in range(0, (n // m) + 1):
        new_li.append(sum(li[i * m:i * m + m]) * (1 if i % 2 == 0 else -1))

    final_value = sum(new_li)

    return final_value