#input first and second no
n1=int(input("Enter the first number : "))
n2=int(input("Enter the second number : "))
#for gcd
def gcd(sm,bi):
    for i in range(1,sm+1):
        if(sm%i==0)and(bi%i==0):
            gcd=i

    return gcd
#compare ni and n2
if n1 > n2:
        small = n2
        big=n1
else:
    small = n1
    big = n2

print("GCD of ",n1,"and",n2,"is",gcd(small,big))