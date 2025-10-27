def calculate_fine(days):
    if days<=5:
        return days*2
    elif days<=10:
        return(5*2)+(days-5)*3
    else:
        return(5*2)+(5*3)+(days-10)*5
print(calculate_fine(12))
