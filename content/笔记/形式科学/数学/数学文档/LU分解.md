##### LU分解
- LU分解
	- $A = LU$
		- $\begin{bmatrix} 1 & 2 &3\\ 2 & 5&7\\3&5&3 \end{bmatrix}=\begin{bmatrix} 1 & 0 &0\\ 2 & 1&0\\3&-1&1 \end{bmatrix}\begin{bmatrix}1&2&3\\0&1&1\\0&0&-5\end{bmatrix}$
		- $A_{n\times n}$ [[方阵]]
		- $L_{n\times n}$ [[三角矩阵|下三角矩阵]], $L$ 的对角线都是 $1$, 乘数在 $L$ 的对角线下方
		- $U_{n\times n}$ [[三角矩阵|上三角矩阵]], $U$ 的主元在对角线上
	- LU分解是没有对换的[[初等变换]]消元法, 充要条件是消去第 $i$ 列时的 $a_{ii}$ 不为零, $A$ 顺序主子式全不为 $0$
		- $A=\begin{bmatrix} 1 & 2 &3\\ 2 & 5&7\\3&5&3 \end{bmatrix}$ $L=\begin{bmatrix} 1 & *&*\\2 & *&*\\3&*& *\end{bmatrix}$
		- $\cong\begin{bmatrix} 1 & 2 &3\\ 0 & 1&1\\0&-1&-6 \end{bmatrix}$ $L=\begin{bmatrix} 1 & 0&*\\2 &1 &*\\3&-1&* \end{bmatrix}$
		- $\cong\begin{bmatrix} 1 & 2 &3\\ 0 & 1&1\\0&0&-5 \end{bmatrix}$ $L=\begin{bmatrix} 1 & 0 &0\\ 2 & 1&0\\3&-1&1 \end{bmatrix}$
		- $U=\begin{bmatrix} 1 & 2 &3\\ 0 & 1&1\\0&0&-5 \end{bmatrix}$ $L=\begin{bmatrix} 1 & 0 &0\\ 2 & 1&0\\3&-1&1 \end{bmatrix}$
		- $A = LU$






