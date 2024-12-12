##### 整体认识
- 整体认识
	- 下面是一个在 `<script>` 标签嵌入 JS 代码的 [[标记语言.HTML|HTML]] 文件, 可以保存为 `hi.html` 用浏览器打开运行, 这段代码实现了一个简单的网页交互功能, 用户可以在文本框中输入自己的名字, 点击按钮后页面会显示一条问候信息, 它涵盖了基本的语法包括变量声明, 控制结构, 函数, 事件处理和 DOM 操作
		- 通过 `const` [[JS.const|声明]]了三个变量 `nameInput`, `greetButton`, `greetingMessage`, 值是使用 `document.getElementById()` 获取的 DOM 元素, 分别表示文本输入框 `<input>`, 问候按钮 `<button>` 和问候段落 `<p>`
		- 通过 `function` [[JS.function|声明]]了一个函数 `greet()`, 用于生成问候信息
			- 通过 `const` [[JS.const|声明]]了一个变量 `name`, 值是 `<input>` 的文本, 接着是一个 `if...else` [[JS.if...else|条件判断]]语句, 判断 `name` 是否为空, 如果不是空就设置 `<p>` 的文本为问候信息, 否则为提示输入信息
		- 通过 `addEventListener()` 为 `<button>` 添加点击事件, 当按钮被点击时, 调用 `greet()` 函数
```html
<!DOCTYPE html>
<html lang="zh-cn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Introduction</title>
</head>
<body>
    <h1>JavaScript 初步示例</h1>

    <!-- 输入框 -->
    <label for="nameInput">请输入你的名字:</label>
    <input type="text" id="nameInput" placeholder="你的名字">
    
    <!-- 按钮 -->
    <button id="greetButton">问候我</button>

    <!-- 显示问候信息的区域 -->
    <p id="greetingMessage"></p>

    <script>
        // 1. 获取 DOM 元素
        const nameInput = document.getElementById('nameInput');
        const greetButton = document.getElementById('greetButton');
        const greetingMessage = document.getElementById('greetingMessage');

        // 2. 定义一个函数，用于生成问候信息
        function greet() {
            // 获取输入框中的名字
            const name = nameInput.value.trim();
            
            // 判断名字是否为空
            if (name) {
                // 生成问候信息
                greetingMessage.textContent = `你好, ${name}! 很高兴见到你！`;
            } else {
                // 提示用户输入名字
                greetingMessage.textContent = '请输入你的名字。';
            }
        }

        // 3. 为按钮添加点击事件监听器
        greetButton.addEventListener('click', greet);
    </script>
</body>
</html>
```
