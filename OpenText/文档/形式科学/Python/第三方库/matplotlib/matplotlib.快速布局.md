##### 单图 [[matplotlib.pyplot|plt.axes()]] [[matplotlib.pyplot|plt.subplots()]] 
```python
# plt生成轴，axes
fig = plt.figure()
ax = plt.axes()
fig.show()

# plt生成轴，subplots
fig, ax = plt.subplots()
fig.show()
```
![[Pasted image 20240314100347.png]]
##### 对称子图 [[matplotlib.pyplot|plt.subplots()]] 
```python
# plt生成轴，subplots
fig, axs  = plt.subplots(2, 2)  # 行 列
# for ax in axs.flat:  # axes = ndarray([[ax1, ax2], [ax3, ax4]])
#     ax.plot(x, y)
fig.show()
```
![[Pasted image 20240314100504.png]]
##### 不对称子图 [[class matplotlib.figure.Figure|fig.add_subplot()]] [[class matplotlib.figure.Figure|fig.add_gridspec()]] 
```python
# fig生成轴，add_subplot
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)  # 2行 1列 第1轴
ax2 = fig.add_subplot(2,2,2)  # 2行 1列 第2轴
ax2 = fig.add_subplot(2,2,(3,4))  # 2行 1列 第3,4轴
fig.show()
```
![[Pasted image 20240314093247.png]]
```python
# fig生成轴，add_gridspec
fig = plt.figure()
spec = fig.add_gridspec(ncols=2, nrows=2)
ax1 = fig.add_subplot(spec[0, :])
ax2 = fig.add_subplot(spec[1, 0])
ax3 = fig.add_subplot(spec[1, 1])
fig.show()
```
![[Pasted image 20240314093323.png]]
```python
# fig嵌套生成轴，add_gridspec
fig = plt.figure()
gs0 = fig.add_gridspec(1, 2)  # 1行 2列
gs00 = gs0[0].subgridspec(2, 2)  # 右列，分成2*2
gs01 = gs0[1].subgridspec(3, 1)  # 左列，分成3*1
for a in range(2):
    for b in range(2):
        ax = fig.add_subplot(gs00[a, b])
for a in range(3):
    ax = fig.add_subplot(gs01[a])
fig.show()
```
![[Pasted image 20240314093336.png]]