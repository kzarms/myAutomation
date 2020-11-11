#Example with comma
print """Я бы не хотел никогда услышать, как он говорит: '''Она сказала: "Он сказал: 'Дай мне двести рублей'"'''"""

#
my_object = 'Test' # True example
# my_object = '' # False example


def f(sum, l=[]):
    l.append(sum)
    print(l)

l = [1]
f(10)