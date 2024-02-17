# Program to compute sum of digit in a given number
print("Program to compute sum of digit in a given number")
num=int(input("Enter any number:"))
sum=0
while num>0:
    rem=num%10
    sum=sum+rem
    num=num//10
print(sum," is sum of given number\n\n")

# Program to display numbers using for loop
print("Program to display numbers using for loop")
num=int(input("Enter a number: "))
for i in range(1,num+1):
    print(i,end=" ")

#Program to compute sum of digit in a given number
print("\n\nProgram to compute sum of number frm 1 to a given number")
sum=0
num=int(input("Enter any number: "))
for i in range(1,num+1):
    sum=i+sum
print("Sum of given natural numbers is:" ,sum)

# Program to find factorial of any number
print("\n\nProgram to find factorial of any number")
num=int(input("Enter any number : "))
ans=1
if num<0:
    print("Value must be non-negative !")
else:
    for i in range(1,num+1):
        ans=ans*num
    print("Factorial result is : ",ans)
