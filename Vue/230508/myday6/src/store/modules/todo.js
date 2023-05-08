// 모듈을 default 로 export 하겠다.
export default {
    state: {
        todoList: [
			// 개별 todo Object
      {
        id: 1638771553377,                // nowDateObj.getTime()
        content: 'Vue',                   // Todo 내용
        dueDateTime: '2021-12-09T00:00',  // 마감일
        isCompleted: false,               // 완료된 할 일
        isImportant: true,				        // 중요 할 일
      },
      {
        id: 1638771553378,
        content: 'Vue Router',
        dueDateTime: '2021-12-10T00:00',
        isCompleted: false,
        isImportant: true,
      },
      {
        id: 16387715533779,
        content: 'Vuex',
        dueDateTime: '2021-12-11T00:00',
        isCompleted: true,
        isImportant: false,
      },
    ],
    },
    mutations: {
        CREATE_TODO(state, todoItem) {
            state.todoList.push(todoItem)
        },
        LOAD_TODOS(state) {
            // 로컬스토리지로부터 데이터를 받아와
            // state에 저장
            const localStorageTodos = localStorage.getItem('todoList')
            if (localStorage.getItem('todoList')) {
                // 문자열 -> 객체형태로 변환해서 저장
                state.todoList = JSON.parse(localStorageTodos)
            }
            // const parsedTodos = JSON.parse(localStorageTodos)

            // state.todoList = parsedTodos
        },
        DELETE_TODO(state, todoItem) {
            const index = state.todoList.indexOf(todoItem)
            state.todoList.splice(index, 1)
        }
    },
    actions: {
        createTodo(context, todoTitle){
            // python 과 다르게 음수인덱스 접근이 불가능 -> 길이 -1 로 구현해야함
            const lastItem = context.state.todoList[context.state.todoList.length-1]
            const newId = lastItem.id + 1
            // store에 저장 전 동기적인 로직
            // "년-월-일T시:분" 형태

            const today = new Date()
            const year = today.getFullYear();
            const month = ('0' + (today.getMonth() + 1)).slice(-2);
            // 마감일은 현재로부터 10일 후
            const day = ('0' + (today.getDate() + 10)).slice(-2);

            const dateString = year + '-' + month  + '-' + day;

            const hours = ('0' + today.getHours()).slice(-2); 
            const minutes = ('0' + today.getMinutes()).slice(-2);

            const timeString = hours + ':' + minutes;

            const dueDate = dateString + 'T' + timeString
            const todoItem = {
                id: newId,
                content: todoTitle,
                isCompleted: false,     // 완료된 할 일
                isImportant: false,      // 중요 할 일
                dueDateTime: dueDate
            }
            context.commit('CREATE_TODO', todoItem)
            context.dispatch('saveTodoListToLocalStorage')
        },
        saveTodoListToLocalStorage(context) {
            // 로컬스토리지는 문자열 밖에 인식 못함
            // JSON.stringify => 문자열로 반환
            const jsonTodos = JSON.stringify(context.state.todoList)
            // 로컬스토리지에 저장
            localStorage.setItem('todoList', jsonTodos)
        },
        loadTodoList(context) {
            context.commit('LOAD_TODOS')
        },
        deleteTodo(context, todoItem){
            context.commit('DELETE_TODO', todoItem)
            context.dispatch('saveTodoListToLocalStorage')
        }
    }
}