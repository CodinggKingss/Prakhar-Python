

print("Enter Your Choice From (+,-,*,/)")
ch=input()
print("Enter The Value of A ")
a=input()
a=int(a)
print("Enter The Value of B")
b=input()
b=int(b)
if(ch=="+"):
    c=a+b
    print("Addition Of A & B is : ", c)
elif(ch=="-"):
    if(a>b):
        c=a-b
        print("Subtarction Of A & B is :", c)
    else:
        c=b-a
        print("Subtarction Of A & B is :", c)
elif(ch=="*"):
    c=a*b
    print("Product Of A & B is :", c)
elif(ch=="/"):
    c=a/b
    print("The Divison of A & B is : ", c)
else:
    print("Wrong Choice")
