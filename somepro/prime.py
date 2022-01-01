# prime =int(input("enter the prime number:"))
# prime1 = True
# for i in range(2,prime):
#     if prime%i==0:
#         prime1 = False
#         break
# if prime1 == True:
#     print(prime,'is prime')
# else:
#     print(prime,'not prime')

n = int(input('enter the number:'))
prime = True
for i in range(2,n):
    if n % i == 0:
        prime = False
        break
if prime == True:
    print('is prime')
else:
    print('is not prime')


