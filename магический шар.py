import random

answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом, Мне кажется - да',\
'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да', 'Пока неясно', 'попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',\
'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
print('Как тебя зовут?')
name = input()
print('Привет, {}'.format(name))


flag = True

while flag == True:
    question = input('Задай мне вопрос, который тебя интересует:  ')
    print()
    print(random.choice(answers))
    print()
    print('Хочешь задать еще вопрос?: (да/нет)')
    question_end = input()
    if question_end == 'нет':
        print('Пока(((')
        flag = False





        
    

        
    
