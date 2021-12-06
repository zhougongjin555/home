### 基础语法

- 创建对象

```js
// 创建一个vue对象
const vu = new Vue({
    el: "#app",    // 指定元素
    data:{   	// 创建数据
        ...
    },
    methods:{     	// p函数
        ...
    },
    watch:{		  // 变量对象监视
        ...
    },
    computed:{	   // 计算属性
        ...
    },
    filters:{	   // 过滤器属性
        ...
    },
  	components:{	   // 用来挂载组件
        ...
    },     
})
```

- 新增标签方法

  - v-text  &  v-html                      使用属性的方法给标签插值
  - v-show  &  v-id、v-else          用于展示或者隐藏标签
  - v-bind  可以简写成为:             给标签绑定属性值
  - v-on     可以简写成为@           给标签绑定事件
  - v-for                                        循环遍历
  - v-model                                  通常结合input等标签，双向保存输入值
  

### VUE组件



