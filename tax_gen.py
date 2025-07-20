class TaxBracket:
    def __init__(self, max, rate):
        self.max = max
        self.rate = rate


b1 = TaxBracket(11600, 0.1)
b2 = TaxBracket(47150, 0.12)
b3 = TaxBracket(100525, 0.22)
b4 = TaxBracket(191950, 0.24)
b5 = TaxBracket(243725, 0.32)
b6 = TaxBracket(609350, 0.35)

brackets = [b1, b2, b3, b4, b5, b6]

previous_amount = 0
previous_max = 0
brackets_after_tax = []
for bracket in brackets:
    amount = previous_amount + \
        (bracket.max - previous_max) * (1 - bracket.rate)

    brackets_after_tax.append(amount)

    previous_amount = amount
    previous_max = bracket.max

for i in brackets_after_tax:
    print(i)

# don't ignore ^

# desired_income = 1
# standard_deduction = 14600
# taxable_income = desired_income-standard_deduction

# ss = 0.124
# medicare = 0.029

# selfemployed = False
# fica_total = ss + medicare
# if selfemployed:
#     fica = fica_total
# else:
#     fica = fica_total / 2

# ss_wage_limit = 168600
# medicare_wage_threshold = 200000

# ignore ^
