let desiredIncome = document.querySelector('#desiredIncome')
let desiredUnit = document.querySelector('#desiredUnit')
let requiredIncome = document.querySelector('#requiredIncome')
let requiredUnit = document.querySelector('#requiredUnit')
let selfEmployed = document.querySelector('#selfEmployed')
const calculate = document.querySelector('#calculate')

// change this to whenver the state of any item is changed, the tax caclulator function is called
calculate.addEventListener('click', () => {
    console.log(desiredIncome.value)
    console.log(desiredUnit.value)
    console.log(requiredUnit.value)
    console.log(selfEmployed.checked)
})