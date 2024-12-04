##### class Mouse
- `Mouse.说明`
	- 鼠标相对于视口的左上角以主框架 CSS 像素操作。
	- 每个页面对象都有自己的鼠标，可以通过 [[Page.实例属性|page.Mouse]] 访问。
```python
# using ‘page.mouse’ to trace a 100x100 square.
page.mouse.move(0, 0)
page.mouse.down()
page.mouse.move(0, 100)
page.mouse.move(100, 100)
page.mouse.move(100, 0)
page.mouse.move(0, 0)
page.mouse.up()
```
- [[Mouse.实例方法]]
