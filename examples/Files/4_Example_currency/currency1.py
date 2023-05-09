import sys

currency = ["CZK", "EUR", "USD"]
amount = 79.9
exchangeRateFile = ["czk_eur.txt", "czk_usd.txt", "eur_usd.txt", "eur_czk.txt", "usd_czk.txt", "usd_eur.txt"]
textMessage = {
    "IOpen"      : "Opening exchange rate file {}...",
    "IOCreate"   : "Creating exchange rate file {}...",
    "IOClose"    : "Closing exchange rate file {}...",
    "IOErrOpen"  : "Can't open file {}!",
    "IOErrRead"  : "Can't read file {}!",
    "IOErrEmpty" : "Empty file {}!",
    "Curr"       : "Available currencies to convert:",
    "CurrToCurr" : "Conversion: {} -> {}",
    "CurrExRate" : "Current exchange rate {} -> {} is {}.",
    "ExRateValue": "Conversion {} {}: {} {}",
    "IOInput"    : "Input current"
}

def getfName(currA, currB):
    if (currA == currency[0] and currB == currency[1]): fName = exchangeRateFile[0]
    if (currA == currency[0] and currB == currency[2]): fName = exchangeRateFile[1]
    if (currA == currency[1] and currB == currency[2]): fName = exchangeRateFile[2]
    if (currA == currency[1] and currB == currency[0]): fName = exchangeRateFile[3]
    if (currA == currency[2] and currB == currency[0]): fName = exchangeRateFile[4]
    if (currA == currency[2] and currB == currency[1]): fName = exchangeRateFile[5]
    return fName

def showCurrencies():  
    print(textMessage["Curr"])
    for i in currency:
        print(currency.index(i), ". ", i)

def getExchangeRate (currA, currB):
    fName = getfName(currA, currB)
    print(textMessage["CurrToCurr"].format(currA, currB))
    print(textMessage["IOpen"].format(fName))
    try:
        foo = open(fName , 'rt', encoding="utf-8")
    except IOError as e:
        print(textMessage["IOErrOpen"].format(fName))
        return False
    except: #handle other exceptions such as attribute errors
        print(textMessage["IOErrOpen"].format(fName))        
        return False
    if foo:
        return foo.readline()
        foo.close()

def inputExchangeRate (currA, currB, exchangeRate):
    fName = getfName(currA, currB)
    print(textMessage["IOCreate"].format(fName))
    try:
        fow = open(fName , 'wt', encoding="utf-8")
    except IOError as e:
        print(textMessage["IOErrOpen"].format(fName))
    except: #handle other exceptions such as attribute errors
        print(textMessage["IOErrOpen"].format(fName))
    if fow:
        fow.writelines(str(exchangeRate))
        fow.close()

def calculateRate (rate, amount):
    return float(rate) * float(amount)

showCurrencies()

rate = False
while not rate:
    rate = getExchangeRate(currency[2], currency[0])
    if not rate:
        inputExchangeRate(currency[2], currency[0], 23.5)
print(textMessage["CurrExRate"].format(currency[2], currency[0], rate))
print(textMessage["ExRateValue"].format(amount, currency[2], calculateRate(rate, amount), currency[0]))

