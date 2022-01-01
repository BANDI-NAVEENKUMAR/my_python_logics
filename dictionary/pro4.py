x = {}
n = int(input("how many key value pairs:"))
i=1
while i<=n:
    x[input("enter the string key")] = int(input("enter the value"))
    i =i+1
print(x)