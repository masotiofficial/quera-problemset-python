import re


# Problem link: https://quera.org/problemset/21205

def check_registration_rules(**kwargs):
    allowed_usernames = []

    for username, password in kwargs.items():
        if is_valid_username(username) and is_valid_password(password):
            allowed_usernames.append(username)

    return allowed_usernames


def is_valid_username(username):
    return username not in ['quera', 'codecup'] and len(username) >= 4


def is_valid_password(password):
    return len(password) >= 6 and not password.isdigit()
