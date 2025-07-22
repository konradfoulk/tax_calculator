self_employed = False

brackets = [
    (0, 11600, 0.10),
    (11600, 47150, 0.12),
    (47150, 100525, 0.22),
    (100525, 191950, 0.24),
    (191950, 243725, 0.32),
    (243725, 609350, 0.35),
    (609350, float('inf'), 0.37)
]

if self_employed:
    ss_rate = 0.124
    medicare_rate = 0.029
else:
    ss_rate = 0.062
    medicare_rate = 0.0145

standard_deduction = 14600


def get_income_tax(taxable_income):
    tax = 0
    for lower, upper, rate in brackets:
        if taxable_income > lower:
            bracket_slice = min(upper, taxable_income) - lower
            tax += bracket_slice * rate
        else:
            break

    return tax


def get_fica_tax(income):
    ss_tax = min(income, 168600) * ss_rate
    medicare_tax = income * medicare_rate
    if income > 200000:
        threshold_slice = income - 200000
        medicare_tax += threshold_slice * 0.009

    return ss_tax + medicare_tax


gross_income = 250000
taxable_income = gross_income - standard_deduction

income_tax = get_income_tax(taxable_income)
fica_tax = get_fica_tax(gross_income)
after_tax_income = gross_income - income_tax - fica_tax

print(gross_income)
print(income_tax)
print(fica_tax)
print(after_tax_income)
