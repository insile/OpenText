##### class Locator
- `Locator.说明`
	- 定位器代表了一种随时在页面上查找元素的方法
	- 每个页面对象可以通过 [[Page.实例方法|Page.定位器]] 创建
```python
page.get_by_label("User Name").fill("John")

page.get_by_label("Password").fill("secret-password")

page.get_by_role("button", name="Sign in").click()

expect(page.get_by_text("Welcome, John!")).to_be_visible()
```
- [[Locator.实例方法]]
- [[Locator.实例属性]]
