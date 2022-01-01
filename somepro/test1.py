l = [1,2,3,4,1,2,3,4,6,8,1,2]

for i in l:
    c = l.count(i)
    if c>1:
        for j in range(len(l)):
            if i in l:
                l.remove(i)
print(l)
