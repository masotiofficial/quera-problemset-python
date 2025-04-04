from collections import Counter


# Problem link: https://quera.org/problemset/60134

def fruits(fruit_list):
    good_fruits = [
        x['name'] for x in fruit_list

        if (x['shape'] == 'sphere') and
           ((x['mass'] >= 300) and (x['mass'] <= 600)) and
           ((x['volume'] >= 100) and (x['volume'] <= 500))
    ]

    return dict(Counter(good_fruits))
