tax_per_year = float(input())

shoes = tax_per_year - (40/100) * tax_per_year
equipment = shoes - (20/100) * shoes
ball = equipment / 4
accessories =  ball / 5

all_tax = tax_per_year + shoes + equipment + ball + accessories

print(f'{all_tax:.2f}')