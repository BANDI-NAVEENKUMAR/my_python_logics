s = "queen"
cou = 0
re = ""
for i in s:
    cou1 = s.count(i)
    if cou < cou1:
        cou = cou1
        re=i
print(re)


