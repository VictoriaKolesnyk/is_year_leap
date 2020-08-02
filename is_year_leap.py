def is_year_leap(year):
    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        return print("True")
    else:
        return print("False")
year =int(input('please enter year  '))
is_year_leap(year)
