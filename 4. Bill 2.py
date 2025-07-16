product = input("Enter product name:")
quantity = input("Enter quantity:")
price = input("Enter price:")

bill = int(quantity) * float(price)

print("- - - Thank you for shopping with us - - -") #no formatting option to tidy up code w/out it becoming messy and confusing
print("Product:", product) #best to add a print line for each instruction
print("Quantity:", quantity)
print("Unit price:", price)
print("-----------------------------------------")
print("Your bill is:", bill)
print("-----------------------------------------")