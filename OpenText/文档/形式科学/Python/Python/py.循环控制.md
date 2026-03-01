##### 循环控制
- 循环控制
	- [[py.continue|continue]] 结束当次循环，继续执行后续次数循环
	- [[py.break|break]] 跳出并结束当前整个循环，执行循环后的语句
	- [[py.else|else]] 没有break，正常完成循环后执行语句
```python
# continue 跳过2
for i in range(5):
    if i == 2:
        continue
    print(i)

# break 结束于3
for i in range(5):
    if i == 3:
        break
    print(i)

# else 正常结束
for i in range(5):
    print(i)
else:
    print("Loop finished.")

```