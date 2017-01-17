import getpass
import requests
import re


DEFAULT_PASSWORDS_LIST_URL = 'https://wiki.skullsecurity.org/images/c/ca/500-worst-passwords.txt'


def check_bad_passwords_online(password_to_check):
    # url = 'https://wiki.skullsecurity.org/images/c/ca/500-worst-passwords.txt'  # simple list of 500 bad passes
    try:
        r = requests.get(DEFAULT_PASSWORDS_LIST_URL).text.splitlines()
        for item in r:
            if password_to_check in item:
                return True
    except requests.exceptions.ConnectionError:
        return False


def get_bad_passwords_from_file(filepath):
    try:
        with open(filepath, 'r') as data:
            bad_passwords = data.read().split("\n")
            return bad_passwords
    except FileNotFoundError:
        return None


def check_bad_passwords_offline(password, bad_passwords):
    if password not in bad_passwords:
        return


def has_upper_and_lower_symbols(password):
    upper_check = any([symbol.isupper() for symbol in password])
    lower_check = any([symbol.islower() for symbol in password])
    if upper_check and lower_check:
        return True


def get_password_strength(password, blacklist=None):
    strength_state = 1

    if len(password) >= 8:
        strength_state += 2
        if has_upper_and_lower_symbols(password):
            strength_state += 2
        if any([symbol.isdigit() for symbol in password]):
            strength_state += 1
        if re.findall(r'[!@#$%^&*><}{]', password):
            strength_state += 2
        if blacklist:

            strength_state += 2
        return strength_state
    else:
        return 1


if __name__ == '__main__':
    user_password = getpass.getpass('Введите ваш пароль\n')
    print(get_password_strength(user_password))
