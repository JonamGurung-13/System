from datetime import datetime
from pathlib import Path
from read import customerIdCheck,supplierIdCheck

def customerInvoice(customerName,soldProduct,totalPrice):
    i = 1
    while i>0:
         fileName = "customerInvoice_"+str(i)+".txt"
         file = Path(fileName)
         if not file.exists():
              break
         i+=1
    with open(fileName,"w") as writeFile:
        writeFile.write(f"{'WeCare - Beauty & Skincare Store':>87}\n")
        writeFile.write(f"{'Customer Invoice':>78}\n")
        writeFile.write("-"*140)
        writeFile.write("\nCustomer Invoice ID: "+customerIdCheck()+"\n")
        writeFile.write("Customer's Name: "+customerName)
        writeFile.write("\nDate: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        writeFile.write("-"*140)
        writeFile.write(f"\n{'Product':30}{'Brand':25}{'Quantity':20}{'Free':20}{'Rate':20}{'Price':20}\n")
        writeFile.write("-"*140)
        for name,value in soldProduct.items():
            writeFile.write(f'\n{name:30}{value["brand"]:25}{value["quantity"]:<20}{value["free"]:<20}{value["rate"]:<20}{value["price"]:<20}')
        writeFile.write("\n"+"-"*140)
        writeFile.write(f"\n{'':95}{'Total:':20}{totalPrice:<20}\n")
        writeFile.write("-"*140)
        writeFile.write(f"\n{'Thank You for Buying from WeCare':>86}")
        writeFile.write(f"\n{'Stay Beautiful & Healthy !!!':>84}")
    
    with open("customerInvoiceId.txt","a") as writeInvoice:
         writeInvoice.write(customerIdCheck()+"\n")


def supplierInvoice(supplierName,restockProduct,totalPrice):
    i = 1
    while i>0:
         fileName = "supplierInvoice_"+str(i)+".txt"
         file = Path(fileName)
         if not file.exists():
              break
         i+=1
    with open(fileName,"w") as writeFile:
        writeFile.write(f"{'WeCare - Beauty & Skincare Store':>87}\n")
        writeFile.write(f"{'Supplier Invoice':>78}\n")
        writeFile.write("-"*140)
        writeFile.write("\nSupplier Invoice ID: "+supplierIdCheck()+"\n")
        writeFile.write("Supplier's Name: "+supplierName+"\n")
        writeFile.write("Date: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        writeFile.write("-"*140)
        writeFile.write(f"\n{'Product':30}{'Quantity':25}{'Previous Rate':25}{'New Rate':25}{'Price':30}\n")
        writeFile.write("-"*140)
        for name,value in restockProduct.items():
            writeFile.write(f'\n{name:30}{value["quantity"]:<25}{value["previousRate"]:<25}{value["newRate"]:<25}{value["price"]:<30}\n')
        writeFile.write("-"*140)
        writeFile.write(f"\n{'':80}{'Total:':25}{totalPrice:<30}\n")
        writeFile.write("-"*140)
        writeFile.write(f"\n{'Thank You for Supplying to WeCare':>86}")

    with open("supplierInvoiceId.txt","a") as writeInvoice:
        writeInvoice.write(supplierIdCheck()+"\n")


def stockUpdateCustomer(name,quantity):
    with open("products.txt","r") as readFile:
        detail = readFile.readlines()

    with open("products.txt","w") as writeFile:
        for line in detail:
            product,brand,previousQuantity,rate,country = line.strip().split(", ")
            if name.lower() in line.lower():
                currentQuantity = str(int(previousQuantity)-quantity)
                writeFile.write(product+", "+brand+", "+currentQuantity+", "+rate+", "+country+"\n")
            
            else:
                writeFile.write(product+", "+brand+", "+previousQuantity+", "+rate+", "+country+"\n")


def stockUpdateSupplier(name,quantity,rate):
    with open("products.txt","r") as readFile:
        detail = readFile.readlines()

    with open("products.txt","w") as writeFile:
        for line in detail:
            product,brand,previousQuantity,previousRate,country = line.strip().split(", ")
            if name.lower() in line.lower():
                currentQuantity = str(int(previousQuantity)+quantity)
                currentRate = str(rate)
                writeFile.write(product+", "+brand+", "+currentQuantity+", "+currentRate+", "+country+"\n")
            
            else:
                writeFile.write(product+", "+brand+", "+previousQuantity+", "+previousRate+", "+country+"\n")


def stockUpdateNew(name,brand,quantity,rate,country):
    with open("products.txt","a") as writeFile:
        writeFile.write(name+", "+brand+", "+quantity+", "+rate+", "+country+"\n")              