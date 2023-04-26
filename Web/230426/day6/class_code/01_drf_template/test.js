

const getEventAdd = function() {
    const getBtn = document.querySelector('#get-btn')
    var done = false
    getBtn.addEventListener('click', (event) => {
        // BackendURL 구성
        const backendURL = 'http://127.0.0.1:8000/api/v1/articles/'
        const ulTag = document.querySelector('ul')
        axios({
            method: 'GET',
            url: backendURL,
            // POST 요청시 data에 담아서
            data: {
                'title': '제목',
                'content': '내용'
            },
            // GET 요청시에 params에 담아서 전달 받을 수 있음
            // params 는 url 뒤쪽에 queryString 형식으로 데이터를 담아서 전달
            // params: {
            //     'contest': '내용'

            // }
        }).then((response) => {
            // console.log('response = ', response)
            if (done == true) {
                console.log('중복요청')
                return
            }
            else {
                const datas = response.data
                datas.forEach(element => {
                    const container = document.createElement('div')
                    const title = document.createElement('li')
                    title.innerText = `${element.id}: ${element.title}`

                    const del_button = document.createElement('button')
                    del_button.classList.add('btn','btn-secondary')
                    del_button.textContent = '삭제'

                    container.appendChild(title)
                    container.appendChild(del_button)
                    ulTag.appendChild(container)

                    del_button.addEventListener('click', (event) => {
                        console.log('>>>>>>>>>>>>')
                        console.log(title)

                        title.remove()
                        del_button.remove()
                    })
                    
                });
                done = true
            }
            
        }).catch((error) => {
            console.log('error = ', error)
        })
    })
}

