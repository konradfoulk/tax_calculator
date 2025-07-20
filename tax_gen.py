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

ss = 0.124
medicare = 0.029

selfemployed = False
fica_total = ss + medicare
if selfemployed:
    fica = fica_total
else:
    fica = fica_total / 2

ss_wage_limit = 168600
medicare_wage_threshold = 200000

b1_after_tax = b1.max * (1 - b1.rate - fica)
b2_after_tax = b1_after_tax + (b2.max - b1.max) * (1 - b2.rate - fica)
b3_after_tax = b2_after_tax + (b3.max - b2.max) * (1 - b3.rate - fica)
b4_after_tax_1 = b3_after_tax + (ss_wage_limit - b3.max) * (1 - b4.rate - fica)

if selfemployed:
    fica = medicare
else:
    fica = medicare / 2

b4_after_tax_2 = b4_after_tax_1 + \
    (b4.max - ss_wage_limit) * (1 - b4.rate - fica)
b5_after_tax_1 = b4_after_tax_2 + \
    (medicare_wage_threshold - b4.max) * (1 - b5.rate - fica)

fica += 0.009

b5_after_tax_2 = b5_after_tax_1 + \
    (b5.max - medicare_wage_threshold) * (1 - b5.rate - fica)
b6_after_tax = b5_after_tax_2 + (b6.max - b5.max) * (1 - b6.rate - fica)

print(b1_after_tax)
print(b2_after_tax)
print(b3_after_tax)
print(b4_after_tax_1)
print(b4_after_tax_2)
print(b5_after_tax_1)
print(b5_after_tax_2)
print(b6_after_tax)

# desired_income = 1
# standard_deduction = 14600
# taxable_income = desired_income-standard_deduction
