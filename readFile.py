def stockProduct():
    file = open('products.txt','r')
    detail = file.readlines()
    print(f"{'Product':25}{'Brand':20}{'Quantity':15}{'Price':15}{'Country':15}")
    print("-"*90)

    for line in detail:
        product,brand,quantity,price,country = line.strip().split(", ")
        print(f"{product:25}{brand:20}{quantity:15}{price:15}{country:15}")
    file.close()