import csv

def getSymbols():
    stocksArr = []
    elementArr = []
    with open("stocks.csv", "r") as stocks:
        # lines = stocks.readline()
        # headers = lines.split(",")

        csvreader = csv.reader(stocks)
        for row in csvreader:
            values = row
            elementArr.append(values)
    
        for element in elementArr:
            if(element[0] == "Symbol"):
                continue
            stocksArr.append(element[0])
        
    return stocksArr

# def main():
#     symbols = getSymbols()
#     symbolCount = 0
    
#     for symbol in symbols:
#         symbolCount += 1
#         print(symbol)

#     print(symbolCount)
# main()