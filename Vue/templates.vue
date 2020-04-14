<script src="https://unpkg.com/vue"></script>

<!------ for loop + checkbox ------->

<div id='example-1'>
  <div v-for="name in names">
    <input type="checkbox" :id="name.id" :value="name.name" v-model="checkedNames">
    <label :for="name.id">{{ name.name }}</label>
  </div>
  <br>
  <span>Checked Names: </span><span v-for="name in checkedNames">{{ name }} √ </span>
</div>


<script type="text/javascript">
new Vue({
  el: '#example-1',
  data: {
    checkedNames: [],
    names: [
      {id:1, name: "Apple"},
      {id:2, name: "Banana"},
      {id:3, name: "Peach"}
    ]
  }
})
</script>

<!------ true/false checkbox ------->

<div id="p">
  <input
    type="checkbox"
    v-model="checked"
    true-value="ap"
    false-value="no"
    id="1"
  >
  <label for="1">{{checked}}</label>
</div>

<script type="text/javascript">
new Vue({
  el: '#p',
  data: {
    checked: false
  }
})
</script>

<!------ todo-list example ------->

<div id="todo-list-example">
  <form v-on:submit.prevent="addNewTodo">
    <label for="new-todo">Add a todo</label>
    <input
      v-model="newTodoText"
      id="new-todo"
      placeholder="E.g. Feed the cat"
    >
    <button>Add</button>
  </form>
  <ul>
    <li
      is="todo-item"
      v-for="(todo, index) in todos"
      v-bind:key="todo.id"
      v-bind:title="todo.title"
      v-on:remove="todos.splice(index, 1)"
    ></li>
  </ul>
</div>

Vue.component('todo-item', {
  template: '\
    <li>\
      {{ title }}\
      <button v-on:click="$emit(\'remove\')">Remove</button>\
    </li>\
  ',
  props: ['title']
})

<script type="text/javascript">
new Vue({
  el: '#todo-list-example',
  data: {
    newTodoText: '',
    todos: [
      {
        id: 1,
        title: 'Do the dishes',
      },
      {
        id: 2,
        title: 'Take out the trash',
      },
      {
        id: 3,
        title: 'Mow the lawn'
      }
    ],
    nextTodoId: 4
  },
  methods: {
    addNewTodo: function () {
      this.todos.push({
        id: this.nextTodoId++,
        title: this.newTodoText
      })
      this.newTodoText = ''
    }
  }
})
</script>



<!------ blog post demo ------->

<div id="blog-post-demo">
  <div>initial post font size: {{fontSize}}</div>
  <div>
    <blog-post
      v-for="post in posts"
      :key="post.id"
      :post="post"
      v-on:enlarge-text="post.postFontSize += $event"    
    ></blog-post>
  </div>
</div>

<script type="text/javascript">
Vue.component('blog-post', {
  props: ['post'],
  template: `
    <div class="blog-post">
      <h3>{{ post.title }}</h3>
      <div :style="{ fontSize: post.postFontSize + 'px' }">{{post.content}}</div>
      <span>postFontSize: {{post.postFontSize}}</span>
      <button v-on:click="$emit('enlarge-text', 1)">
        Enlarge text
      </button>
    </div>
  `
})
var fontSize = 15
new Vue({
  el: '#blog-post-demo',
  data: {
  	fontSize : fontSize,
    posts: [
      { id: 1, title: 'My journey with Vue', content: 'Content 1 is here', postFontSize: fontSize },
      { id: 2, title: 'Blogging with Vue', content: 'Content 2 is here', postFontSize: 15 },
      { id: 3, title: 'Why Vue is so fun', content: 'Content 3 is here', postFontSize: 15 }
    ]
  }
})
</script>

