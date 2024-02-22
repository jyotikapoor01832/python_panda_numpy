def factorial(n):
    y=1
    for i in range(1,n+1):
        y=y*i
    return y
def rfact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*rfact(n-1)
    
num=int(input("Enter any value :"))
res=factorial(num)
print("Factorial of a given number is :",res)
r= rfact(num)
print("Recursive factorial of a given number is :",r)