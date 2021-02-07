dict = {'a':5,'b':'Kyle'}
print(
    type(dict),
    dict['b']
    )
dict2 = {'Name1':'Kyle','Name2':'Habi','Age1':34,'Age2':55}
print(
    dict2,
    dict2.fromkeys([1,2,3],0),
    dict2.get('Name2','Not Exist'),    #just show the value not copy to the dict.
    dict2.setdefault(input(),'No Values'),  #Copy not-exist values to the dict.
    dict2
)
dict = {'a':5,'b':'Kyle'}
dict2 = {'Name1':'Kyle','Name2':'Habi','Age1':34,'Age2':55}
print(input() in dict2) # Keys not values
print(dict2.keys())  # return all keys in dict2
print(dict2.values()) # return all the values in dict2
print(dict2.update(dict))

dict = {'a':5,'b':'Kyle'}
dict2 = {'Name1':'Kyle','Name2':'Habi','Age1':34,'Age2':55}
dict2.update(dict) # to update values in dict into dict2
print(dict2)