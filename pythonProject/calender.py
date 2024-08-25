year=int(input("Enter the year you want check leap year or not?="))

if(year%4==0):


    if(year%400==0):
        print("Year inputed is leap year!")

    elif(year%4==0):
        print("Year inputed is leap year!")

    else:
        print("Year inputed is not leap year!")

else:
    if (year % 100 == 0):
        print("Year inputed is not leap year!")

    else:
        print("Year inputed is leap year!")