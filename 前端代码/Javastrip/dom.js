// 查找标签

    // 直接查找
    var ele1 = document.getElementById('i1')  // ele1是一个dom对象
    console.log(ele1)

    var ele2 = document.getElementsByClassName('c1')  // 查找的dom数组
    console.log(ele2)

    var ele3 = document.getElementsByTagName('div')   //查找的是dom数组
    console.log(ele3)


    //导航查找
    var li_list = document.getElementsByTagName('li')
    console.log(li_list)

    console.log('第一个li标签的父亲标签是：',li_list[0].parentElement)
    console.log('第二个li标签的上兄弟标签是：',li_list[1].previousElementSibling)
    console.log('第二个li标签的下兄弟标签是：',li_list[1].nextElementSibling)


    //CSS选择器查找
    var cssselector = document.querySelector('.c2 .c3 .c4 li')  //只找到一个
    var cssselectors = document.querySelectorAll('.c2 .c3 .c4 li')  //找到所有
    console.log('查找到的首个li标签是：',cssselector)
    console.log('查找到的所有里标签为：',cssselectors)


// 绑定事件
    cssselector.onclick = function (){
        alert(123)
    }

// 操作标签

var ele =document.querySelector(".c10");

ele.onclick = function (){
    // 查看标签文本
    console.log('拿到标签内部的HTML',this.innerHTML)
    console.log('拿到标签内部的文本',this.innerText)
}

ele.ondblclick = function (){   // 双击事件
    // 设置标签文本
    this.innerHTML = "<a href='#'>yuan</a>"     // 赋值为HTML
    //this.innerText = "<a href='#'>yuan</a>"   //赋值为纯文本
}












