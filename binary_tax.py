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

standard_deduction = 14600

ss = 0.124
medicare = 0.029
self_employed = False
if self_employed:
    fica = ss + medicare
else:
    fica = (ss + medicare)/2

ss_wage_limit = 168600
medicare_threshold = 200000
