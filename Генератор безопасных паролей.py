import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

def pass_question():
    global num_pass, len_pass
    passw = ''
    print('Введите необходимое количество генерируемых паролей:')
    num_pass = int(input())
    print('Введите длину пароля: ')
    len_pass = int(input())
    print('Пароль должен включать цифры? да/нет: ')
    question_digit = input()
    if question_digit == 'да':
        passw += digits
    print('Включать ли прописные буквы в пароль? да/нет: ')
    question_uppercase_letters = input()
    if question_uppercase_letters == 'да':
        passw+=uppercase_letters
    print('Включать ли строчные буквы в пароль? да/нет: ')
    question_lowercase_letters = input()
    if question_lowercase_letters == 'да':
        passw+=lowercase_letters
    print('Включать ли символы !#$%&*+-=?@^_ ? да/нет: ')
    question_punctuation = input()
    if question_punctuation == 'да':
        passw+=punctuation
    return passw

def pass_generation():
    password_gen = ''
    for i in range(num_pass):
        password_gen = random.sample(password, len_pass)
        print('Уникальный пароль:')
        print(''.join(password_gen))
    print('Генерация завершена, выберите наилучший!')

    


print('Добрый день, ответьте на пару вопросов и мы вам сгенерируем уникальный пароль!')
password = pass_question()
pass_generation()
.


        
        
    
    


    
