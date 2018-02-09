a = 80                #if for while
if a > 90:
    print 'yes'
elif a > 70:
    print 'ok'
else:
    print 'no'

shu = [100, 90, 80, 70]
sum = 0
for dshu in shu: 
    sum = sum + dshu
print sum

x = 0
sum = 0 
while x < 4:
    sum = sum +shu[x]
    x = x + 1
print sum

x = 0 
sum = 0
while True:
    x = x + 1
    if x % 2 == 0:
        continue
    elif x > 20:
        break
    sum = sum + x
print sum

for x in ['a', 'b', 'c']:
    for y in ['1', '2', '3']:
        print x + y 