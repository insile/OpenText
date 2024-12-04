##### numpy 通用函数与运算符
- 通用函数(或简称 ufunc)是以**逐元素**的方式操作 ndarray 的函数，支持数组广播、类型转换和其他一些标准特性。例如逐元素的加或者减，numpy API专题中有很多函数是通用函数，特别是逻辑函数数学函数
- [[numpy.通用函数可选关键字参数]]
- 下面是通用函数对应的运算符
```python
# 两个数组各元素对应运算+ - * / ** 
y = xl + x2 
	# np.add(xl,x2[,y])
y = xl - x2 
	# np.subtract(xl,x2[,y])
y = xl * x2 
	# np.multiply(xl,x2[,y])
y = xl / x2 
	# np.divide(xl,x2[,y])
y = xl / x2 
	# np.true_divide(xl,x2[,y])
y = xl // x2 
	# np.floor_divide(xl,x2[,y])
y = -xl 
	# np.negative(xl[,y])
y = xl ** x2 
	# np.power(xl,x2[,y])
y = xl % x2 
	# np.remainder(xl,x2[,y]), np.mod(xl,x2,[,y])

# 算数比较，产生布尔型数组> < >= <= == != 
y = x1 == x2 
	# np.equal(xl,x2[,y])
y = xl != x2 
	# np.not_equal(xl,x2[,y])
y = xl < x2 
	# np.less(xl,x2[,y])
y = xl <= x2
	# np.less_equal(xl,x2[,y])
y = xl > x2 
	# np.greater(xl,x2[,y])
y = xl >= x2 
	# np.greate_equal(xl,x2[,y])

# 二元运算
y = x1 & x2 
	# np.bitwise_and(xl,x2[,y])
y = x1 | x2
	# np.bitwise_or(xl,x2[,y])
y = x1 ^ x2
	# np.bitwise_xor(xl,x2[,y])
y = ~ x1 
	# np.bitwise_invert(xl[,y])
```