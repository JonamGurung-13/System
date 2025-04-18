from datetime import datetime

#This function is to show the detail of product
def stockProduct():
    file = open('products.txt','r')
    detail = file.readlines()
    print(f"{'Product':25}{'Brand':20}{'Quantity':15}{'Price':15}{'Country':15}")
    print("-"*90)

    for line in detail:
        product,brand,quantity,price,country = line.strip().split(", ")
        print(f"{product:25}{brand:20}{quantity:15}{price:15}{country:15}")
    file.close()


#This function is for creating customer invoice
def sellProduct():
    #This takes input from user
    customerName = input("Enter customer name: ")
    productName = []
    productQuantity = []
    totalQuantity =[]
    free = 0
    price = []

    i = 0
    while i>=0:
        productName.append(input("Enter product name: "))
        productQuantity.append(int( input("Enter the quantity of product: ")))
        if productQuantity[i]>=3:
            free = int(productQuantity[i]/3)
            totalQuantity.append(productQuantity[i] + free)

        else:
            totalQuantity.append(productQuantity[i])
    
        anotherProduct = input("Do you want to buy another product (Yes/No): ")
        if anotherProduct.lower()=="yes":
            i+=1
            continue

        else:
            #Reading product text file for selling product
            with open("products.txt","r") as file:
                detail =  file.readlines()

            print("Invoice No.: CINV" + datetime.now().strftime("%y%m%d"))
            print("Customer's name: "+customerName)
            print("Date and Time: "+ datetime.now().strftime("%Y-%m-%d, %H:%M:%S"))
            print(f"{'Product':25}{'Brand':20}{'Quantity':15}{'Rate(Rs)':15}{'Price':15}")
            print("-"*90)
            price = []
            for line in detail:
                product,brand,quantity,rate,country = line.strip().split(", ")
                for j in range(len(productName)):
                    if product == productName[j]:
                        rate = int(rate)
                        productPrice = rate*productQuantity[j]
                        price.append(productPrice)
                        print(f"{product:25}{brand:20}{totalQuantity[j]:<15}{rate:<15}{productPrice:<15}")

            print("-"*90)
            total = 0
            for a in range(len(price)):
                total = total + price[a]
            print(f"{'Total':75}{total}")

            #Writing customer invoice for selling product
            with open("customerInvoice.txt","w") as invoice:
                invoice.write("Invoice No.: CINV" + datetime.now().strftime("%y%m%d\n"))
                invoice.write("Customer's Name: "+customerName)
                invoice.write("\nDate and Time: "+str(datetime.now().strftime("%Y-%m-%d, %H:%M:%S")))
                invoice.write("\n")
                invoice.write(f"\n{'Product':25}{'Brand':20}{'Quantity':15}{'Rate(Rs)':15}{'Price':15}\n")
                invoice.write("-"*90)
                for line in detail:
                    product,brand,quantity,rate,country = line.strip().split(", ")
                    for j in range(len(productName)):
                        if product == productName[j]:
                            rate = int(rate)
                            productPrice = rate*productQuantity[j]
                            invoice.write(f"\n {product:25}{brand:20}{totalQuantity[j]:<15}{rate:<15}{productPrice:<15}\n")

                invoice.write("-"*90)
                invoice.write(f"\n {'Total':75}{total}")
                
            #Writing to override products.txt for updating stocks
            with open("products.txt","w") as writer:
                for line in detail:
                    product,brand,quantity,rate,country = line.strip().split(", ")
                    for b in range(len(productQuantity)):
                        if product == productName[b]:
                            quantity=int(quantity)
                            quantity -= totalQuantity[b]
                            break

                    writer.write(f"{product}, {brand}, {quantity}, {rate}, {country}\n")
            break



#This function is for creating supplier invoice
def restockProduct():
    #This take input from user
    supplierName = input("Enter supplier name: ")
    productName = []
    productQuantity = []
    newRate = []
    totalCost = []

    i = 0
    while i>=0:
        productName.append(input("Enter product name: "))
        productQuantity.append(int( input("Enter the quantity of product: ")))
        newRate.append(int(input("Enter its price: ")))
        anotherProduct = input("Do you want to add another product (Yes/No): ")
        if anotherProduct.lower()=="yes":
            i+=1
            continue

        else:
            #Reading product text file for restocking product
            with open("products.txt","r") as file:
                detail =  file.readlines()

            print("Invoice No.: SINV"+datetime.now().strftime("%y%m%d"))
            print("supplier's name: "+supplierName)
            print("Date and Time: "+str(datetime.now().strftime("%Y-%m-%d, %H:%M:%S")))
            print(f"{'Product':25}{'Brand':20}{'Quantity':15}{'Previous rate(Rs)':25}{'New rate(Rs)':25}{'Price':15}")
            print("-"*125)
            for line in detail:
                product,brand,quantity,rate,country = line.strip().split(", ")
                for j in range(len(productName)):
                    if product == productName[j]:
                        price = productQuantity[j] * newRate[j]
                        totalCost.append(price)
                        print(f"{product:25}{brand:20}{productQuantity[j]:<15}{rate:<25}{newRate[j]:<25}{price:<15}")

            print("-"*125)
            total = 0
            for a in range(len(totalCost)):
                total = total + totalCost[a]
            print(f"{'Total':110}{total}")

            #Writing supplier invoice for selling product
            with open("supplierInvoice.txt","w") as invoice:
                invoice.write("Invoice No.: SINV"+datetime.now().strftime("%y%m%d\n"))
                invoice.write("supplier's Name: "+supplierName)
                invoice.write("\nDate and Time: "+str(datetime.now().strftime("%Y-%m-%d, %H:%M:%S")))
                invoice.write("\n")
                invoice.write(f"\n{'Product':25}{'Brand':20}{'Quantity':15}{'Previous rate(Rs)':25}{'New rate(Rs)':25}{'Price':15}\n")
                invoice.write("-"*125)
                for line in detail:
                    product,brand,quantity,rate,country = line.strip().split(", ")
                    for j in range(len(productName)):
                        if product == productName[j]:
                            price = productQuantity[j] * newRate[j]
                            invoice.write(f"\n{product:25}{brand:20}{productQuantity[j]:<15}{rate:<25}{newRate[j]:<25}{price:<15}\n")

                invoice.write("-"*125)
                invoice.write(f"\n {'Total':110}{total}")
                
            #Writing to override products.txt for updating stocks
            with open("products.txt","w") as writer:
              
                for line in detail:
                    product,brand,quantity,rate,country = line.strip().split(", ")
                    for b in range(len(productName)):
                        if product == productName[b]:
                            quantity=int(quantity)
                            quantity += productQuantity[b]
                            rate = newRate[b]
                            break
                        
                    writer.write(f"{product}, {brand}, {quantity}, {rate}, {country}\n")
                    

            break