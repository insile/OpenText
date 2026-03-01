##### 基础操作
- [[np.copyto()]]  将源数组的值复制到目标数组中
##### 维度
```python
np.expand_dims(a, axis)
	# 增加一个 指定维度 
	# np.expand_dims([1, 2, 3], axis=0)  (3,)->(1,3)
	# np.expand_dims([[1, 2], [3, 4]], axis=2)  (2,2)->(2,2,1)
np.squeeze(a, axis=None)
	# 去除 shape 为 1 的轴
```
##### 连接切分数组
- [[np.concatenate()]]  沿着现有轴连接一系列数组
- [[np.stack()]]  增加新轴, 并沿指定轴连接数组
- [[np.split()]]  沿轴将一个数组拆分为多个子数组
##### 增加移除元素
- [[np.insert()]]  沿轴在索引前插入数值
- [[np.append()]]  将数值追加到一个数组的末尾
- [[np.repeat()]]  沿轴重复元素
- [[np.pad()]]  用于在数组的边缘填充值