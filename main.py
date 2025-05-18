from operation import viewStock,sellProduct,restockProduct

optionLoop = 0
while optionLoop==0:
    print("╔"+"═"*40+"╗")
    print(f"║{'WeCare Beauty & Skincare Store'.center(40)}║")
    print("╠"+"═"*40+"╣")
    print(f"║{'1. View Stocks':40}║")
    print(f"║{'2. Sell Products':40}║")
    print(f"║{'3. Restock Products':40}║")
    print(f"║{'4. Exit':40}║")
    print("╚"+"═"*40+"╝")
    try:
        option = int(input("Enter an option: "))
    except:
        print("Invalid input!!!\n"
              "Please put proper input\n")
        continue

    if option==1:
        print()
        viewStock()
    
    elif option==2:
        print()
        sellProduct()
    
    elif option==3:
        print()
        restockProduct()
    
    elif option==4:
        break

    else:
        print("Invalid Input!!!")
        print("Please choose from the option")

    print()
