# n = int(input('enter the number:'))
# a = 0
# b = 1
# for i in range(n):
#     c = a + b
#     a = b
#     b = c
#     print(c)

# r = 0
# s = 1
# for z in range(10):
#     t = r + s
#     r = s
#     s = t
#     print(t)


x = 0
y = 1
print(x)
print(y)
z = x + y
while z<100:
    print(z)
    x = y
    y = z
    z = x + y