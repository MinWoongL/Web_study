// set initial count
let count = 0

const value = document.querySelector('#value')
const btns = document.querySelectorAll('.btn')

// console.log(btns)
btns.forEach(function (btn) {
    // console.log(item)
    btn.addEventListener("click", function (e) {
        const styles = e.currentTarget.classList
        if(styles.contains('decrease')){
            count -= 1
        }
        else if(styles.contains('increase')){
            count += 1
        }
        else{
            count = 0
        }
        if(count > 0){
            value.style.color = "blue"
        }
        if(count < 0){
            value.style.color = "violet"
        }
        if(count === 0){
            value.style.color = "#222"
        }
        value.textContent = count
    })
})