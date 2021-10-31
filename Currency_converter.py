with open('currency_data.txt')as f:
    lines = f.readlines()


currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]

    
amount = int(input("Enter the amount : "))    
print("Enter the name of the currency you want to covert this amount to? Available options are -> ")
[print(item) for item in currencyDict.keys()]
currency = input("Please copy&past and enter one of this value : \n")
print(f"{amount} INR is equel to {amount *float(currencyDict[currency])} {currency}")
