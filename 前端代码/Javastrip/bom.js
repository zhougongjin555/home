// //打印window对象
// console.log(window)
//
// //window 下面的三个弹窗方法
// window.alert('牛皮啊')
//
// msg = window.confirm("请问打开新的窗口？")  // 返回布尔值
// console.log('选择是',msg)
//
// num = window.prompt('请输入一个数字')   // 返回输入值
// console.log('输入的数字是：',num)
//
// if(msg) {
//     // window.open('http://www.baidu.com','_blank','width=800px,height=500px,left=100px,top=100px');
//     window.open("http://www.baidu.com","_blank","width=800px,height=500px,left=200px,top=200px");
// }
//
// window.close() // 关闭窗口



// // 定时方法
// var id = setInterval(function(){
//     console.log('ok')
//     },1000)  //循环定时，时间单位毫秒
// window.clearInterval(id)
//
//
// var id2 = setTimeout(function(){
//     console.log('一次')
// },1000)  //单次定时，时间单位毫秒
// window.clearTimeout(id2)


// location地址栏对象
console.log('location对象是：',location)
console.log('url完整信息是：',location.href)
console.log('域名端口：'.location.host)
console.log('参数',location.search)

















