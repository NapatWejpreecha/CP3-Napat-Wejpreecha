Username = input("Enter Username : ")
Password = input("Enter Password : ")
if Username=="LungTaewBan" and Password=="7777" :
    print("Welcome")
    print("------LungShop------")
    print("Shop's Product")
    print("1. iPhone       (31,900 THB)")
    print("2. iPad         (27,900 THB)")
    print("3. Airpods      (6,900 THB)")
    print("4. Apple Pencil (4,490 THB)")
    print("*price doesn't include vat*")
    userSelected = int(input("Choose your option >> "))
    if userSelected == 1:
        price = 31900
        vat = 7
        result = price + (price*vat/100)
        print("iPhone :" ,result, "THB")
    elif userSelected == 2:
        price = 27900
        vat = 7
        result = price + (price*vat/100)
        print("iPad :",result, "THB")
    elif userSelected == 3:
        price = 6900
        vat = 7
        result = price + (price*vat/100)
        print("Airpods :",result, "THB")
    elif userSelected == 4:
        price = 4490
        vat = 7
        result = price + (price*vat/100)
        print("Apple Pencil :" ,result, "THB")
    print("Thank you")
    print("-----------------")
else:
    print("Please Try Again")
