num =int(input("Enter the number :"))
#first no and second no is always 0 and 1.
n1=0
n2=1
print(n1)
print(n2)
#process to  generate fabonacci seriea
for i in range(2,num):
    n3=n2+n1
    print(n3)
# update values
    n1=n2
    n2=n3