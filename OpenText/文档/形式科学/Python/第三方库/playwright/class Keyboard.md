##### class Keyboard
- `Keyboard.说明`
	- 提供用于管理虚拟键盘的 API
	- 每个页面对象都有自己的键盘，可以通过 [[Page.实例属性|page.Keyboard]] 访问。
```python
# 按住shift以选择和删除某些文本的示例
page.keyboard.type("Hello World!")
	# Hello World!
page.keyboard.press("ArrowLeft")
	# Hello World[光标]!
page.keyboard.down("Shift")
	# 按住shift键
for i in range(6):
	# 左键选中6个字符 " World"
    page.keyboard.press("ArrowLeft")
page.keyboard.up("Shift")
	# 释放shift键
page.keyboard.press("Backspace")
	# 删除选中字符

# 大写A
page.keyboard.press("Shift+KeyA")

# 全选
page.keyboard.press("Control+A")
```
- [[Keyboard.实例方法]]
