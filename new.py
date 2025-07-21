# for single filers using the standard deduction
def get_income_after_tax(income, self_employed):
    income_tax = 0
    fica_tax = 0

    standard_deduction = 14600
    taxable_income = income - standard_deduction

    if self_employed:
        ss = 0.124
        medicare = 0.029
    else:
        ss = 0.062
        medicare = 0.0145

    # calculate income tax
    if taxable_income > 0:
        if taxable_income > 609350:
            income_tax += 11600 * 0.1
            income_tax += (47150 - 11600) * 0.12
            income_tax += (100525 - 47150) * 0.22
            income_tax += (191950 - 100525) * 0.24
            income_tax += (243725 - 191950) * 0.32
            income_tax += (609350 - 243725) * 0.35
            income_tax += (taxable_income - 609350) * 0.37
        elif taxable_income > 243725:
            income_tax += 11600 * 0.1
            income_tax += (47150 - 11600) * 0.12
            income_tax += (100525 - 47150) * 0.22
            income_tax += (191950 - 100525) * 0.24
            income_tax += (243725 - 191950) * 0.32
            income_tax += (taxable_income - 243725) * 0.35
        elif taxable_income > 191950:
            income_tax += 11600 * 0.1
            income_tax += (47150 - 11600) * 0.12
            income_tax += (100525 - 47150) * 0.22
            income_tax += (191950 - 100525) * 0.24
            income_tax += (taxable_income - 191950) * 0.32
        elif taxable_income > 100525:
            income_tax += 11600 * 0.1
            income_tax += (47150 - 11600) * 0.12
            income_tax += (100525 - 47150) * 0.22
            income_tax += (taxable_income - 100525) * 0.24
        elif taxable_income > 47150:
            income_tax += 11600 * 0.1
            income_tax += (47150 - 11600) * 0.12
            income_tax += (taxable_income - 47150) * 0.22
        elif taxable_income > 11600:
            income_tax += 11600 * 0.1
            income_tax += (taxable_income - 11600) * 0.12
        elif taxable_income > 0:
            income_tax += taxable_income * 0.1

    # calculate FICA tax
    if income > 200000:
        fica_tax += 168600 * ss
        fica_tax += 200000 * medicare
        fica_tax += (income - 200000) * (medicare + 0.009)
    elif income > 168600:
        fica_tax += 168600 * ss
        fica_tax += income * medicare
    elif income > 0:
        fica_tax = income * (ss + medicare)

    print(income_tax)
    print(fica_tax)
    print(income - income_tax - fica_tax)


get_income_after_tax(250000, False)
