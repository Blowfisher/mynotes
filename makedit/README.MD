# Javascript note
```text
Javascript  区分大小写


语句以分号 ; 结束，语句块{...}

注释：
行注释：
// 加速度克劳馥的接口

块注释：
/**
技术的开发了手机
**/




数据类型和变量：
Number :Javascript不区分整数和浮点数，统一用Number表示


字符串：字符串是以单引号 ' 或双引号 " 括起来的任意文本


布尔值：布尔值和布尔代数的表示完全一致，一个布尔值只有True、false两种值

&&与运算，只有所有都为true，&&运算结果才是true
||或运算，只要其中有一个为true，||运算结果为true

！运算是非运算，它是单目运算符


特别注意相等运算符== 
== 比较，它会自动转换数据类型再比较，
===比较，它不会自动转换数据类型，如果数据类型不一致，返回false

NaN 这个特殊的Number与所有其他值都不相等，包括它自己：
NaN === NaN;

唯一能判断NaN的方法是通过isNaN()函数：
isNaN(NaN);//true


最后要注意浮点数的相等比较：
1/3 === (1-2/3);//false 

浮点数在运算过程中会产生误差，因为计算机无法精确表示无限循环小数，要比较连各个浮点数是否相等，只能计算它们之差的绝对值，看是否小于某个阈值：
Math.abs(1/3-(1-2/3)) < 0.0000001;//true

null和undefined
null表示一个‘空’的值，它和0以及空字符串‘’不同，0是一个数值，‘’表示长度为0的字符串，而null表示‘空’。


数组：
数组是一组按顺序排列的集合，集合的每个值称为元素。数组用[]表示，元素之间用,分隔。

[1,2,3];
另一种创建数组的方法是通过Array()函数实现
new Array(1,2,3);

数组的元素可以通过索引来访问。索引起始值为0：
var arr = [1,2,3,4,5,'Hello',null,true];
arr[0];



对象
Javascript的对象是一组由键-值组成的无序集合，eg：
var person = {
	name:'Bob',
	age:20,
	tags:['js','web','mobile'],
	city:'Beijing',
	hasCar:true,
	zipcod:null 
};

Javascript对象的键都是字符串类型，值可以是任意数据类型。
要获取一个对象的属性，我们用  对象变量.属性名 的方式
person.name;



变量：

use strict 定义变量时需先声明: var a

字符串操作
message = '你好' + name +',你今年'；
message = ‘你好，${name},你今年${age}岁了！’；

var s = 'string'
s.[N] 序列号访问数据

toUpperCase()把一个字符串全部变为大写
s.toUpperCase()

toLowerCase()把一个字符串全部变为小写
s.toLowerCase()


indexOf()会搜索指定字符串出现的位置
s.index('string')

substring()返回指定索引区间的子串
s.substring(0,5)




数组 Array 数组可以更改长度,超出长度的元素以undefined表示 支持索引，修改，超出索引范围的索引赋值会引起Array大小变化
 
var arr = [1,2,3,4,'Hi']
arr.length


indexOf()搜索一个指定元素位置
slice()对应string的substring()版本

arr.slice(0,2)

arr.slice() 返回所有元素



push() 和pop()

arr.push('a','b') //往arr数组末尾添加若干元素
arr.pop() //把arr最后一个元素删掉


unshift() shift()

arr.unshift('1,'2',) //在arr头部添加若干元素
arr.shift() //把arr头部第一个元素删掉


sort()
arr.sort() //对arr排序，会直接修改arr元素位置

reverse（）
arr.reverse() //对arr中的元素 位置反转操作





splice() 可以从指定的索引开始删除若干元素，然后再从该位置添加若干元素

arr.splice(2,3,'apple','pear')； //从第三个元素开始往后删除3个元素，然后再添加2个元素


arr.splice(2,2) //从第三个开始 往后删除2个元素

arr.splice(2,0,'apple','pear') //从第三个元素开始，删除0个元素，然后再添加2个元素




concat()把两个array连接起来，返回一个新的array

var arr = ['a','B','C'];
arr.concat(1,2,[3,4]); 



join()把当前array的每个元素都用指定的字符串连接起来，然后返回连接后的字符串
var arr = ['A','B']
arr.join('-')  //返回‘A-B’






对象：无序集合{...}表示一个对象

成员判断 in 
var  object = {
	name: 'name',
	birth: 1990,
	school: 'No.1 middle School',
	score: null
}


有些属性是继承的，用 in 判断时要注意，可以用hasOwnProperty()方法；

object.hasOwnProperty('name'); //true 


条件判断：
if () {
	...
}
else {
	...
}


if (){...}else if(){...} else ....




javascript 把null、undefined、0、NaN和空字符串''视为false，其他值一概视为true




for (i=1;i<=N;i++){...}
for(;;){//无限循环}

for ...in 对象时获取key为索引，数组时获取的key为元素 

var o = [1,2,3,4]
var o = {
	name: 'JACK';
	age: 20;
	city: 'Beijing'
};
for (var key in o) {
	if (o.hasOwnProperty(key)){
		console.log(key);
	}
}


for ...of 
for (var x of a){
	...
	}



while (n>99){...}

do...while 
do {
	...
}
while(n>100);



JavaScript的默认对象表示方式{} 键值对


Map是一组键值对的结构，具有极快的查找速度。
var m = new Map([['Michael',95],['Bob',99],['Tracy',87]]);
m.get('Bob');

初始化空Map
var m = new Map();
m.set('Bob',99);
m.has('Bob');
m.delete('Bob');

对同一个键反复赋值 有效值为最后一次赋值



Set 是一组key的集合，不存储value，由于key不能重复，所以Set中，没有重复的key。重复的元素将自动过滤
var s1 = new Set();
var s2 = new Set([1,2,3,4]);


Set增加key
s1.add(key);

Set删除key
s1.delete(key);



iterable 对象 array set map  
for ... of  循环iterable对象的元素而不是(for ... in)属性


iterable对象内置forEach方法，它接受一个函数，每次迭代就自动回调该函数
var a = ['A','B','C'];
a.forEach(function(element,index,array){
	console.log(element + ',index = ' + index);
});

set与array类似，但set没有索引，因此回调函数的前两个参数都是元素本身；
var s = new set(['A','B','C'])
s.forEach(function (element,sameElement,set) {
	console.log(element);}

Map 的回调函数参数依次为 value key 和 map本身
var m = new Map(function (value,key，map){
	console.log(value);
})




函数 
function abs(x){...}
function 指出这是一个函数定义；
abs 是函数名
(x) 括号内列出函数的参数，多个参数以,分隔
{...} 函数体 

定义：
function abs(x){
	...
	return x     #没有return时 返回结果为undefined
	}


第二种函数定义方式
var abs = function (x){
	....
	return x;
};

function (x) {...} 是一个匿名函数，他没有函数名 赋值给abs引用


判断值类型 使用 typeof x !== 'number'


arguments 函数内部起作用，永远指向当前函数的调用者传入的所有参数。arguments类似array但不是一个array

arguments.length

rest 参数只能写在函数形参列表最后，前面用...标识，未指明的参数将绑定至rest变量



JavaScript的函数在查找变量时从自身函数定义开始，从“内”向“外”查找。
如果内部函数定义了与外部函数重名的变量，则内部函数的变量将“屏蔽”外部函数的变量


变量提升 但不会同时赋值


window 全局作用域

let 申明一个块级作用于变量

const 与 let 都具有块级作用域 

const 定义常量
const PI = 3.14;


解构赋值  对应层次必须一致 结构必须一致
声明同时赋值 
var [x,y,z] = [1,2,3];

如果声明后再赋值会报错 需要用小括号括起来
var x,y;
({x,y} = {name:'小明',age:21,gender:'male'});



apply函数方法 把参数打包成array再传入
apply 指定函数的this指向对象，fun.apply(obj,[]) array表示函数本身的参数；

call()把参数按顺序传入。

普通函数通常把this绑定未null
Math.max.apply(null,[3,4,5]);
Math.max.call(null,3,4,5);





高阶函数
map()方法定义在JavaScript的Array中
function foo(){...}
arr = [1,23,4,5,6];
arr.map(foo);

reduce()方法定义在JavaScript的Array中 reduce()中fun()必须接收两个参数，


fileter 常用于把array的某些元素过滤掉，true的话 然后返回剩下的元素



箭头函数  x =>x*x;







map 一组键值对的结构，具有极快的查找速度 
申明方式：
var m=new map([['a',11],['b',12]]);
添加：m.set('E',122);
删除：m.delete('E')  是否有key m.has('E')  获取 m.get(‘E’)


set 集合一组key的集合，不存储value，key不能重复
添加：var s=new set([1,2,3,4,5])
    s.add(6)  s.delete(6)



自执行函数：
 (function (){...})()


字符串常用方法和属性:
obj.trim() 去空格
obj.charAt(index) 索引找字符
obj.substring(start,end) 分片
obj.indexOf(char) 




dom选择器：
document.getElementById('id')
document.getElementsByClassName('name')
document.getElementsByTagName('tagname ')


创建标签:document.createElement('a')
	link.href='http://www.baidu.com'
	link.innerText='百度'

var btn = document.createElement('input')
btn.type = 'button'
btn.value = '我是动态的'

var test = document.getElementById('test');

先定位id为‘test’的节点，再返回其内部所有‘tr’节点
var trs = document.getElementById('test').getElementsByName('tr');


获取节点‘test’下的所有直属子节点
var cs = test.children;


获取test下第一个、最后一个子节点
var first = test.firstElementChild;
var last = test.lastElementChild;







typeof 区分对象类型 number;boolean;string;function和undefined 无法区分 null;[] {}

判断Array用Array.isArray()
判断null 用myVay === null;

判断某个全局变量是否存在用typeof window.myVar ==='undefined';
函数内部判断某个变量是否存在用 typeof myVar === 'undefined';



typeof 123; //number 

parseInt() 把任意类型装换到number
parseFloat() 把任意类型装换到float

String() 或 toString()




javascript 月份表示 0 january 1 february 2 march 3 April 4 may ;5 june;6 july 7 august ;8 september 9 october 10 november 11 december 

时间处理 Date()

var now = new Date();
now.getFullYear(); 
getMonth();月份
getDate(); 天
getDay();星期几
getHours(); 24小时制
getMinutes(); 分钟
getSeconds(); 秒
getMilliseconds(); 毫秒 
getTime(); number形式表示时间戳



var a = new Date(11232344455);
a.toLocalString(); 显示的字符串与操作系统设定的格式有关
d.toUTCString(); // 'Wed, 24 Jun 2015 11:49:22 GMT'，UTC时间，与本地时间相差8小时








RegExp 正则表达式：
\d  匹配一个数字  \D
\w  匹配一个字母或数字下划线  \W
. 可以匹配任意字符
* 匹配任意一个字符 0次或无穷次

+ 匹配至少一个字符


? 匹配 0 个或1 个字符
{n} 表示匹配n次
{n,m} 表示至少匹配n次 至多匹配m次
\s 匹配一个空格（包括tab） \S






序列化：JSON

var xiaoming = {...}
var s = JSON.stringify(xiaoming,func,'  ');
var s = JSON.stringify(xiaoming,['name','skills'],'  ')

var xiaoming = {
    name: '小明',
    age: 14,
    gender: true,
    height: 1.65,
    grade: null,
    'middle-school': '\"W3C\" Middle School',
    skills: ['JavaScript', 'Java', 'Python', 'Lisp'],
    toJSON: function () {
        return { // 只输出name和age，并且改变了key：
            'Name': this.name,
            'Age': this.age
        };
    }
};

JSON.stringify(xiaoming)
console.log:  "{"Name":"小明","Age":14}"


console.log(s);
function func(key,value){...}

反序列化：JSON.parse()





window 对象不但充当全局作用域，而且表示浏览器窗口

window对象有innerWidth和innerHeight属性，可获取浏览器窗口内部宽度高度

outerWidth和outerHeight 可以获取浏览器窗口整个高宽


navigator对象表示浏览器的信息：
navigator.appName 浏览器名称
navigator.appVersion 浏览器版本
navigator.language  浏览器设置的语言
navigator.platform 操作系统类型
navigator.userAgent 浏览器设定的User-Agent字符串



screen对象表示屏幕的信息，
screen.width 屏幕宽度，以像素为单位
screen.height 屏幕高度，以像素为单位
screen.colorDepth 返回颜色位数



location对表示当前页面的URL信息
location.href 完整的url
location.host //www.baidu.com
location.protocol //http
location.port //80
location.pathname // /path/index.html/
location.search //？a=1&b=2
location.hash top

location.assign() 加载一个新页面  
location.reload() 重新加载当前页面




document对象表示当前页面，由于html在浏览器中以DOM形式表示树形结构，document对象就是整个dom树的根节点
document.title 表示网页title



document对象还有一个cookie属性，可以获取当前页面的cookie



document.querySelector('#q1') 获取id为q1的节点
document.querySelectorAll('div.highlighted >p') 获取q1节点内的符合条件的所有节点

修改、更新DOM
var p = document.getElementById('p-id');
p.inneText = 'adc'; 能自动对内容编码，保证无法设置任何标签 不返回隐藏元素的文本
p.innerHTML = '<span>hi<\span>' 能修改结构，但要对内容编码避免xss攻击
p.textcontent =‘adb’ 能自动对内容编码，保证无法设置任何标签 返回所有文本




移动、插入操作：appendChild()
移动操作后 树状结构将改变，移动的标签会在原来node删除 新的node添加
var js = document.getElementById('js');
var list = document.getElementById('list');
list.appendChild(js);

新建插入操作
var d = document.createElement('style');
d.setAttribute(type,'text/css');
d.innerHTML = 'p{color:red}';
document.getElementsByTagName('head')[0].appendchild(d);



var 
	list = document.getElementById('list');
	ref = document.getElementById('python');
	haskell = document.createElement('p');
	haskell.id = 'haskell';
	haskell.innerText = 'Haskell';
	list.insertBefor(haskell,ref);
	
	

删除DOM：先获取该节点本身及它的父节点，然后再调用父节点的removeChild把自己删除
var  self = document.getElementById('to-be-removed');

var parent = self.parentElement;

var removed = parent.removeChild(self);





操作表单：
文本框：<input type="text" />
口令框：<input type="password" />
单选框：<input type='radio' />
复选框：<input type='checkbox' />
下拉框：<select></select>
隐藏文本：<input type="hidden" />
<input type='color' value='red'>
<input type='date' value='2017-12-5'> datetime datetime-local 


获取值：仅适用于text password hidden 以及select
// <input type="text" id='email'>
var input = document.getElementById('email');
input.value //获取用户输入的值

单选、复选的value属性返回的永是HTML的预设值，而我们需要获得的是用户是否勾上了选项，用checked判断


设置值：input.value = 'text@jianke.com'




提交表单:
<form id="test-form" onsubmit="return checkForm()">
   <input type="text" name="test">
   <button type="submit">Submit</button>
 </form>
 <script>
 function checkForm(){
 	var form = document.getElementById("test-form");
 	return true;  //true为提交 false 不会提交
 }
 </script>


 提交加密的密码：
 <form id="login-form" method="post" onsubmit="return checkForm()">
   <input type="text" id="username" >
   <input type="password" id="input-password">
   <input type="hidden" id="md5-password" name="password">
   <button type="submit">Submit</button>

<script>
function checkForm(){
	var input_pwd = document.getElementById("input-password");
	var md5_pwd = document.getElementById('md5-password');
	md5_pwd.value = toMD5(input_pwd.value);
}
</script>





文件操作：
<input type="file"> 
文件api接口: file FileReader

var reader = new FileReader();
reader.onload = function(e) {
	var data = e.target.result;
	preview.style.backgroundImage = 'url('+data+')'
}
reader.onload()回调函数


AJAX :Asynchronous JavaScript and XML 
用JavaScript 执行异步网络请求

eg:
function success(text){
	var textarea = document.getElementById('test-response-text');
	textarea.value = text;
}
function fail(code){
    var textarea = document.getElementById('test-response-text');
    textarea.value = 'Error code:' + code;
}
var  request;
if (window.XMLHttpRequest){
	request = new XMLHttpRequest();
}else {
	request = new ActiveXObject('Microsoft.XMLHTTP');
}

request.onreadystatechange = function(){
	if(request.readystate === 4){
	    if (request.status === 200){
	      return success(request.responseText);
	    }else {
	      return fail(request.status);
	    }
	}else{
	  //*****
	}
}
request.open('GET','api/categories');
request.send();
alert('请求已发送，请等待响应。。。');



































======+++++++++++++++++++++++++++++==============================
JQUERY




面向对象编程：没有类只有函数 对象
function Student(props){
	this.name=props.name
}
Student.prototype.hello = function (){
	alert('Hello, '+this.name+'!');
}
实现桥接原型链
function inherits(Child,Parent){
	var F=function(){
	F.prototype = Parent.prototype;
	Child.prototype=new F();
	Child.prototype.constructor=Child;
	}
}


ES6新添加了class定义类
class Student {
	constructor(name){
	  this.name=name;
	}
	say() {
	 alert('Hi, '+this.name+'!');
	}
}

class继承:
class PrimaryStudent extends Student {
	constructor(name,grade){
	super(name);
	this.grade=grade;
	}
	myGrade(){
	  alert('I am at grade'+this.grade);
	}
}





location 代表当前url
window 既是全局变量又代表当前浏览器窗口
navigator 代表当前浏览器
screen


Dom更新操作
list = document.getElementById('eg');
list.innerHTML = 'xxx'
list.innerText = 'xxx'

Dom 插入操作:
var js = document.creatElemnt('p')
js.id="js"
js.innerText='javascript'
list.appendChild(js)

list.insertBefore(py,js);





删除操作：
var self = document.getElementById('removed');
var parent = self.parentElement;

var removed = parent.removeChild(self);


操作表单:









jquery别名$ 
选择器：$('p')标签选择器
$('#id') id选择器
$('.name') 类选择器
$('[name=name]') 固定标识选择器

层级选择器
$('p.name input ')
子选择器:类似层级选择器，但是限定了层级关系必须是父子关系
$('parent>child')

过滤器 filter
$('ul.lang li') 层级选择

$('ul.lang li:first-child');
$('ul.lang li:last-child');
$('ul.lang li:nth-child(2)');选出第N个元素，N从1开始;
$('ul.lang li:nth-child(even)'); 选出序号为偶数的元素
$('ul.lang li:nth-child(0dd)') 选出序号为奇数的元素



操作DOM 
修改text和HTML
js1 = $('test-ul li[name=name]').text() 获取对应dom节点 的文本
js2 = $('test-ul li[name=name]').html() 获取对应原始html文本

设定text和html
js1 = $('test-ul li[name=name]')

js1.text('text')修改文本
js1.html('<span style='color:red'>javascirpt</span>') 修改html


修改CSS
调用jQuery对象的css('name','value')
eg:
$('#test-css li.dy>span').css('background-color', '#ffd351').css('color', 'red');

eg:
var div = $('#test-div')
div.css('color'); 获取css属性
div.css('color','#336621');设定css属性
div.css('color','');清除css属性



选择离最近的元素，元素可以是父级，可以是子集
$('#span02').closest('div').css({width:'200px',height:'200px'})


$('.list li') 不能回到父级
$('.list').children(): 可以通过end() 回到父级(选择父级的所有子元素)
 
$('.list').children().css({background:'gold',height:'30px'}).end().css({background:'green'});



siblings('.list') list同一级别其它兄弟元素选中 
$('.list li:eq(2)').css({background:'gold'}).siblings().css({background:'green'})



$('div').find('.list') 在div中找class为list的元素




##**：选择器获取的多个元素，获取信息获取的是第一个。比如 $('div').css('width') 获取的是第一个div的width


操作样式类名：
$('#div1').addClass('divClass2') //为id为div1的对象追加divClass2
$('#div1').removeClass('divClass2')//移除id为div1的对象的class名为divClass2的样式
$('#div1').addClass('divClass divClass2 ')//移除多个样式
$('#div1').toggleClass('anotherClass')//重复切换anotherClass样式




this是原生对象
$(this).index() 获取当前按钮所在层级范围的索引值
eg:选项卡
<script type="text/javascript" src="js/jquery-1.12.4.min.js"></script>
<script type='text/javascript'>
$(function(){
	$('#btns input').click(function{
		$(this).addClass('cur').siblings().removeClass('cur');
		$('#contents div').eq($(this).index()).addClass('active').
		siblings().removeClass('active');
	});
})
</javascript>


jquery 属性操作

1、$('#div1').html() 获取添加操作
2、$('#div1').text() 获取/添加文本内容
3、$('#img1').attr('src') 获取/设置某个属性的值 (获取图片地址)


4 checked 是否选中
读写checkbox的属性
$('#check').prop('checked'); //确定当前是否选中
$('#check').prop(checked:true)






事件：on 方法用来绑定一个事件
eg: 
var a = $('#test-link');
a.on('click',function(){
	alert('Hi');
})

简化版:
a.click(function(){
	alert('Hi');
})

鼠标事件：
click:鼠标单击时触发
dblclick：鼠标双击时触发
mouseenter:鼠标进入时触发
mouseleave:鼠标移出时触发
mousemove:鼠标在DOM内部移动时触发
hover:鼠标进入和退出时出发两个函数，相当于mouseenter加上mouseleave

键盘事件
键盘事件仅作用在当前焦点的DOM上，通常是input 、textarea

keydown:键盘按下时触发
keyup:键盘松开时触发
keypress:按一次键后触发

其它事件
focus:当DOM获得焦点时触发
blur:当DOM失去焦点时触发
change:当input，select，textarea的内容改变时触发
submit：当form提交时触发
ready：当页面被载入并且dom树完成初始化后触发






异常处理
try ... catch ... finally

```





















































































































