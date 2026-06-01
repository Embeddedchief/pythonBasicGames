line01 = "********************"
line02 = "*                  *"
line03 = "*     WELCOME!     *"


print(line01)
print(line02)
print(line03)
print(line02)
print(line01)


weather = 'void'

if weather == 'Sunny':
    print('Its sunny')
elif weather == 'Raining':
    print('Its Raining')
else:
    print('its neither Raining or sunny')


print('Another way to use if and else condition (Teneray)')

weather = 'Raining'

print('Its raining') if weather == 'Raining' else print ('Its not raining, it might be sunny or void')