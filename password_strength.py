import getpass
import requests
import re
import sys
import os


DEFAULT_PASSWORDS_LIST_URL = 'https://wiki.skullsecurity.org/images/c/ca/500-worst-passwords.txt'


def check_bad_passwords_online(password_to_check):
        passwords_list = requests.get(DEFAULT_PASSWORDS_LIST_URL).text.splitlines()
        if password_to_check not in passwords_list:
            return True


def get_bad_passwords_from_file(filepath):
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r') as data:
                bad_passwords = data.read().split("\n")
                return bad_passwords
        except FileNotFoundError:
            return None


def check_bad_passwords_offline(password, bad_passwords):
    if bad_passwords:
        if password not in bad_passwords:
            return True


def has_upper_and_lower_symbols(password):
    upper_check = any([symbol.isupper() for symbol in password])
    lower_check = any([symbol.islower() for symbol in password])
    if upper_check and lower_check:
        return True


def has_spec_chars(password):
    if re.findall(r'[!@#$%^&*><}{]', password):
        return True


def has_digits(password):
    if any([symbol.isdigit() for symbol in password]):
        return True


def check_in_blacklists(password, blacklist=None):
    if blacklist:
        return check_bad_passwords_offline(password, get_bad_passwords_from_file(blacklist))
    else:
        return check_bad_passwords_online(password)


def get_password_strength(password, blacklist=None):
    strength_state = 1

    if len(password) >= 8:
        strength_state += 2

        if has_upper_and_lower_symbols(password):
            strength_state += 2
        if has_digits(password):
            strength_state += 1
        if has_spec_chars(password):
            strength_state += 2
        if check_in_blacklists(password, blacklist):
                strength_state += 2

    return strength_state


if __name__ == '__main__':
    user_password = getpass.getpass('Введите ваш пароль : ')
    try:
        pass_list = sys.argv[1]
    except IndexError:
        pass_list = None
    print('Сложность пароля по 10-бальной шкале: {} '.format(get_password_strength(user_password, pass_list)))

