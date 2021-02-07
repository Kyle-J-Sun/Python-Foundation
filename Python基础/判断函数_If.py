date = input();
if date == '1':
    print('Monday')
elif date == '2':
    print('Tuesday')
elif date == '3':
    print('Wednesday')
elif date == '4':
    print('Thursday')
elif date == '5':
    print('Friday')
elif date == '6':
    print('Saturday')
else: print('Sunday')

year = int(input())
if (year%4 == 0 and year%100 != 0) or year%400 == 0:
    print('%d is a leap year' % year)
else:
    print('%d is not a leap year' % year)


i = 0
while i<100:
    print('this is %d' % i)
    i = i + 1
print('That\'s the end')
