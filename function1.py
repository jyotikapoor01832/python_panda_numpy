def findSquare(x):
    y=x*x
    return  y

def findCube(x):
    z=x*x*x
    return z

num= int(input("Enter any value : "))
res= findSquare(num)   
print("Square of given number is : ",res )
res= findCube(num)
print("Cube of given number is : ",res)