#Example with comma
print """Я бы не хотел никогда услышать, как он говорит: '''Она сказала: "Он сказал: 'Дай мне двести рублей'"'''"""

#
my_object = 'Test' # True example
# my_object = '' # False example

if len(my_object) > 0:
    print('my_object не пуст')

if len(my_object):  # 0 преобразовывается к False
    print 'my_object не пуст'

if my_object != '':
    print 'my_object не пуст'

if my_object: # пустая строка преобразовывается к False
    print 'my_object не пуст'

