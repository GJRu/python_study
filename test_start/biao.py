print [x * (x+1) for x in range(1, 10, 2)]

d = { 'aaa': 11, 'bbb': 22, 'ccc': 33 }
def ge(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)
tds = [ge(name, score) for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'

def strup(L):
    return [x.upper() for x in L if isinstance(x,str)]
print strup(['He', 'she', 187])

print [x*100+y*10+z for x in range(1,10) for y in range(0,10) for z in range(0,10) if cmp(x,z)==0]