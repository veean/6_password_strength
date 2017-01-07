# 6_password_strength

* Cкрипт вычисляет сложность пароля, поданного на входб оценивая пароль в диапазоне [1, 10], 
где 1 - очень слабый пароль, 10 - очень сильный.
*  Также на вход скрипту необходимо подать файл, c плохими (часто используемыми) паролями.
* По умолчанию 
    
    
    https://wiki.skullsecurity.org/images/c/ca/500-worst-passwords.txt

Пример запуска скрипта: 
    
    python password_strength.py  path_to_password_blacklist