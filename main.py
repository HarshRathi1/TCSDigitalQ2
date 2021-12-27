year=int(input())
def day(year):
    if year in range(1700,1918):
        if year%4==0:
            print("12.09."+str(year))
        else:
            print("13.09."+str(year))
    elif year==1918:
        print("26.09."+str(year))
    elif year in range(1919,2701):
        if year%400==0 or (year%4==0 and year%100!=0):
            print("12.09."+str(year))
        else:
            print("13.09."+str(year))
day(year)