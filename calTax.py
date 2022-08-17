#enter the salary
sal=float(input("Enter Your Salary: Rs")) # sal = salary
#condition
if(sal<250000):
    print("No Tax Payable")
elif(sal>=250000)and(sal<500000):
    print("5% Tax Payable")
    salary=sal-((sal*5)/100)
    print("Salary(After Tax Deduction: Rs",salary)
elif(sal>=500000)and(sal<1000000):
    print("20% Tax Payable")
    salary=sal-((sal*20)/100)
    print("Salary(After Tax Deduction: Rs",salary)
elif(sal>=1000000):
    print("30% Tax Payable")
    salary=sal-((sal*30)/100)
    print("Salary(After Tax Deduction: Rs",salary)