// exports 객체에 add와 multiply 를 추가
// 덧셈
exports.add = function(a, b){
    return a+b
}

// 곱셈
exports.multiply = function(a, b){
    return a*b
}

//math 모듈 내에서만 사용하는 함수
const mySub = function(a, b){
    return a + 10
}

// sub는 a에 10을 더해주고, b 를 뺀 결과를 반환하는 함수
// exports.sub = function(a, b){
//     return mySub(a) - b
// }

const innerSub = function(a, b){
    return mySub(a) - b
}

exports.sub = innerSub

console.log(this.sub(3, 5))
console.log(this)

// console.log(innerSub(3, 5))