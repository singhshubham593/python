#creating list
list = []
#taking no input
num= int(input("Enter number of elements : "))
#taking element and storing in list
for i in range(0, num):
    print("Element(",i,") :",end=' ')
    element = int(input())
    list.append(element)
# show in array form
print(list)
sum=0
for i in range(0, num):
# for sum element+
    sum=sum+list[i]
print("Sum is ",sum)
#for avarage of element
avg=sum/num
print("Avarage is ",avg)