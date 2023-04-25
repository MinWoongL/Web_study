const menus = ['치킨', '피자']

// 재료 준비
const preCooking = function(item) {
    return new Promise((resolve, reject) => {
        console.log(`${item} 재료준비`)
        // 1초 후에 재료 준비가 완료되면 약속
        setTimeout(() => {
            resolve()
        }, 1000)
    })
    // console.log('재료 준비')
}

// Promise 객체를 반환하도록 수정
// cooking 함수에서 호출

// 실제 요리: 3초
const realCooking = function(item) {
    return new Promise((resolve, reject) => {
        console.log(`${item} 요리 중`)
        // 3초 후에 요리가 완료되면
        setTimeout(() => {
            resolve()
        }, 3000)
    })
    // console.log('요리 중')
}

// 요리 후 청소: 2초
const afterCooking = function(item) {
    return new Promise((resolve, reject) => {
        console.log(`${item} 요리 완료! 청소 작업`)
        // 2초 후
        setTimeout(() => {
            resolve()
        }, 2000)
    })
    // console.log('요리 완료! 청소 작업')
}


// 식당에서 전달받은 메뉴를 요리하는 함수
const cooking = function(item, callback) {
    // promise Chaining
    preCooking(item).then(() => {
        console.log(`${item} 재료 준비 완료`)
        // 그냥 Promise 객체를 반환하는 함수
        // Promise 객체의 반환을 기다리도록 return을 설정
        // 함수실행완료를 기다리도록 return을 설정
        return realCooking(item)
    })
    .then(() => {
        console.log(`${item} 요리 완료`)
        return afterCooking(item)
    })
    .then(() => {
        console.log(`${item} 청소 완료`)
        callback()
    })
    .catch((error) => {
        console.log(error)
    })



    // preCooking(item).then(() => {
    //     console.log('재료 준비 완료')

    //     realCooking(item).then(() => {
    //         console.log('요리 완료')

    //         afterCooking(item).then(() => {
    //             console.log(`${item} 청소 완료`)
    //             callback()
    //         })
    //     })
    // }).catch((error) => {
    //     console.log(error)
    // })


    // // 재료 준비
    // preCooking()
    // // 1초 후
    // setTimeout(() => {
    //     // 요리 중
    //     realCooking()
    //     // 3초 후
    //     setTimeout(() => {
    //         // 청소
    //         afterCooking()
    //         // 2초 후
    //         setTimeout(() => {
    //              // 아래 코드 실행
    //             console.log('30분 경과')
    //             console.log(`${item} 조리 완료!`)
    //             callback()
    //         }, 2000)
    //     }, 3000)
    // }, 1000)
}



// 1. 앱으로 치킨 주문
const orderDelivery = function(item) {
    
    console.log(`${item} 주문 시도`)

    if (!menus.includes(item)) {
        console.log(`${item} 은 없는 메뉴입니다`)
        return
    }

    order(item, function(){
        console.log(`${item} 배달 완료`)
    })
    
}

// 2. 앱 -> 식당으로 메뉴 전달
const order = function(item, callback) {
    
    console.log(`${item} 식당에서 메뉴 전달 받음!`)
    cooking(item, function() {
        console.log(`조리 완료! 배달 시작!`)
    })

    // 특정 함수가 정상 실행 되었을 때 다른 함수 호출
    // 하는 방식으로 실행관리 효율적으로 가능
    callback()

}

orderDelivery('치킨')
console.log('---------')
orderDelivery('피자')
console.log('---------')
orderDelivery('짜장면')