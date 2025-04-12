import re


# Problem link: https://quera.org/problemset/87181

def words_check(text):
    result = {}

    for word in text.split():
        clear_word = re.sub(r"[^a-zA-Z]", "", word)

        if len(clear_word) > len(word) / 2:
            formatted_word = clear_word.capitalize()

            result[formatted_word] = result.get(formatted_word, 0) + 1

    return dict(sorted(result.items()))
