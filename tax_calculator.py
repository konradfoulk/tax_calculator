def income(self_employed, desired_income):
    if self_employed:
        if desired_income <= 8907.97:
            return desired_income/(1 - 0.1 - 0.153)
        elif 8907.98 <= desired_income <= 35479.09:
            x = (desired_income - 8907.97)/(1 - 0.12 - 0.153)
            return 11926 + x
        elif 35479.1 <= desired_income <= 69885.09:
            x = (desired_income - 35479.09)/(1 - 0.22 - 0.153)
            return 48476 + x
        elif 69885.1 <= desired_income <= 126912.13:
            x = (desired_income - 69885.09)/(1 - 0.24 - 0.153)
            return 103351 + x
        elif 126912.14 <= desired_income <= 154961.18:
            x = (desired_income - 126912.13)/(1 - 0.32 - 0.153)
            return 197301 + x
        elif 154961.19 <= desired_income <= 341745.71:
            x = (desired_income - 154961.18)/(1 - 0.35 - 0.153)
            return 250526 + x
        elif 341745.72 <= desired_income:
            x = (desired_income - 341745.71)/(1 - 0.37 - 0.153)
            return 626351 + x
    elif not self_employed:
        if desired_income <= 9820.23:
            return desired_income/(1 - 0.1 - 0.0765)
        elif 9820.24 <= desired_income <= 39187.35:
            x = (desired_income - 9820.23)/(1 - 0.12 - 0.0765)
            return 11926 + x
        elif 39187.36 <= desired_income <= 77791.21:
            x = (desired_income - 39187.35)/(1 - 0.22 - 0.0765)
            return 48476 + x
        elif 77791.22 <= desired_income <= 142005.35:
            x = (desired_income - 77791.21)/(1 - 0.24 - 0.0765)
            return 103351 + x
        elif 142005.36 <= desired_income <= 174126.04:
            x = (desired_income - 142005.35)/(1 - 0.32 - 0.0765)
            return 197301 + x
        elif 174126.05 <= desired_income <= 389661.1:
            x = (desired_income - 174126.05)/(1 - 0.35 - 0.0765)
            return 250526 + x
        elif 389661.11 <= desired_income:
            x = (desired_income - 389661.1)/(1 - 0.37 - 0.0765)
            return 626351 + x
