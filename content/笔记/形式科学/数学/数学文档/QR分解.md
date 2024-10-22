##### QR分解
- QR分解
	- $A = QR$
		- $\begin{bmatrix}0&3&1\\0&4&-2\\2&1&1 \end{bmatrix}=\begin{bmatrix}0&0.6&0.8\\0&0.8&-0.6\\1&0&0 \end{bmatrix}\begin{bmatrix}2&1&1\\0&5&-1\\0&0&2\end{bmatrix}$
		- $A_{m\times n}$ [[矩阵]]
		-  $Q_{m\times n}$ [[正交矩阵]], $Q$ 的列向量组是 $A$ [[列空间]]的[[正交基|标准正交基]]
		- $R_{n\times n}$ [[三角矩阵|上三角矩阵]], $R$ 是[[可逆矩阵|可逆矩阵]]且在对角线上的元素为正数.
	- 若 $A$ [[矩阵的秩|列满秩]], 则可QR分解
		- 通过[[格拉姆-施密特方法]]求 $A$ [[列空间]]的[[正交基|标准正交基]]组成 $Q$ 
		- 然后通过 $A = QR\rightarrow Q^TA=Q^TQR=ER=R$ 求出$R$


