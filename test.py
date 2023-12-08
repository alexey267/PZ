def star():
    global a
    a = a + 1
    print('*' * a)


a = 0
m = int(input('Введите лимит цикла: '))

for i in range(m):
    star()
