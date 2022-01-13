- let、const与var的区别

  ```
  var 最基础的变量声明
  
  ## 不污染全局变量、for循环函数的例子（var let返回的值不一样）
  let 不能被重复声明、块变量（一旦声明于大括号之内，就不能被外界读取引用）
  const 不能被重复生命，块变量、一旦声明变量，值无法进行修改，如果声明对象，对象本身不可修改，但是内部的值可以修改
  ```

- 模板字符串

  ```javascript
  // 占用字符，使用反引号``，内部用$(变量名)来实现引用效用
  const oBox = document.querySelector('.box');
  let id = 1,
      name = '小马哥';
  let htmlStr = `<ul>
              		<li>
                  		<p id=${id}>${name}</p>
              		</li>
          	   </ul>`;
          // oBox.innerHTML = "<ul><li><p id=" + id + ">" + name + "</p></li></ul>";   替代繁琐的字符串拼接问题
          oBox.innerHTML = htmlStr;
  ```

- 函数增强

  ```js
  // 一、形参可以使用值，或者调用函数，类似python语法
  // es5的写法
  function add(a, b) {
      a = a || 10;
      b = b || 20;
      return a + b;
  }
  console.log(add()); */
  
  //es6写法
  function add(a, b = 20) {
      return a + b;
  }
  console.log(add(30));
  
  // 2.默认的表达式也可以是一个函数
  function add(a, b = getVal(5)) {
      return a + b;
  }
  
  function getVal(val) {
      return val + 5;
  }
  console.log(add(10));
  
  
  
  // 二、...keys 类比python的*args
  function pick(obj, ...keys) {
      // ...keys 解决了arguments 的问题
      let result = Object.create(null);
      for (let i = 0; i < keys.length; i++) {
          result[keys[i]] = obj[keys[i]];
      }
      return result;
  }
  
  let book = {
      title: 'es6的教程',
      author: '周公瑾',
      year: 2019
  }
  let bookData = pick(book, 'year', 'author');
  console.log(bookData);
  
  function checkArgs(...args) {
      console.log(args);
      console.log(arguments);
  }
  checkArgs('a', 'b', 'c');
  
  
  
  // 三、...变量 类比python的reduce功能
  let arr = [1,2,3,4,6];
  // 数组拆分打印
  console.log(...arr);
  
  
  
  // 四、箭头函数 function(){} 可以替换为 ()=>{}
  // 注意事项
  // 1，箭头函数不存在this指向，一旦使用，this就会跳过函数往上作用域查找
  // 2，箭头函数内部没有arguments变量
  // 3，不能使用new方法来实例化对象
  let add = (m, n) => {return m + n};
  let add1 = (m, n) => m + n;
  let getObj = id => ({id:id,name:"周公瑾"});
  console.log(add(1,2), add1(1,2));
  ```

- 解构赋值

  ```js
  // es5
  let a = {
      'type': 'idea';
      'age': 15
  }
  let n1 = a.type;
  let n2 = a.age;
  
  // es6,使用{}对对象解构,必须对象属性名称
  let {type, age} = a;
  console.log(n1, n2, type, age)
  // 对数组解构
  let arr = [1,2,3];
  let [a,b] = arr;
  console.log(a,b);
  // 可嵌套
  let [a,[b],c] = [1,[2],3];
  ```

- 对象功能的扩展

  ```js
  // 简写功能
  const name = 'zhougongjin', age = 18;
  const person = {
      name: name,
      age: age,
      sayName: function(){
          console.log(`my name is ${name}, age is ${age}`)
      }
  }
  person.sayName();
  
  
  //上文对象可以简写为
  const name = 'zhougongjin', age = 18;
  const person = {
      name,
      age,
      sayName(){console.log(`my name is ${name}, age is ${age}`)}
  }
  person.sayName();
  
  // Object.is() 相当于 ===
  console.log(1===1, Object.is(1,1));
  
  // assign()对象的合并
  let newobj = Object.assign({}, {a:1}, {b:2});
  console.log(newobj)  // {a: 1, b: 2};
  ```

- 新数据类型Symbol，Set，Map

  ```js
  // Symbol，声明变量独一无二，通常用于定义私有变量
  const s1 = Symbol('name');
  let person = {
      [name]: '周公瑾',
  };
  
  
  //Set，集合，无重复有序列表
  const set = new Set()
  set.add(1) // 添加元素
  set.add([2,3])
  console.log(set)
  set.delete([2,3])   // 删除元素
  console.log(set)
  console.log(set.has('1')) // 检查是否包含元素 
  
  
  //Map类型是键值对的有序列表，键和值是任意类型
  let map = new Map();
  map.set('name','张三');
  map.set('age',20);	// 设值
  console.log(map.get('name'));
  console.log(map);
  map.has('name');   // true
  map.delete('name');  // 删除
  map.clear();   // 清空
  console.log(map);
  map.set(['a',[1,2,3]],'hello');
  console.log(map); 
  
  
  ```

- 数组的扩展用法

  ```js
  // 1.from() 将伪数组转换成真正的数组
  function add() {
      // console.log(arguments);
      // es5转换
      // let arr = [].slice.call(arguments);
      // console.log(arr);
      // es6写法
      let arr = Array.from(arguments);  // 将arguments伪数组转化为真正的数组
      console.log(arr);
  }
  add(1, 2, 3);
  
   let lis = document.querySelectorAll('li')
   console.log(Array.of(3, 11, 20, [1, 2, 3], {id: 1}));
  
  
   // 2.of() 将任意的数据类型，转换成数组
  console.log(Array.of(3, 11, 20, [1, 2, 3], {
      id: 1
  }));
  
  
  // 3.copywithin() 数组内部将制定位置的元素复制到其它的位置，返回当前数组
  // 从3位置往后的所有数值，替换从0位置往后的三个数值
  console.log([1, 2, 3, 8, 9, 10].copyWithin(0, 3));
  //[8,9,10,8,9,10]
  
  
  //  4.find() findIndex()
  // find()找出第一个符合条件的数组成员
  let num = [1, 2, -10, -20, 9, 2].find(n => n < 0)
  // console.log(num);
  
  // findIndex()找出第一个符合条件的数组成员的索引
  let numIndex = [1, 2, -10, -20, 9, 2].findIndex(n => n < 0)
  // console.log(numIndex);
  
  
  // 5.entries() keys() values() 返回一个遍历器  可以使用for...of循环进行遍历，参考python 字典的keys,values,items     
  // keys() 对键名遍历
  // values() 对值遍历
  // entries() 对键值对遍历
  // console.log(['a','b'].keys());
  
  for (let index of ['a', 'b'].keys()) {
      console.log(index);
  }
  
  for (let ele of ['a', 'b'].values()) {
      console.log(ele);
  }
  
  for(let [index,ele] of ['a','b'].entries()){
      console.log(index,ele); 
  }
  
  
  // 6.includes() 返回一个布尔值，表示某个数组是否包含给定的值
  console.log([1,2,3].includes(2));
  console.log([1,2,3].includes('4'));
  ```

- 迭代器 & 生成器（可以实现异步编程）

  ```js
  // Iterator迭代器
  // 是一种新的遍历机制，两个核心
  // 1.迭代器是一个接口，能快捷的访问数据，通过Symbol.iterator来创建迭代器 通过迭代器的next()获取迭代之后的结果
  // 2.迭代器是用于遍历数据结构的指针(数据库的游标)
  
  // 使用迭代
  const items = ['one', 'two', 'three'];
  // 1.创建新的迭代器
  const ite = items[Symbol.iterator]();
  console.log(ite.next()); //{value: "one", done: false} done如果为false表示遍历继续 如果为true表示遍历完成
  console.log(ite.next());
  console.log(ite.next());
  console.log(ite.next()); //{value: undefined, done: true}
  
  
  // generator函数 可以通过yield关键字，将函数挂起，为了改变执行流提供了可能，同时为了做异步编程提供了方案
  // 它普通函数的区别
  // 1.function后面 函数名之前有个*
  // 2.只能在函数内部使用yield表达式，让函数挂起
  function* add() {
      console.log('start');
      // x 可真的不是yield '2'的返回值，它是next()调用 恢复当前yield()执行传入的实参
      let x = yield '2';  //并非将2赋值给x，而是在下次yield被执行的时候传入的参数来赋值
      console.log('one:'+x);
      let y = yield '3';
      console.log('two:'+y);
      return x+y;  
  }
  const fn = add();
  console.log(fn.next()); //{value:'2',done:false}
  console.log(fn.next(20)); //{value:'3',done:false}
  console.log(fn.next(30)); //{value:50,done:true}
  ```

- Promise对象（可以实现异步编程）

  ```js
  // Promise 承诺
  // 相当于一个容器，保存着未来才会结束的事件(异步操作)的一个结果
  // 各种异步操作都可以用同样的方法进行处理 axios
  
  // 特点：
  // 1.对象的状态不受外界影响  处理异步操作 三个状态  Pending(进行)  Resolved(成功) Rejected(失败)
  // 2.一旦状态改变，就不会再变，任何时候都可以得到这个结果
  function timeOut(data, ms) {
      return new Promise((resolved, rejected) => {
          setTimeout(()=>{
              if(Object.is(data, 1)) {
                  resolved('返回成功的消息...')
              }else {
                  rejected('返回失败的消息...')
              }
          }, ms)
      })
  }
  timeOut(2, 1000).then((val)=>{
      console.log(val)
  })
  
  
  // catch方法
  const getJSON = function (url) {
      return new Promise((resolve, reject) => {
          const xhr = new XMLHttpRequest();
          xhr.open('GET', url);
          xhr.onreadystatechange = handler;
          xhr.responseType = 'json';
          xhr.setRequestHeader('Accept', 'application/json');
          // 发送
          xhr.send();
  
          function handler() {
              if (this.readyState === 4) {
                  if (this.status === 200) {
                      resolve(this.response.HeWeather6);
                  } else {
                      reject(new Error(this.statusText));
                  }
              }
          }
      })
  }
  getJSON('https://free-ap.heweather.net/s6/weather/now?location=beijing&key=4693ff5ea653469f8bb0c29638035976')
      .then(data => {
      console.log(data);   // 成功状态捕获
  }).catch(err => {
      console.log(err);	// 失败状态捕获
  }).finally(
  	console.log('执行完成');   // 不管成功失败，都执行此方法
  )
  
  
  // 事务（同时成功，同时失败）--伪代码
  let promise1 = new Promise((resolve, reject) => {});
  let promise2 = new Promise((resolve, reject) => {});
  let promise3 = new Promise((resolve, reject) => {});
  let p4 = Promise.all([promise1, promise2, promise3])
  p4.then(()=>{
      // 三个都成功  才成功
  }).catch(err=>{
      // 如果有一个失败 则失败
  })
  
  
  
  // race方法，为某个异步请求设置超时时间，并且在超时后执行相应的操作 --伪代码
  Promise.race([requestImg('https://timgsa.baidu.com/'),timeout()]).then(data=>{
      console.log(data);
  }).catch(err=>{
      console.log(err);
  });
  ```

- async方法（可以实现异步编程）

  ```js
  async function getNowWeather(url) {
      // 发送ajax 获取实况天气
      let res = await getJSON(url);
      console.log(res);
      // 获取HeWeather6的数据   获取未来3~7天的天气状况
      let arr = await res.HeWeather6;
      return arr[0].now;
  }
  getNowWeather('https://free-api.heweather.net/s6/weather/now?location=beijing&key=4693ff5ea653469f8bb0c29638035976')
      .then(now => {console.log(now);})
  ```

- class对象

  ```js
  class Person {
      // constructor关键字，实例化的时候会立即被调用
      constructor(name, age) {
          this.name = name;
          this.age = age;
      }   // 注意此处没有逗号
   	sayHello() {
          return 'hello world'
      },
  }
  // 通过Object.assign()方法一次性向类中添加多个方法
  Object.assign(Person.prototype, {
      sayName() {
          return this.name
      },
      sayAge() {
          return this.age
      }
  })
  let p1 = new Person('小马哥', 28);
  console.log(p1);
  
  
  
  
  // 类的继承
  // 使用关键字 extends
  class Animal{
      constructor(name,age) {
          this.name = name;
          this.age = age;
      }
      sayName(){
          return this.name;
      }
      sayAge(){
          return this.age;
      }
  }
  
  class Dog extends Animal{
      constructor(name,age,color) {
          super(name,age);
          // Animal.call(this,name,age);
          this.color = color;
      }
      // 子类自己的方法
      sayColor(){
          return `${this.name}是${this.age}岁了,它的颜色是${this.color}`
      }
      // 重写父类的方法，supers
      sayName(){
          return this.name + super.sayAge() + this.color;
      }
  }
  let d1 = new Dog('小黄',28,'red');
  console.log(d1.sayColor());
  console.log(d1.sayName());
  
  
  ```

  







