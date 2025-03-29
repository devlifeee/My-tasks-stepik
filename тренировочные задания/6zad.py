def is_leap_year(year): 
# Год является високосным, если он делится на 4 без остатка   
# За исключением годов, которые делятся на 100 без остатка, но не делятся на 400 без остатка
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
leap_years_sum = 0
for year in range(0, 2024 + 1):   
    if is_leap_year(year):
        leap_years_sum += year
print(leap_years_sum)