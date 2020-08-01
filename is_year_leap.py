def is_year_leap(year):
    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        print("True")
    else:
        print("False")
year =int(input('please enter year  '))
is_year_leap(year)