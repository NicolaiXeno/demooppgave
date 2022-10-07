Input = ''
while not Input.isdigit() and not len(Input) == 1:
    Input = input('Oppgi en tall: ')

for i in range(1,Input+1):
    if i > 1:
        print('{} lakser'.format(i))
    else:
        print('{} laks'.format(i))
    




