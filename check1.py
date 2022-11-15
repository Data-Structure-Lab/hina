list1=[1,5,10,20]
list2=[2,4,15,15]
if (len(list1))==(len(list2)):
    print("True")
else:
    print("False")
l1=0
for i in range(0,len(list1)):
    l1=l1+list1[i]
print("Sum of all elements in given list1: ",l1)
l2=0
for i in range(0,len(list2)):
    l2=l2+list2[i]
print("Sum of all elements in given list2: ",l2)
if l1==l2:
    print("Sum is Equal")
else:
    print("Sum not Equal")
