#To take input from user.
minimumNo=int(input("Enter the lowest no :")) # minimum =1;
maximumNo = int(input("Enter the highest no :")) # maximum =100;
# to process number minimum (1) to maximum (100)
for number in range (minimumNo,maximumNo+1):
    count =0
# process to find prime number
    for i in range(2,(number//2+1)):
        if (number%i==0):
            count = count+1
            break
    if(count==0 and number!=1):
              print("%d"%number, end = ' ')
