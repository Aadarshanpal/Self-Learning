from num_to_day import converter

date = input("Enter the full date in the format YYYY/MM/DD: ")

q = int((date[-2]+date[-1]))

m = int((date[5]+date[6]))

k = int((date[2]+date[3]))

j = int((date[0]+date[1]))

if m == 1 or m == 2:
    if m == 1:
        m = 13
    elif m == 2:
        m = 14
    year = f"{int(date[:4]) - 1:04d}"
    j = int(year[:2])
    k = int(year[2:])

h = (q + ((13*(m+1))//5) + k + k//4 + j//4 + 5*j) % 7

print(f"The day was: {converter(h)}")