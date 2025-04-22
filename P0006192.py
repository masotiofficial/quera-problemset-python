# Problem link: https://quera.org/problemset/6192

a, b, c, d, e, f = map(int, input().split())

def can_fit(width, length):  
    return (width <= a and length <= b) or (width <= b and length <= a)

if can_fit(d, e) or can_fit(d, f) or can_fit(e, f):
    print("zende mimuni")
else:
    print("dari mimiri")