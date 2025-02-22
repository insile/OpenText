##### QR分解
- QR分解
	- **QR分解**指[[方阵]] $A$ 分解为[[正交矩阵]]或者[[酉矩阵]] $Q$ 和[[三角矩阵|上三角矩阵]] $R$, 即 $A = LU$. 若 $A$ [[矩阵的秩|列满秩]], 则可QR分解, 首先通过[[格拉姆-施密特方法]]求 $A$ [[列空间]]的[[正交基|标准正交基]]组成 $Q$ , 然后通过 $A = QR\rightarrow Q^*A=Q^*QR=IR=R$ 求出$R$
- $A = QR$
	- $A_{n\times n}$ 方阵
	- $Q_{n\times n}$ 正交矩阵或者酉矩阵, $Q$ 的列向量组是 $A$ 列空间的标准正交基
	- $R_{n\times n}$ 上三角矩阵, $R$ 是可逆矩阵且在对角线上的元素为正数

>[!example]- $\begin{bmatrix}0&3&1\\0&4&-2\\2&1&1 \end{bmatrix}=\begin{bmatrix}0&0.6&0.8\\0&0.8&-0.6\\1&0&0 \end{bmatrix}\begin{bmatrix}2&1&1\\0&5&-1\\0&0&2\end{bmatrix}$
> - 格拉姆-施密特方法并单位化
> 	- $\mathbf{v_1}=(0,0,1)$
> 	- $\mathbf{v_2}=(0.6,0.8,0)$
> 	- $\mathbf{v_3}=(0.8,-0.6,0)$
> - $Q=\begin{bmatrix}0&0.6&0.8\\0&0.8&-0.6\\1&0&0 \end{bmatrix}$
> - $R=Q^*A=\begin{bmatrix}2&1&1\\0&5&-1\\0&0&2\end{bmatrix}$



