# define tax information in one place
standard_deduction = 14600
brackets = [
    (0, 11600, 0.10),
    (11600, 47150, 0.12),
    (47150, 100525, 0.22),
    (100525, 191950, 0.24),
    (191950, 243725, 0.32),
    (243725, 609350, 0.35),
    (609350, float('inf'), 0.37)
]
ss = 0.124
medicare = 0.029
additonal_medicare_rate = 0.009
ss_wage_limit = 168600
medicare_threshold = 200000


# find federal income tax amount
def get_income_tax(gross_income):
    taxable_income = gross_income - standard_deduction
    tax = 0
    for lower, upper, rate in brackets:
        if taxable_income > lower:
            bracket_slice = min(upper, taxable_income) - \
                lower  # min handles full brackets
            tax += bracket_slice * rate
        else:
            break

    return tax


# find FICA tax amount
def get_fica_tax(income, self_employed=False):
    if self_employed:  # self employed persons pay full FICA tax
        ss_rate = ss
        medicare_rate = medicare
    else:  # half of FICA is paid  by employers for employed persons
        ss_rate = ss / 2
        medicare_rate = medicare / 2

    # min handles income over wage limit
    ss_tax = min(income, ss_wage_limit) * ss_rate
    medicare_tax = income * medicare_rate
    if income > medicare_threshold:  # additional medicare tax is applied to income over the threshold
        threshold_slice = income - medicare_threshold
        # all must pay full additional tax
        medicare_tax += threshold_slice * additonal_medicare_rate

    return ss_tax + medicare_tax


# find income after tax
def get_taxed_income(income, self_employed=False):
    income_tax = get_income_tax(income)
    fica_tax = get_fica_tax(income, self_employed)

    return income - income_tax - fica_tax


# find required income before tax for an inputted desired income
def find_required_income(desired_income, self_employed=False, tolerance=1):
    highest_rate = brackets[-1][-1]

    # using binary search to search through solutions to the after tax income
    low = desired_income
    high = desired_income / (1 - highest_rate)
    while (high - low) >= tolerance:  # finding exact match causes infinite loop, tolerance handles this
        mid = (high + low) / 2
        if get_taxed_income(mid, self_employed) > desired_income:
            high = mid
        else:
            low = mid
    return high
