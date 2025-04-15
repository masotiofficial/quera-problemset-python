# Problem link: https://quera.org/problemset/102248

def compare(string_one, string_two):
    while string_one and string_two:
        first_char_string_one = string_one[0]
        first_char_string_two = string_two[0]

        compare_first_chars = ord(first_char_string_one) - ord(first_char_string_two)

        if compare_first_chars == 0:
            string_one = string_one[1:]
            string_two = string_two[1:]

        elif compare_first_chars >= 0:
            string_two = string_two[1:]

        elif compare_first_chars <= 0:
            string_one = string_one[1:]

        if string_one and string_two:
            string_one = ''.join(reversed(string_one))
            string_two = ''.join(reversed(string_two))

    if string_one:
        return string_one
    elif string_two:
        return string_two
    else:
        return 'Both strings are empty!'
