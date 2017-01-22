# 6_password_strength

Cкрипт вычисляет сложность пароля, поданного на вход, оценивая пароль в диапазоне [1, 10], 
где 1 - очень слабый пароль, 10 - очень сильный.
*  На вход скрипту можно подать файл (необязательный параметр), c плохими (часто используемыми) паролями.
* По умолчанию список плохих паролей подсматривается  [тут](https://wiki.skullsecurity.org/images/c/ca/500-worst-passwords.txt)


##Установка скрипта и зависимостей

    git clone https://github.com/veean/13_cinemas.git
    cd 13_cinemas
    pip install -r requirements.txt

##Применение

Пример запуска скрипта: 
    
    $python password_strength.py  [path_to_password_blacklist]
     Введите ваш пароль :
     Сложность пароля по 10-бальной шкале: 8 балл(ов)
     

 