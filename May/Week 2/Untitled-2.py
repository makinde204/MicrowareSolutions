def isValidDate(year,month,date):
    if year <= 2024:
        if month<=12:
            if  date<= 31:
                print("True")
    else:
        
        print("False")

isValidDate(2004,12,24)