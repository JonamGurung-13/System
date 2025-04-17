from readFile import stockProduct

print("Options")
print("-"*7)
print("1. Sell Product")
print("2. Stock Product")
print("3. Restock Product")

choose =int(input("Choose an option: "))

if choose==1:
    print()

elif choose==2:
    stockProduct()

elif choose ==3:
    print()

else:
    print("Invalid choice")