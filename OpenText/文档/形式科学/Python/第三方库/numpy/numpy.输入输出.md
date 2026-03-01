##### numpy 输入
```python
# 输入
np.loadtxt(frame, dtype=np.float,delimiter=None, unpack=False,)
#	frame:文件、字符串或产生器，可以是.gz或.bz2的压缩文件
#	dtype:数据类型，可选
#	delimiter:分割字符串，默认是任何空格
#	unpack:如果True，读入属性将分别写入不同变量
		
np.fromfile(frame, dtype=float, count=‐1, sep='')  
#	frame:文件、字符串
#	dtype:读取的数据类型  
#	count:读入元素个数，‐1表示读入整个文件  
#	sep:数据分割字符串，如果是空串，写入文件为二进制


```
##### numpy 输出
```python
np.savetxt(frame, array, fmt='', delimiter=None, newline='\n', header='', footer='', comments='#', encoding=None)
#	frame:文件、字符串或产生器，可以是.gz或.bz2的压缩文件
#	array:存入文件的数组
#	fmt:写入文件的格式，例如：%d %.2f %.18e
#	delimiter:分割字符串，默认是任何空格
#	newline:分割行
#	header:头文件
#	footer:尾文件
#	comments:文件前符号
#	encoding:编码

np.tofile(frame, sep='', format='%s')
#	frame:文件、字符串  
#	sep:数据分割字符串，如果是空串，写入文件为二进制 
#	format:写入数据的格式
```