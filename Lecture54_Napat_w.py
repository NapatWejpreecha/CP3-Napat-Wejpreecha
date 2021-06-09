def login():
    Username = input("Enter Username : ")
    Password = input("Enter Password : ")
    if Username == "admin" and Password == "test1234":
        return showMenu()
    else:
        print("Try again")
        return login()

def showMenu():
    print("-----LungTuuShop-----")
    print("1.Vat Calculator")
    print("2.Price Calaculator")
    return menuSelect()

def menuSelect():
    userSelected = int(input("Choose your option >> "))
    if userSelected == 1:
        return vatCalculate()
    elif userSelected == 2:
        return priceCalculate()
    else:
        print("Please Select Our options")
        return showMenu()

def vatCalculate():
    totalPrice = int(input("Enter total price : "))
    vat = 7
    result = str(totalPrice*vat/100)
    print(result + " THB")

def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    result = str((price1+price2) + ((price1+price2)*7/100))
    print(result + " THB")

login()
