---
创建时间: 2026-02-14
更新时间: 2026-08-29
页面类型: 1
更新次数: 3
准确率: 100
完整度: 90
阅读状态: 0
---
##### QR 分解
- QR 分解
	- **QR 分解**是一种[[矩阵因式分解]], 记作 $A = QR$, 指[[矩阵]] $A$ 分解为[[正交矩阵]]或[[酉矩阵]] $Q$ 和[[三角矩阵|上三角矩阵]] $R$. 设矩阵 $A \in \mathbb{F}^{m \times n}$ 且 $m \ge n$, 则 QR 分解主要分为完全 QR 分解和简化 QR 分解. 在完全 QR 分解中, 矩阵 $Q \in \mathbb{F}^{m \times m}$ 是正交矩阵或酉矩阵, 列向量组构成目标空间 $\mathbb{F}^m$ 的标准正交基, 矩阵 $R \in \mathbb{F}^{m \times n}$ 是矩形上三角矩阵, 底部 $m-n$ 行为零. 在简化 QR 分解中, 矩阵 $Q \in \mathbb{F}^{m \times n}$ 仅满足列正交性, 列向量组构成列空间 $\text{Col}(A)$ 的标准正交基, 矩阵 $R \in \mathbb{F}^{n \times n}$ 是可逆上三角矩阵. QR 分解的代数本质是[[格拉姆-施密特方法|格拉姆-施密特正交化]]的矩阵表达. 通过构造列空间的标准正交基组成 $Q$, 结合正交性由 $Q^HA=R$ 或 $Q^TA=R$ 计算矩阵 $R$. 任意矩阵均存在 QR 分解. 当且仅当 $A$ 为[[矩阵的秩|列满秩]]且限定 $R$ 的主对角线元素全为正数 $r_{ii} > 0$ 时, 简化 QR 分解存在且唯一. 只有当 $A$ 是满秩方阵且限定 $R$ 对角线全正时, 完全 QR 分解唯一. 数值计算中常用豪斯霍尔德变换或吉文斯旋转以获得更稳定的分解
		- $A = QR = \begin{bmatrix} \mathbf{q}_1 & \cdots & \mathbf{q}_n & \cdots & \mathbf{q}_m \end{bmatrix} \begin{bmatrix} r_{11} & r_{12} & \cdots & r_{1n} \\ 0 & r_{22} & \cdots & r_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & r_{nn} \\ \hline 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 0 \end{bmatrix}$
		- $A = QR = \begin{bmatrix} \mathbf{q}_1 & \mathbf{q}_2 & \cdots & \mathbf{q}_n \end{bmatrix} \begin{bmatrix} r_{11} & r_{12} & \cdots & r_{1n} \\ 0 & r_{22} & \cdots & r_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & r_{nn} \end{bmatrix}$


>[!example]- QR 分解
> - 目标矩阵
> 	- $A = \begin{bmatrix}0&3&1\\0&4&-2\\2&1&1 \end{bmatrix}$
> - 格拉姆-施密特方法
> 	- $\mathbf{v_1}=(0,0,1)$
> 	- $\mathbf{v_2}=(0.6,0.8,0)$
> 	- $\mathbf{v_3}=(0.8,-0.6,0)$
> - 构造矩阵
> 	- $Q=\begin{bmatrix}0&0.6&0.8\\0&0.8&-0.6\\1&0&0 \end{bmatrix}$
> 	- $R=Q^TA=\begin{bmatrix}2&1&1\\0&5&-1\\0&0&2\end{bmatrix}$
> - 最终结果
> 	- $\begin{bmatrix}0&3&1\\0&4&-2\\2&1&1 \end{bmatrix}=\begin{bmatrix}0&0.6&0.8\\0&0.8&-0.6\\1&0&0 \end{bmatrix}\begin{bmatrix}2&1&1\\0&5&-1\\0&0&2\end{bmatrix}$

