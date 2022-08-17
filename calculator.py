print("This is a simple calculator")
#Input two no
print("Enter two numbers")
a=int(input("a: "))
b=int(input("b: "))
#no for work
print("press 1 to add",a,"and",b) #1 for add
print("press 2 to subtract",a,"and",b) #2 for sub
print("press 3 to multiply",a,"and",b) #3 for muit
print("press 4 to divide",a,"and",b) #4 for div
#Enter choice
choice=int(input(">>"))
#out of choice
if(choice<1)or(choice>4):
    print("Wrong Choice")
#add
elif(choice==1):
    print(a,"+",b,"=",a+b)
#sub
elif(choice==2):
    print(a,"-",b,"=",a-b)
#muit
elif (choice == 3):
    print(a, "*", b, "=", a * b)#div

elif(choice==4):
    print(a,"/",b,"=",a/b)