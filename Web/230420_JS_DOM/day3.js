console.log(document.querySelectorAll('body > ul > li'))

// create_append
const title = document.createElement('h1')
title.innerText = 'DOM 조작'
const div = document.querySelector('div')
div.appendChild(title)


// appendchild
const fruitsList = document.querySelector('#fruits')
const banana = document.querySelector('#banana')
fruitsList.appendChild(banana)