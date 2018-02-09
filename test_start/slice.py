#coding:utf-8   slice 切片
L = range(1, 50)
print L[0:5]
print L[2::3]
print L[4:40:5]

L = range(1, 101)
print L[-10:]
print L[-46::5]
print L[4::5][-10:]

def firCharUpper(s):
    return s[0:1].upper()+s[1:]
print firCharUpper('hello')
print firCharUpper('mary')
print firCharUpper('ok')