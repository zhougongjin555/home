// 变量先声明在赋值
var x;
x = 10;
console.log(x)


// 直接声明并赋值
var y=10;


// 声明多个变量
var a=1,b=2;


// 全局变量
c = 3


// 数据类型
    // number 数字类型
    var x1=1,x2=3.14
    console.log('x1的数据类型',typeof x1)
    console.log('x2的数据类型',typeof x2)

    // 字符串类型
    var s1='hello world'
    console.log(s1, typeof s1)
    console.log('s1的长度为：',s1.length)
    console.log('s1转换为大写：',s1.toUpperCase)
    console.log('s1转换为小写：',s1.toLowerCase)
    console.log('s1中l(first)的位置索引：',s1.indexOf('l'))
    console.log('s1[1]位置的字符为',s1[1])
    console.log('s1[1:4]切片:',s1.slice(1,4))
    console.log('s1从第一个字符往后切三个字符：',s1.substr(1,3))


    var res='周-公-瑾'
    console.log('res正则切分为：', res.split('-'))

    var s2='   周  公  瑾     '
    console.log('s2移除前后的空白后的样子：',s2.trim())


    //boolean 布尔值
    var b1=true,b2=false;
    console.log('b1, b2的数据类型',typeof b1,typeof b2)


    //类型之间的强制转换
        //字符串转化为数字
        var box1='一共100次';
        var box2='100次';
        var ret1=parseInt(box1),ret2=parseInt(box2);
        console.log('box1,box2转换为数字为：',ret1,ret2)

        var box3 = "3.14";
        console.log(parseFloat(box2) ); // 3.14

        var box4 = "3.1.4";
        console.log(parseFloat(box4) ); // 3.1
        console.log(Number(box4) ); // NaN

        //数字转化为字符串
        var num1=100;
        console.log(num1.toString())
        console.log(String(num1))


//运算符号
var c1=10;
var c2=c1++
console.log('c1++是先赋值在计算',c2)  //10
console.log('此时c1为',c1)
var c3=++c1
console.log('++c1是先计算在赋值',c3)  //12
console.log('此时c1为',c1)

    //'=='弱相等
    console.log(1=='1') //true
    //'==='强相等
    console.log(1==='1') //false

//三元运算，条件运算符
var c4 = 5>18 ?5:18;  //true return 5 false return 18


//流程控制语句
if(c1 === c2){
    console.log('c1=c2')
}else{
    console.log('c1!=c2')
}

switch (c1){
    case 1:
        console.log('1')
        break
    case 2:
        console.log('2')
        break
    default:
        console.log('不知道')
}

//循环语句
while(c1<15){
    console.log(c1,'ok')
    c1++
}

for (var i=0;i<10;i++){
    console.log(1 ,'first')
}

var arr=[0,1,2,3,4,5,6,7,8,9]
for (var i in arr){
    console.log(2, 'second')
}


//数组
    //两种声明方式
    var a1=[1,2,3];
    var a2 = new Array(1,'a',true);

    //数组方法
    console.log('a1的长度为',a1.length);
    console.log('a1后面添加一个元素',a1.push('周公瑾'),a1);
    console.log('a1删除最后一个元素',a1.pop(),a1);
    console.log('a1最前面添加一个元素',a1.unshift('牛逼'),a1);
    console.log('a1最前面删除一个元素',a1.shift(),a1);
    console.log('a1元素顺序反转',a1.reverse(),a1);

    //数字排序(原始排序方法按照ascii码的顺序去排列，可能出现10，100比2小的情况)
    function sort_num(x,y){
        return y-x;
    }
    console.log('排序结果为',a1.sort(sort_num))

    //任意位置删除多个元素,添加多个元素,替换多个元素
    //splice(操作位置的下标,删除操作的成员长度,"替换或者添加的成员1","替换或者添加的成员2")
    var arr=[1,2,3,4,5,56,5,64,74,65,]
    console.log('删除arr第二个字符后面的两个元素',arr.splice(2,2),arr)
    console.log('向arr第二个字符后面添加两个元素',arr.splice(2,0,3,4),arr)
    console.log('替换arr第二个字符后面添加两个元素',arr.splice(2,2,100,1000),arr)

    //合并两个数组
    console.log('拼接a1 & a2为：',a1.concat(a2))
        
    //拼接数组内的元素
    var name='周 公 瑾'
    var ret = name.split(' ');
    console.log('用逗号拼接ret内部元素为',ret.join(','))

    //数组切片
    console.log('arr的第一个到第五个元素为：',arr.slice(1,5))

//object对象（字典）
    //声明object对象
    var person1 = new Object();
    person1.name='周公瑾';
    person1.age=21;
    console.log('我的object对象是：',person1)
    console.log('我的object对象中的name属性值为：',person1.name)
    console.log('我的object对象中的age属性值为：',person1.age)

    var person2 ={
        name:'诸葛亮',
        age:66
    }
    console.log('我的object对象是：',person2)
    console.log('我的object对象中的name属性值为：',person2.name)
    console.log('我的object对象中的age属性值为：',person2.age)

    //访问方式
    console.log('我的object对象中的name属性值为：',person2.name,person2['name'])

    for(var attr in person1){
        console.log(attr,person1[attr]);
    }


//JSON序列化和反序列化
    // 把json对象转换成json字符串
    var data = {
        name: "xiaoming",
        age: [22,33,44],
        say: function(){
            alert(123);
        }
    };
    var ret3 = JSON.stringify(data);
    console.log(ret3 ); // {"name":"xiaoming","age":22}

    // 把json字符串转换成json对象
    var str = `{"name":"xiaoming","age":22}`;
    var ret4 = JSON.parse(str);
    console.log(ret4);


//Date对象
    //声明Date对象
    var d1 = new Date();
    console.log(d1)
    console.log('转换为字符串：',d1.toLocaleString())

    var d2 = new Date('2021-05-08 11:55:38');
    console.log('我输入的日期为：',d2.toLocaleString())

    var d3 = new Date(5000);   //时间戳（毫秒）
    console.log('计算后的时间为：',d3.toLocaleString())


    //获取时间的部分信息

//Math对象
    var num = -3.1415926;
    console.log('保留两位小数',num,num.toFixed(2));
    console.log('取绝对值',num,Math.abs(num));
    console.log('向上取整',num,Math.ceil(num));
    console.log('先下取整',num,Math.floor(num));
    console.log('四舍五入',num,Math.round(num));
    console.log('乘方运算',num,Math.pow(num,2));
    console.log('随机取值',Math.random());

