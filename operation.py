from datetime import datetime
from write import customerInvoice,supplierInvoice,stockUpdateCustomer,stockUpdateSupplier,stockUpdateNew
from read import returnBrand,returnCountry,returnProduct,returnQuantity,returnRate,customerIdCheck,supplierIdCheck

#This is for viewing the stock of products available in the store
def viewStock():
    print("┌"+"─"*36+"┬"+"─"*26+"┬"+"─"*21+"┬"+"─"*21+"┬"+"─"*21+"┐")
    print(f"│ {'Product':35}│ {'Brand':25}│ {'Quantity':20}│ {'Rate(Rs)':20}│ {'Country':20}│") #Headings
    print("├"+"─"*36+"┼"+"─"*26+"┼"+"─"*21+"┼"+"─"*21+"┼"+"─"*21+"┤")
    for i in range(len(returnProduct())):
        product = returnProduct()[i]
        brand = returnBrand()[i]
        quantity = returnQuantity()[i]
        rate = returnRate()[i]*3
        country = returnCountry()[i]
        print(f"│ {product:35}│ {brand:25}│ {quantity:<20}│ {rate:<20}│ {country:20}│")
    print("└"+"─"*36+"┴"+"─"*26+"┴"+"─"*21+"┴"+"─"*21+"┴"+"─"*21+"┘")


#This is for selling the products
def sellProduct():
    totalPrice = 0.00
    generateInvoice = False
    exit = False
    customerNameValid = False
    while not exit:
        while not customerNameValid:
            customerName = (input("Enter the customer's name: ")).strip() #Take customer name as an input
            if not customerName.replace(" ","").isalpha():
                print("Invalid Customer's Name!!!\n")
            else:
                customerNameValid = True

        choosenProduct = {}
        addProduct = []
        while customerNameValid:
            productName = (input("Enter product name: ")).strip()
            productNameValidation = False
            brandName = ""
            productRate = 0.00
            refusedProduct = False
            exception = True
            for i in range(len(returnProduct())):
                product = returnProduct()[i]
                brandName = returnBrand()[i]
                quantity = returnQuantity()[i]
                productRate = returnRate()[i]*3
                if productName.lower() == product.lower():
                    productNameValidation = True
                    productName=product
                    break

            if not productNameValidation:
                print("Product not available!!!!\n")
                anotherProduct = input("Do you want to buy another product(Yes/No): ")
                if anotherProduct.lower() == "yes":
                    print()
                    continue

                else:
                    exit = True
                    break
            if productName in addProduct:
                quantity -= (choosenProduct[productName]["quantity"] + choosenProduct[productName]["free"])

            if quantity==0:
                print("Product Out of Stock")
                anotherProduct = input("Do you want to buy another product(Yes/No): ")
                if anotherProduct=="yes":
                    continue

                else:
                    if addProduct!=[]:
                        generateInvoice = True
                    exit = True
                    break
                    
            while exception:
                try:
                    productQuantity = int(input("Enter the product quantity: "))
                    if productQuantity<0:
                        print("Invalid Quantity, Please put proper value")
                    else:
                        exception = False
                except:
                    print("Please give proper input\n")
            free = 0
            if productQuantity >3:
                free += int(productQuantity/3)

            if quantity<(productQuantity+free):
                if quantity%4 == 3:
                    availableQuantity = int(quantity/4)*3
                else:
                    availableQuantity = int(quantity/4)*3 + quantity%4
                print("Insufficient Quantity!!!")
                print(f"Available Quantity for purchase {availableQuantity}")
                anotherProduct = input("Do you want to buy this product within the available quantity(Yes/No): ")
                if anotherProduct.strip()=="yes":
                    i = 0
                    while i ==0:
                        while not exception:
                            try:
                                productQuantity = int(input("Enter the product quantity: "))
                                if productQuantity<0:
                                    print("Invalid Quantity, Please put proper value")
                                else:
                                    exception = True
                            except:
                                print("Please give proper input\n")
                        free = 0
                        if productQuantity >3:
                            free += int(productQuantity/3)

                        if availableQuantity >= productQuantity:
                            break

                else:
                    refusedProduct = True

            if not refusedProduct:
                price = productQuantity*productRate
                totalPrice += price
                if productName in addProduct:
                    choosenProduct[productName]["quantity"] +=productQuantity
                    choosenProduct[productName]["free"]+=free
                    choosenProduct[productName]["price"]+=price
        
                
                else:
                    choosenProduct[productName] = {"brand":brandName, "quantity":productQuantity, "free":free, "rate":productRate, "price":price}
                    addProduct.append(productName)
        
            anotherProduct = input("Do you want to buy another product(Yes/No): ")
            generateInvoice = True
            if anotherProduct.strip().lower() == "yes":
                print()
                continue

            else:
                break

        if generateInvoice:
            #Displays invoice in terminal
            print("\n"+"WeCare - Beauty & Skincare Store".center(140))
            print("Customer Invoice".center(140))
            print("-"*140)
            print("Customer Invoice ID: "+customerIdCheck())
            print("Customer's Name: "+customerName)
            print("Date: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
            print("-"*140)
            print(f"{'Product':30}{'Brand':25}{'Quantity':20}{'Free':20}{'Rate':20}{'Price':20}")
            print("-"*140)
            for name,value in choosenProduct.items():
                print(f'{name:30}{value["brand"]:25}{value["quantity"]:<20}{value["free"]:<20}{value["rate"]:<20}{value["price"]:<20}')
            print("-"*140)
            print(f"{'':95}{'Total:':20}{totalPrice:<20}")
            print("-"*140)
            print("Thank You for Buying from WeCare".center(140))
            print("Stay Beautiful & Healthy !!!".center(140))
            

            #Creates a .txt file for customer invoice
            customerInvoice(customerName,choosenProduct,totalPrice)

            
            #Updates the stock of products
            for name,value in choosenProduct.items():
                totalQuantity = value["quantity"] + value["free"]
                stockUpdateCustomer(name,totalQuantity)
            
            exit = True
            

#This is for restocking the products
def restockProduct():
    price = 0.00
    totalPrice = 0.00
    generateInvoice = False
    restockProduct = {}
    newStockProduct = {}
    exit = False
    supplierNameValid = False
    while not exit:
        while not supplierNameValid:
            supplierName = (input("Enter the supplier's name: ")).strip() #Take supplier name as an input
            if not supplierName.replace(" ","").isalpha():
                print("Invalid Supplier's Name!!!\n")

            else:
                supplierNameValid = True

        addProduct = []
        while supplierNameValid:
            exception = True
            previousRate = 0.00
            newProduct = False
            productName = (input("Enter the product name: ")).strip()

            for i in range(len(returnProduct())):
                product = returnProduct()[i]

                if productName.lower() == product.lower():
                    previousRate = returnRate()[i]
                    newProduct = False
                    break
                else:
                    newProduct = True
                
            if not newProduct:
                if productName in addProduct:
                    while exception:
                        try:
                            productQuantity = int(input("Enter the product quantity: "))
                            if productQuantity<0:
                                print("Invalid Quantity, please put proper input\n")
                            else:
                                exception = False
                        except:
                            print("Please give proper input\n")
                    price = restockProduct[productName]["newRate"]*productQuantity
                    restockProduct[productName]["quantity"]+=productQuantity
                    restockProduct[productName]["price"]+=price
                    
                else:
                    while exception:
                        try:
                            productQuantity = int(input("Enter the product quantity: "))
                            if productQuantity<0:
                                print("Invalid Quantity, please put proper value\n")
                            else:
                                exception = False
                        except:
                            print("Please give proper input\n")

                    while not exception:
                        try:
                            productRate = float(input(f"Enter the price (previous price:{previousRate}): "))
                            if productRate<0:
                                print("Invalid Price, please put proper value\n")
                            else:
                                exception = True
                        except:
                            print("Please give proper input\n")

                    price = productRate*productQuantity
                    restockProduct[productName] = {"quantity":productQuantity, "previousRate":previousRate, "newRate":productRate, "price":price}
                    addProduct.append(productName)
                totalPrice +=price

            else:
                if productName in addProduct:
                    while exception:
                        try:
                            productQuantity = int(input("Enter the product quantity: "))
                            if productQuantity<0:
                                print("Invalid Quantity, Please put proper value\n")
                            else:
                                exception = False
                        except:
                            print("Please give proper input\n")
                    price = restockProduct[productName]["newRate"]*productQuantity
                    restockProduct[productName]["quantity"]+=productQuantity
                    restockProduct[productName]["price"]+=price

                else:
                    productBrand = (input("Enter the brand of the product: ")).strip()
                    while exception:
                        try:
                            productQuantity = int(input("Enter the product quantity: "))
                            if productQuantity<0:
                                print("Invalid Quantity, Please put proper value\n")
                            else:
                                exception = False
                        except:
                            print("Please give proper input\n")

                    while not exception:
                            try:
                                productRate = float(input("Enter the price: "))
                                if productRate<0:
                                    print("Invalid price, Please put proper value\n")
                                else:
                                    exception = True
                            except:
                                print("Please give proper input\n")
                    productCountry = (input("Enter the product's country of origin: ")).strip()
                    price = productRate*productQuantity
                    restockProduct[productName] = {"quantity":productQuantity,"previousRate":previousRate, "newRate":productRate, "price":price}
                    newStockProduct[productName] = {"brand":productBrand, "quantity":productQuantity, "rate":productRate, "country":productCountry}
                    addProduct.append(productName)
                totalPrice +=price

            anotherProduct = input("Do you want to restock another product(Yes/No): ")
            generateInvoice = True
            if anotherProduct.strip().lower() == "yes":
                print()
                continue

            else:
                break

        #Invoice generator
        if generateInvoice: #Display supplier invoice in terminal
            print("\n"+"WeCare - Beauty & Skincare Store".center(140))
            print("Supplier Invoice".center(140))
            print(" "+"-"*140)
            print("\nSupplier Invoice ID: "+supplierIdCheck())
            print("Supplier's Name: "+supplierName)
            print("Date: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
            print(" "+"-"*140)
            print(f"{'Product':30}{'Quantity':25}{'Previous Rate':25}{'New Rate':25}{'Price':30}")
            print("-"*140)
            for name,value in restockProduct.items():
                print(f'{name:30}{value["quantity"]:<25}{value["previousRate"]:<25}{value["newRate"]:<25}{value["price"]:<30}')
            print("-"*140)
            print(f"{'':80}{'Total:':25}{totalPrice:<30}")
            print("-"*140)
            print("Thank You for Supplying to WeCare".center(140))


            #Creating .txt file for supplier invoice
            supplierInvoice(supplierName,restockProduct,totalPrice)


            #Updating the stocks
            for name,value in restockProduct.items():
                stockUpdateSupplier(name,value["quantity"],value["newRate"])

            for name,value in newStockProduct.items():
                stockUpdateNew(name,value["brand"],str(value["quantity"]),str(value["rate"]),value["country"])
            
            exit = True                     