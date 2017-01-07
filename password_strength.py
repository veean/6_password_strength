import getpass
import requests


def get_password_strength(password):
    strength_state = 0
    special_char_edge = 126

    if len(password) >= 8:
        strength_state += 2
    if any([symbol.isupper() for symbol in password]):
        strength_state += 1
    if any([symbol.islower() for symbol in password]):
        strength_state += 1
    if any([symbol.isdigit() for symbol in password]):
        strength_state += 1
    if any([ord(symbol) < special_char_edge for symbol in password]):
        strength_state += 2
    if getpass.getuser() not in password:
        strength_state += 1
    if check_bad_passwords(password):
        strength_state += 2

    return strength_state


def check_bad_passwords(password):
    url = 'https://wiki.skullsecurity.org/images/c/ca/500-worst-passwords.txt'  # simple list of 500 bad passes
    try:
        r = requests.get(url).text.splitlines()
        for item in r:
            if password in item:
                return True
    except requests.exceptions.ConnectionError:
        return False

if __name__ == '__main__':
    print("Please enter your password: ")
    password_ = input('Введите ваш пароль\n')
    print(get_password_strength(password_))
