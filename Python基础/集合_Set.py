#Sets      use {} to create a set
# No Orders No Repeats
lst1 = [1,1,1,3,3,3,3,3,3,5,6,6,7,7,8,8,8,8,8,9,2,332,4,3,3,5,3,5]
lst2 = set(lst1)
# print(lst2) # use sets to remove the duplicates
lst2.add('h')
# print(lst2)
lst2.remove(1)
# print(lst2)

l1 = {1,1,2,3,5,4,4,5,5,6,6,8}
l2 = {6,7,7,3,5,1,2,2,2,5}
print(type(l1))
print(l1,l2)
l3 = set()
l3 = l2.intersection(l1) # intersection between l1 and l2.
itsct = l1 & l2
print(itsct)
print(l3)

l1 = {1,1,2,3,5,4,4,5,5,6,6,8}
l2 = {6,7,7,3,5,1,2,2,2,5}
l7 = l1.union(l2) # find the union between l1 and l2 sets.
print(l7)
l8 = l1 | l2
print(l8)

l1 = {1,1,2,3,5,4,4,5,5,6,6,8}
l2 = {6,7,7,3,5,1,2,2,2,5}
l4 = l1.difference(l2) # find the difference between l1 and l2 (exist in l1 but not in l2)
print(l4)
diff = l1 - l2
print(diff)
l5 = l2.difference(l1)# find the difference between l1 and l2 (exist in l2 but not in l1)
print(l5)
diff2 = l2 - l1
print(diff2)
l6 = l1.symmetric_difference(l2) # find the difference between l1 and l2 sets.
print(l6)
diff3 = l2 ^ l1
print(diff3)

l1 = {1,1,2,3,5,4,4,5,5,6,6,8}
l2 = {6,7,7,3,5,1,2,2,2,5}
print(l1.pop())
print(l1)

l1 = {1,1,2,3,5,4,4,5,5,6,6,8}
l2 = {6,7,7,3,5,1,2,2,2,5}
print(l1.pop())
print(l1)
l2.discard(5)
print(l2)
l2.clear()
print(l2)
l2.update([10,70,5,55,23])
print(l2)