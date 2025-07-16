sal = 100

if sal>=2000:
    tax = sal*21/100
else:
    tax = sal*15/100

net = sal - tax

print("Your salary", sal)
print("Tax calculated is:", tax)
print("Net salary:", net)