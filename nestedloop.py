# Find biggest among two given numbers
num1=int(input("Enter first value: "))
num2=int(input("Enter second value:"))
if num1!=num2:
    if num1>num2:
        print(num1,"is biggest")
    else:
        print(num2,"is biggest")
else:
    print("Both values are same !!")