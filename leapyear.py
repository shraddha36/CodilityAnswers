def leapYear(year):
    if ((year%4)==0 & (year % 100!= 0)) | ((year%100==0)&(year%400 == 0)):
        return("{} yes its an leap year".format(year))
    return("Nope")
print(leapYear(1700))
