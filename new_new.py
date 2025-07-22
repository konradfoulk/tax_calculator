brackets = [
    (0, 11600, 0.10),
    (11600, 47150, 0.12),
    (47150, 100525, 0.22),
    (100525, 191950, 0.24),
    (191950, 243725, 0.32),
    (243725, 609350, 0.35),
    (609350, float('inf'), 0.37)
]


def get_income_tax(gross_income):
    standard_deduction = 14600

    taxable_income = gross_income - standard_deduction
    tax = 0
    for lower, upper, rate in brackets:
        if taxable_income > lower:
            bracket_slice = min(upper, taxable_income) - lower
            tax += bracket_slice * rate
        else:
            break

    return tax


def get_fica_tax(income, self_employed):
    if self_employed:
        ss_rate = 0.124
        medicare_rate = 0.029
    else:
        ss_rate = 0.062
        medicare_rate = 0.0145

    ss_tax = min(income, 168600) * ss_rate
    medicare_tax = income * medicare_rate
    if income > 200000:
        threshold_slice = income - 200000
        medicare_tax += threshold_slice * 0.009

    return ss_tax + medicare_tax


def get_after_tax_income(income):
    income_tax = get_income_tax(income)
    fica_tax = get_fica_tax(income, False)

    return income - income_tax - fica_tax


def find_after_tax_income(desired_income, tolerance=1):
    low = desired_income
    high = desired_income / (1 - brackets[-1][-1])
    while (high - low) > tolerance:
        mid = (low + high) / 2
        mid_after_tax = get_after_tax_income(mid)
        if mid_after_tax < desired_income:
            low = mid
        else:
            high = mid
    return high


required_income = find_after_tax_income(600000)
print(required_income)
after_tax_income = get_after_tax_income(required_income)
print(after_tax_income)
