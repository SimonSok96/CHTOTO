import random
a = random.randint(1,10)
b = int(input('Угaдай число: '))
while a != b:
    if a < b:
        print('\n', 'Меньше')
        b = int(input('Угaдай число: '))
    else:
        print('\n', 'Больше')
        b = int(input('Угaдай число: '))
print('\n', 'Угaдал!')
