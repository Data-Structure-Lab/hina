a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if a>b and a>c:
    print("a is the biggest number")
elif b>a and b>c:
    print("b is biggest number")
elif c>a and c>b:
    print("c is biggest number")
elif a==b and a==c:
    print("All numbers are equal")
elif a==b:
    print("a and b are equal")
elif a==c:
    print("a and c are equal")
elif b==c:
    print("b and c are equal")
    
