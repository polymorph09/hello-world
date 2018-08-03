a = int(input('Введіть число: '))
s = ''
for i in range(0,a):


    if (i % 2 == 0):
        s += 'Fizz'
    else:
        s += 'Buzz'

print(s)
