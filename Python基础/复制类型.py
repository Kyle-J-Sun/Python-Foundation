# Direct Assignment
a = [3,4,5]
b = a
print(a == b)
b[0] = 9998
print(b)
print(a)
print(id(a))
print(id(b))

# Shallow Copy
import copy
a = [4,5,3,1]
b = copy.copy(a)
print(a,b,id(a),id(b))
c = [4,2,[3,1,2]]
d = copy.copy(c)
print(c,'\n',d,'\n',id(c),id(d),'\n',id(c[2]),id(d[2]))

# Deep Copy
import copy
a = [2,1,3,[3,1,2]]
b = copy.deepcopy(a)
print(a,'\n',b,'\n',id(a),id(b),'\n',id(a[3]),id(b[3]))
