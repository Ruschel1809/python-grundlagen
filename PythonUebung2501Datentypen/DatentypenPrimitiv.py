i=1
f=2.0
c=3+4j
s='string'
t=('e',5)
l=[6,7,8]
set={'a','n'}
print(type(i))
print(type(f))
print(type(c))
print(type(s))
print(type(t))
print(type(l))
print(type(set))
print(float(i))
print(str(i))
newList=[l[0], l[1]]
if list(t)[1] not in newList:
    newList.append(list(t)[1])
print(newList)
set.add('a')
print(set)
set.add('b')
print(set)