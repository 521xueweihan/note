# 看廖雪峰老师js教程随手记录下来的笔记

## 入门
1. 每行结尾记得写“;”，不写也不会报错。
2. NaN表示“Not a Number”，例如：`0/0`结果为NaN。**注意**：NaN与任何值不等包括它自身。唯一能判断Nan的方法是通过`isNaN()`函数。
3. Infinity 表示无限大。
4. `==`它会自动转换数据类型在比较，而`===`不会自动转换类型，如果数据类型不一样，返回`false`。
5. 比较浮点数：因为计算浮点数有误差所以，只能计算它们的差的绝对值，看是否小于某个阈值。`Math.abs(1 / 3 === (1 - 2 / 3)) < 0.000001;`
6. JavaScript的对象是一组由'键-值'组成的无序集合（很像python中的字典），然后可以通过`对象变量.属性名`获取一个对象的属性。
7. 多行字符串使用｀｀，等同于python中的`"""...."""`
8. 数组操作中，如果索引值超过了范围，JavaScript的数据不会报错，而是改变数据的大小。
9. 通过`arr.slice() === arr`是false，通过slice()复制的数组不等于原来的数组。
10. 对象属性如果形如：`xxx-xx`则需要用`xxx[xxx-xx]`形式进行操作和赋值。
11. 要判断一个对象的某个属性是自身拥有的，而不是继承的，则需要用`hasOwnProperty()`方法。
12. `for (;;)`如果没有`break`则将无限循环下去。
13. 使用Map时需要注意：由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉！

## 函数
1. JavaScript可以传入任意个参数而不影响调用。传入的参数多，虽然函数中并不需要这些参数。如果少的话，返回Nan。
2. 关键字arguments可以获得传入的所有参数。
3. reset参数可用获取而外的参数，返回一个数组。**注意**:reset参数只能写在最后。
4. 在JavaScript中，前面调用，后面声明的变量，不回报错。但这个变量的值为：undefined！**注意**:这点和python不一样！
5. 全局变量会绑定在window上。
6. 控制语句中的变量，可以在控制体之外调用。跟python一样，ES6引入了新的关键字`let`，使用`let`代替`for`。可以解决这个问题。
7. 为了防止this带来的问题，只在对象内的方法中使用this，`this`相当于python中的`self`。
8. `sort()`方法会直接对Array进行修改，它返回的结果仍是当前Array
9. 箭头函数：`x => x * x`相当于`function (x) { return x * x; }`

## 标准对象
1. Date对象的月份从0～11
2. 不要使用new Number()，new Boolean()，new String()创建包装对象；使用parseInt()或parseFloat()来转换任意类型到number;用String()来转换任意类型到string，或者直接调用某个对象的toString()方法；通常不必把人一类型转换为boolean，在判断。typeof操作符可以判断出number,boolean,string,function和undefined；判断Array要使用Array.isArray(arr)；判断null使用 myVar === null；判断某个全局变量是否存在typeof window.myVar === 'undefined'；函数内部判断某个变量是否存在typeof myVar === 'undefined'
3. 数字转成字符串`(123).toString()`
4. JSON格式的字符串，通常使用JSON.parse()把它变成一个JavaScript对象。
5. 正则对象格式：`/正则表达式/`

## 面向对象编程
1. JavaScript中没有实例的概念，而是通过原型（prototype）来实现面向对象编程。
2. 创建对象通过function，调用这个function的时候一定要new function，否则函数内的this，会提示undefined
3. 面向对象编程，参照：
```JavaScript
// 创建类
class Student{
	constructor(name) {
		this.name = name;
	}
	hello() {
		alert('Hello, ' + this.name + '!' );
	}
}

// 继承类
class PrimaryStudent extends Student {
	constructor(name, grade) {
		super(name); // 继承父类的构造方法
		this.grade = grade;
	}
}
```

## 浏览器对象
js在前端的应用作用就是操作页面中的元素实现动作效果。  
1. location对象可以实现加载新的页面，也就是js实现页面跳转。
2. document对象表示当前页面。它是整个DOM树的根节点。也就是说，可以通过document对象实现操作当前页面的元素。
3. 操作DOM：需要先获取操作的元素，如果是插入操作需要先新建一个元素，之后使用appendChild方法插到队尾，使用`parentElement.insertBefore(newElement, referenceElement);`插到指定位置；更新DOM则需要使用innerHTML（非转译，innerTEXT转义），注意style对应的是css的样式。
4. 操作文件：表单的`enctype`必须指定为`multipart/form-data`，`method`必须定为`post`。
5. HTML5提供了获取上传文件更多信息的功能。
6. ajax请求时，URL的域名必须和当前页面完全一致。

## jQuery
jQuery就相当于js一个库（类），写好了各种方法，方便于调用，操作dom节点。

1. 多层选择：`$('ancestor descendant')`（祖先，后代）注意：不是父子节点。
2. 子选择器：`$('parent>child')`child节点必须是parent节点的直属子节点。
3. 过滤器：附加在选择器上，例如：`$('ul.lang li:nth-child(even)'); // 选出序号为偶数的元素`
4. 查找：`find()`方法是向下查找，`parent()`方法是从当前节点向上查找。**注意** 同一层的节点通过`next()`和`prev()`方法
5. 筛选：`filter()`方法可以过滤掉不符合选择条件的节点
6. 遍历某标签下面的所有值：`$("xxx").each(function())`函数中使用this变量，操作遍历的数据。参考：http://www.w3school.com.cn/jquery/jquery_traversing.asp
7. 操作DOM：
	- 节点的text方法获取文本，html方法获取html。如果该节点不存在，不会报错！
	- css方法是操作样式的，可以直接修改任何样式属性。`addClass()`方法可以直接添加‘样式类’。
	- 显示和隐藏DOM：show()和hide()方法，而不需要去关心display属性。  
	- 操作属性：`attr()`和`removeAttr()`获取，修改，删除属性，例如：`div.attr('name', 'Hello'); // div的name属性变为'Hello'`
	- 获取选择框，下拉框的选项：`var selected = $('#test-option'); selected.is(':selected'); //true`
	- 获取value值：val()方法。**注意**：选择框也可通过`val()`方法获取，选择之后的值。
8. 修改DOM：增加：`append()`方法，增加到最后；`prepend()`方法，增加到最前面；`after()`和`before()`方法，指定在那个节点的前后；`remove()`方法，删除节点。
9. ready事件：`$(function () {...})`常见的ready方法的写法。
10. `off()`方法，移除所有的绑定事件。
11. **注意**:用户操作才会出发时间，javascript修改值不会触发事件。但是：`input.change()`相当于`input.trigger('change')`，它是`trigger()`方法的简写。
12. 动画：`div.hide(3000); // 在3秒钟内逐渐消失`。**注意**：时间单位为毫秒。`toggle()`根据当前状态，执行另外一种动画。
13. `animate()`方法，当前状态，转变成传入参数的状态。
14. **注意**：在使用jQuery时候，因为是链式操作，所以需要返回this。
