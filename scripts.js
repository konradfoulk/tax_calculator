import { findTaxedIncome, findRequiredIncome } from './calculators.js'

let afterTaxCalc = document.querySelector('#afterTaxCalc')
let reqCalc = document.querySelector('#reqCalc')

let selfEmployed = document.querySelector('#selfEmployed')

let income = document.querySelector('#income')
let incomeUnit = document.querySelector('#incomeUnit')
let afterTaxUnit = document.querySelector('#afterTaxUnit')

let desiredIncome = document.querySelector('#desiredIncome')
let desiredUnit = document.querySelector('#desiredUnit')
let requiredUnit = document.querySelector('#requiredUnit')

function calculateAfterTax() {
    let afterTax = findTaxedIncome((income.value * incomeUnit.value), selfEmployed.checked)
    let incomeRound = Math.round(afterTax / afterTaxUnit.value * 100) / 100
    document.querySelector('#incomeAfterTax').textContent = incomeRound
}

function calculateRequired() {
    let requiredIncome = findRequiredIncome((desiredIncome.value * desiredUnit.value), selfEmployed.checked)
    let requiredRound = Math.round(requiredIncome / requiredUnit.value * 100) / 100
    document.querySelector('#requiredIncome').textContent = requiredRound
}

income.addEventListener('input', calculateAfterTax)
incomeUnit.addEventListener('change', calculateAfterTax)
afterTaxUnit.addEventListener('change', calculateAfterTax)

desiredIncome.addEventListener('input', calculateRequired)
desiredUnit.addEventListener('change', calculateRequired)
requiredUnit.addEventListener('change', calculateRequired)

selfEmployed.addEventListener('change', () => {
    calculateAfterTax()
    calculateRequired()
})

document.querySelector('#afterTaxBtn').addEventListener('click', () => {
    afterTaxCalc.style.display = 'block'
    reqCalc.style.display = 'none'
})
document.querySelector('#reqBtn').addEventListener('click', () => {
    reqCalc.style.display = 'block'
    afterTaxCalc.style.display = 'none'
})