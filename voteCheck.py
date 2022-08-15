age =int(input("Enter the age of the person :"))
if age>18:
    print("person can vote.")
else:
    print("Person cannot vote.")
    wait = 18-age
    print("person can wait for :")
    print(wait)