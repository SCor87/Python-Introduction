sal = 200

if sal>=1000:

    if sal>=2000:
        tax = sal*21/100
    else:
        tax = sal*15/100

else:
    tax = 0

net = sal - tax
print("Salary:", sal)
print("Tax calculated:", tax)
print("Net salary:", net)