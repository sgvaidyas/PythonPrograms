"""
Factorial
n=4 1*2*3*4 =24

"""
n = int(input("Enter the val = "))
prod = 1
s = ""
for i in range(1,n+1):
    prod = prod*i
    s = s+str(i)+"*"
print("Factorial of {0} is {1} = {2}".format(n,s[:-1],prod))