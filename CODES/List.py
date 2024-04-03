#List...........

marks=[11,12,13]
print(marks,"\n")

#in list we can store differnt datatypes values
a=[10,20,30,"hindi","english","maths",10.25,20.65,0.42,True,False]
print(a,"\n")

#print element from specific index
print(a[1])
print(a[5])
print(a[8])
print(a[9],"\n")

#print element from list but from backward...
print(a[-1])
print(a[-6],"\n")

#print element from list from range ex:2-5
print(a[2:8],"\n")

#adding new element at end..
a.append(56)
print(a,"\n")

#inserting element at any index
a.insert(1,45)
print(a,"\n")

#length of the list
print(len(a),'\n')

#finding element from the list
print(20 in a)
print(25 in a,'\n')

#print element using for loop
for i in a:
    print(i)

print("\n")

#print element using while loop
i=0
while i<len(a):
    print(a[i])
    i=i+1

print("\n")
#to clear whole list...
a.clear()
print(a)