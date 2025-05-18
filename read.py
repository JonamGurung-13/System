def loadData():
    with open("products.txt","r") as readFile:
        detail = readFile.readlines()

    product = []
    brand = []
    quantity = []
    rate = []
    country = []
    for line in detail:
        product.append(line.strip().split(", ")[0])
        brand.append(line.strip().split(", ")[1])
        quantity.append(int(line.strip().split(", ")[2]))
        rate.append(float(line.strip().split(", ")[3]))
        country.append(line.strip().split(", ")[4])
    return product,brand,quantity,rate,country
    
def returnProduct():
    product,_,_,_,_ = loadData()
    return product

def returnBrand():
    _,brand,_,_,_ = loadData()
    return brand

def returnQuantity():
    _,_,quantity,_,_ = loadData()
    return quantity

def returnRate():
    _,_,_,rate,_ = loadData()
    return rate

def returnCountry():
    _,_,_,_,country = loadData()
    return country

def customerIdCheck():
    with open("customerInvoiceId.txt","r") as invoiceId:
        invoice = invoiceId.readlines()
        if invoice == []:
            return "CINV1"
        else:
            i = 1
            while i>0:
                idName = "CINV"+str(i)
                a = 0
                for ids in invoice:
                    id = ids.strip()
                    if id == idName:
                        a+=1
                        break
                
                if a == 0:
                    return idName
                
                i+=1

def supplierIdCheck():
    with open("supplierInvoiceId.txt","r") as invoiceId:
        invoice = invoiceId.readlines()
        if invoice == []:
            return "SINV1"
        else:
            i = 1
            while i>0:
                idName = "SINV"+str(i)
                a = 0
                for ids in invoice:
                    id = ids.strip()
                    if id == idName:
                        a+=1
                        break
                
                if a == 0:
                    return idName
                
                i+=1
