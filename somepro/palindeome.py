n = int(input('enter the number:'))
temp = n
rev = 0
while n>0:
    last = n%10
    n = n//10
    rev = (rev*10)+last
print('reveserd number is:', rev)
if rev ==temp:
    print('is palindrom')
else:
    print('is not palindrome')