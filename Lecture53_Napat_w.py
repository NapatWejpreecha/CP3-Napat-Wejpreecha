def vatCalculate(totalPrice = float(input("Enter total price : "))):
    result = str((totalPrice*7/100)+totalPrice)
    return result + " THB"
print(vatCalculate())