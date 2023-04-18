let a

// console.log(a)
// console.log(typeof(a))

// 1. null 과 undefined
// let a = '서버로부터 데이터를 받아오는 코드'
// 결과가 undefined 라면
// 서버로부터 데이터를 못 받아온 것
// a 라는 변수

console.log(a)              // undefined
console.log(a == null)      // true
console.log(a == undefined) //  true
console.log(a === null)     //  false
console.log(a == undefined) //  true



// 2. 문자열 형변환
let str = "test"
// new: 새로운
let str2 = new String("test")

console.log(typeof(str))    // string
console.log(typeof(str2))   // object

// 객체처럼 쓴다? -> 내장 메서드를 활용 가능
// "text"는 원시값인데, toUpperCase 라는 메서드 어떻게 가질가?
// JS 는 내부적으로 원시타입에 대해 내장 객체를 가지고 있다
//      -> 원시 타입 사용 시 내장 객체로 해석

console.log("test".toUpperCase())

console.log(`1 = ${str == str2}`)
console.log(`2 = ${str === str2}`)
// 객체끼리의 비교: 주소값이 다르므로 false
console.log(`3 = ${str == new String("test")}`)
console.log(`4 = ${str === new String("test")}`)


// 문자열끼리 + 연산자: 문자열을 붙이는 연산자
console.log('1' + '2')  // 12
console.log(1 + 2)      // 3
console.log(1 + '2')    // 12 -> 정수는 문자열로 암시적 형변환 되어 적용

// 문자열 -> 숫자로 형변환됨
// 문자열끼리 써도
console.log('5'-'1')        // 4
console.log('5'-'1'+'3')    // 43
console.log('2' + '3'*4)    // 212

console.log('10'*3 + '10'/2)    // 35

let strr = "hello"
let bool = true

console.log(strr + bool) // 문자열로 형변환 되어 계산
console.log(str - bool)  // NaN (Not-a-Number)
console.log(str * bool)

// true: 1, false: 0 으로 형변환하여 계산
console.log(3 + Number(true))   // 4
console.log(3 + false)          // 3

// 블록스코프
{
    let a = 20
    console.log(a) // 20
    // 전역에서 이미 a를 선언했지만, 블록스코프 내부라서 다시 재선언하여 사용 가능
}

const fruits = {
    a: 'apple',
    b: 'banana'
}

// 반복문에서 여러개의 블록스코프를 사용하는 것으로 판단되어
// const 변수도 계속 바뀌며 사용이 가능하다.
for (const key in fruits){
    const tmp_key = key
    console.log(tmp_key)
}


let x = 20
function myFunction() {
    // myFunction 의 함수 스코프
    // innerFunction 의 렉시컬 스코프
    let num = 10
    console.log(num)

    function innerFunction() {
        console.log(x)
    }

    innerFunction()
}
// 밖으로 나오게 되면, 렉시컬 스코프는 전역 스코프만 가능
// function innerFunction() {
//     console.log(x)
// }

// innerFunction()
myFunction()

function myFunction2(x) {
    function add(y){
        console.log(x+y)
    }
    return add
}

// x에 해당하는 값은 고정시켜두고, y에 해당하는 값만 바꾸면서 쓰고 싶을 때 사용하는 기법 Closure
let func = myFunction2(10)
func(20)

// 배열, 객체
// 얕은복사와 깊은복사

// 원시타입 빼고는 다 얕은 복사
// 1. 함수에서 사용 시
// function func(arr){
//     arr[0] = 10
// }

// let arr = [1, 2, 3]
// func(arr)

// 2. 변수로 복사할 때
let numbers = [1, 2, 3]
let newnumbers = numbers
newnumbers[0] = 10
console.log(numbers)        // [10, 2, 3]
console.log(newnumbers)     // [10, 2, 3]

// 간단한 깊은 복사
let numbers2 = [1, 2, 3]
let newnumbers2 = [...numbers2]


// 자바스크립트는 함수 파라미터 개수를 따로 체크하지 않는다.
// 개발자가 주의해서 사용
function mF(x, y){
    console.log(x+y)
    // arguments: 함수에 전달 된 argument 들을 가지고 있음
    // 전달된 데이터 정보 확인 시 유용하게 활용가능
    // 특히, js 파일이 여러 개일 때, 디버깅 시 유용하게 활용 가능
    console.log(arguments)
}
mF(10, 20)          
mF(10, 20, 30, 40)  // 버그안남
mF(10)              // 버그안남