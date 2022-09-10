from email import charset


def isBookValid():
    string = ""
    isbn = "9780316066525"
    isbn13 = isValidISBN13(isbn)
    if(type(isbn13) == list):
        for i in isbn13:
            string += i
        print("\nISBN"+"("+isbn+"): ",string,"\n")
    else:
        print("\nISBN"+"("+isbn+"):",isbn13,"\n")


def isValidISBN10(isbn):
    total = 0
    for i in range(9):
        if 0 <= int(isbn[i]) <= 9:
            total += int(isbn[i]) * (10 - i)
    total += 10 if isbn[9] == 'X' else int(isbn[9])
    if(len(isbn)< 10 or total%11 !=0):
        return False    
    elif(total%11 == 0):
        return True

def convert10_digit_to_13_digit(isbn):
    threeDigitsList = ["9","7","8"]
    isbnList = list(isbn)
    threeDigitsList.extend(isbnList)
    checkNum = int(threeDigitsList[12]) + 1
    charac = str(checkNum)
    threeDigitsList[12] = charac
    return threeDigitsList

def isValidISBN13(isbn):
    message = ""
    total = 0
    numList = ['1','3','1','3','1','3','1','3','1','3','1','3','1']
    newList = []
    if (len(isbn) == 10):
        if(isValidISBN10(isbn) == True):
            newList = convert10_digit_to_13_digit(isbn)
            return newList
        else:
            message = "invalid"
            return message
    else:
        newList = list(isbn)
        for i in range(len(numList)):
            for j in newList[i]:
                total +=  int(numList[i]) * int(j)
        if(total%10 == 0 and len(isbn) == 10):
            message = "valid"
            return newList
        else:
            message ="valid"
            return message
        

isBookValid()  
        