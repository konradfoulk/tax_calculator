const standardDeduciton = 14600
const brackets = [
    (0, 11600, 0.10),
    (11600, 47150, 0.12),
    (47150, 100525, 0.22),
    (100525, 191950, 0.24),
    (191950, 243725, 0.32),
    (243725, 609350, 0.35),
    (609350, Infinity, 0.37)
]
const ss = 0.124
const medicare = 0.029
const additionalMedicareRate = 0.009
const ssWageLimit = 168600
const medicareThreshold = 200000

function getIncomeTax(grossIncome) {
    const taxableIncome = grossIncome - standardDeduciton
    let tax = 0

    for (let [lower, upper, rate] in brackets) {
        if (taxableIncome > lower) {
            let bracketSlice = Math.min(upper, taxableIncome) - lower
            tax += bracketSlice * rate
        } else {
            break
        }
    }

    return tax
}

function getFicaTax(income, selfEmployed) {
    let ssRate
    let medicareRate
    if (selfEmployed) {
        ssRate = ss
        medicareRate = medicare
    } else {
        ssRate = ss / 2
        medicareRate = medicare / 2
    }

    let ssTax = Math.min(income, ssWageLimit) * ssRate
    let medicareTax = income * medicareRate
    if (income > medicareThreshold) {
        let thresholdSlice = income - medicareThreshold
        medicareTax += thresholdSlice * additionalMedicareRate
    }

    return ssTax + medicareTax
}

export function findTaxedIncome(income, selfEmployed) {
    let incomeTax = getIncomeTax(income)
    let ficaTax = getFicaTax(income, selfEmployed)

    return income - incomeTax - ficaTax
}

export function findRequiredIncome(desiredIncome, selfEmployed, tolerance = 0.001) {
    const highestRate = brackets[-1][-1]

    let low = desiredIncome
    let high = desiredIncome / (1 - highestRate)
    while ((high - low) >= tolerance) {
        let mid = (high + low) / 2
        if (getTaxedIncome(mid, selfEmployed) > desiredIncome) {
            high = mid
        } else {
            low = mid
        }
    }
    return high
}