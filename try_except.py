
try:
    print('Yo Try ho')
    # print(YoTryho)
except:
    print('Yo Except ho')
else:
    print('Yo else ho')
finally:
    print('Yo Finally ho')

try:
    with open('try_except_file_1.txt', 'r+') as f:
        try:
            f.write('La balla file vitra xiryo.')
        except:
            print('lekhdaina ta k vako')
except:
    print('k grya bhai yo, k grya?')

y = -1

if y<0:
    raise Exception('No numbers below zero')

x = 'Anmol Sir, Autograph'

if not type(x) is int:
    raise TypeError('No Autograph Please')
