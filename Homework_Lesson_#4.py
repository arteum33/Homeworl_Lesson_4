# Задача 1
'''
Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка
(могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random);
'''

import random
names = ['Cвобода','Мичие', 'Эсат', 'Харум', 'Хуртулав', 'Каскар', 'Апелл', 'Дзиппо', 'Азахат', 'Гаджима', 'Аюр',
         'Халакав', 'Фируз' , 'Азахат', 'Изнифат', 'Ленмар', 'Болат', 'Мархай', 'Азахат', 'Лютфий', 'Лютфий', 'Лютфий',
         'Лютфий', 'Лютфий', 'Сафуан', 'Мидекчеп', 'Максентий', 'Милодара', 'Эсберген', 'Ях', 'Гирмасолта']

def f(names, n):
    print('Задача №1\n','Выборка из',n,'случайных имен:',random.sample(names, k=n))
f(names, 10)


# Задача 2
# Напишите функцию вывода самого частого имени из списка на выходе функции F;

def f(names):
    counter = 0
    num = names[0]

    for i in names:
        most_apper_list = names.count(i)
        if(most_apper_list> counter):
            counter = most_apper_list
            num= i
    return num

print('Задача №2\n','Самое часто встречаемое имя: ', f(names))


# Задача 3
# Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.


def f(word_letters):
    word_letters = sorted(word_letters, reverse=False)
    for word_letter in word_letters:
        first_letter = word_letter[0]

    return (first_letter)

print('Задача №3\n', 'Самая редкая первая буква имен: ', f(names))


# Задача 4
# В файле с логами   https://drive.google.com/open?id=1pKGu-u2Vvtx4xK8i2ZhOzE5rBXyO4qd8 найти дату самого позднего лога (по метке времени)
logs_list = ['2011-08-01 18:03:34,338 - exampleApp - INFO - Program started',
             '2012-09-02 19:13:53,338 - exampleApp - INFO - added 7 and 8 to get15',
             '2012-10-02 20:23:31,338 - exampleApp - INFO - Done!',
             '2013-08-01 01:43:33,338 - exampleApp - INFO - Program started',
             '2011-09-19 12:53:33,338 - exampleApp - INFO - added 10 and 11 to get15',
             '2012-10-12 22:03:33,338 - exampleApp - INFO - Done!',
             '2017-08-01 01:13:51,338 - exampleApp - INFO - Program started',
             '2019-09-19 12:21:34,338 - exampleApp - INFO - added 7 and 8 to get15',
             '2018-10-12 23:31:01,338 - exampleApp - INFO - Done!']


def f(logs):
    for log in logs:
        log_time = log[11:19]
    return str(log_time)
print('Задача №4\n', 'Самый последний LOG: ', f(logs_list))
