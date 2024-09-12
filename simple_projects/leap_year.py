y = input("Enter any year=")
leap_year1 = str(y)[0:2]
leap_year2 = str(y)[2:]
le_ap = str(y)[:1]
if len(str(y)) == 4:
     if int(leap_year1) % 4 == 0:
         if int(leap_year2) % 4 == 0:
             print(y+" is a leap year!")
         else:
             print(y+" is not a leap year!")
     else:
         if int(leap_year2) == 0:
             print(y+" is not a leap year!")
         elif int(leap_year2)%4 == 0:
             print(y+" is a leap year!")
         else:
             print(y+" is not a leap year!")

elif len(str(y)) == 3:
    if int(le_ap) % 4 == 0:
        print(y+" is a leap year!")
    else:
        print(y+" is not a leap year!")
else:
    print(y + " is not a leap year!")
