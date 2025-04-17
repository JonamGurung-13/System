from readFile import *

print("Options")
print("-"*7)
print("1. Sell Product")
print("2. Stock Product")
print("3. Restock Product")

choose =int(input("Choose an option: "))

if choose==1: #Enble sell option
    sellProduct()

elif choose==2: #Display product details
    stockProduct()

elif choose ==3: #Enable restock option
    restockProduct()

else:
    print("Invalid choice")