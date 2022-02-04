import random
x = random.randint(1,100)
print('Добро пожаловать в числовую угадайку')

def is_valid(n):
    if n.isdigit():
        if 1<=int(n)<=100:
            return True
        else:
            print('Введите число в диапазоне 1-100')
            return False
    else:
        print('Вы ввели недопустимые данные, попробуйте еще раз :')
        return False

count = 0
flag = True
while flag == True:
    n = input('Введите число : ')
    if is_valid(n) == False:
        continue
    count+=1
    if int(n) < x:
        print('Слишком маленькое число, попробуйте еще раз.')
    elif int(n)>x:
        print('Слишком большое число, попробуйте еще раз.')
    else:
        print('Congralutation! you win, угадано за {} попыток'.format(count))
        flag = False
        print('Сыграем еще раз? да/нет:')
        f = input()
        if f == 'да':
            flag = True
        else:
            print('Всего доброго')
        
    

        
    
