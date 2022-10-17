---
layout: post
title: 高级算法作业
description: >
 高级算法作业
tags: [Courses]
author: author1
---

> 高级算法第三次作业

## 第一题

### (1)

显然当$a\in A\wedge a\in B\Rightarrow$，这样的位置$F_C$和$A\cap B$的bloom filters是一样的。

当$a\in A\wedge a\notin B$时，只要$\exists b\in B\wedge b\notin A,\exists i,j,1\leq i,j\leq k,s.t.\quad h_j(b)=h_i(a)$，且对于$A\cap B$中的元素没有哈希到$h_j(b)$这个位置，则$A\cap B$的bloom filters至少有一位和$F_A\wedge F_B$不同

### (2)

记$a_i,b_i$分别是A和B的bloom filters产生的m个bit的第i位,a,b为A,B中元素

$相同的bit数 = \sum\limits_{i=1}^m I(a_i=b_i) \Rightarrow E[same]=\sum\limits_{i=1}^mPr[a_i=b_i]

$

$E[differ] = n - E[same]$

$Pr[a_i=b_i] = Pr[\exists p,q,h_p(a)=i\wedge h_q(b) = i] + Pr[\forall p,q,h_p(a)\neq i \wedge h_q(b)\neq i]$

$Pr[\exists p,q,h_p(a)=i\wedge h_q(b) = i]\\

= Pr[\exists p,q,h_p(a)=i\wedge h_q(b)=i\|a=b]Pr[a=b] + Pr[\exists p,q,h_p(a)\wedge h_q(b)=i\|a\neq b]Pr[a\neq b]\\

=(1-(1-\dfrac{1}{m})^k)\dfrac{\|A\cap B\|}{n^2} + (1-(1-\dfrac{1}{m})^k-(1-\dfrac{1}{m})^k+(1-\dfrac{1}{m})^{2k})(1-\dfrac{\|A\cap B\|}{n^2})$

$Pr[\forall p,q,h_p(a)\neq i \wedge h_q(b)\neq i]\\

=Pr[\forall p,q,h_p(a)\neq i \wedge h_q(b)\neq i \| a\neq b]Pr[a\neq b]+Pr[\forall p,q,h_p(a)\neq i \wedge h_q(b)\neq i\|a\neq b]Pr[a\neq b]\\

=(1-\dfrac{1}{m})^k\dfrac{\|A\cap B\|}{n^2}+(1-\dfrac{1}{m})^{2k}(1-\dfrac{\|A\cap B\|}{n^2})$

$Pr[a_i=b_i] = 2((1-\dfrac{1}{m})^k-(1-\dfrac{1}{m})^{2k})\dfrac{\\|A\cap B\\|}{n^2}+1-2(1-\dfrac{1}{m})^k+2(1-\dfrac{1}{m})^{2k}$

$E[differ] = n - n(2((1-\dfrac{1}{m})^k-(1-\dfrac{1}{m})^{2k})\dfrac{\\|A\cap B\\|}{n^2}+1-2(1-\dfrac{1}{m})^k+2(1-\dfrac{1}{m})^{2k})$

## 第二题

对于$\dfrac{n}{2}$个球,uniformly at random的期望为$\Theta(\dfrac{\log \dfrac{n}{2}}{\log\log\dfrac{n}{2}})$,two choice $\dfrac{n}{2}$的期望为$\Theta(\log\log \dfrac{n}{2})$，当某一半是uniformly at random的时候，期望则为uniformly at random的期望，因为 $\log\log\dfrac{n}{2} = o(\dfrac{\log \dfrac{n}{2}}{\log\log\dfrac{n}{2}}))$


### (1)

前一半随机选择仍为$\Theta(\dfrac{\log n/2}{\log\log\dfrac{n}{2}})=\Theta(\dfrac{\log }{\log\log n})$

### (2)

$\Theta(\dfrac{\log \dfrac{n}{2}}{\log\log\dfrac{n}{2}}) + \Theta(\log\log \dfrac{n}{2}) = \Theta(\dfrac{\log \dfrac{n}{2}}{\log\log\dfrac{n}{2}}) = \Theta(\dfrac{\log }{\log\log n})$

### (3)

将一个随机选取和two choice视为一个操作，共有$\dfrac{n}{2}$个操作，记第i个盒子的球的个数为$X_i$

$Pr[\max\limits_{1\leq i\leq n} X_i \geq L] \leq nPr[X_1\geq L]$

$Pr[X_i \geq L] \leq \sum\limits_{i=0}^{L}\tbinom{m/2}{i}\dfrac{1}{n^i}\tbinom{m/2}{L-i}(1-(1-\dfrac{1}{n})(1-\dfrac{1}{n}))^{L-i})\\(至少i个uniform的操作选择第一个bin，至少L-i个two choice中有一个选择了第一个bins)\\

\leq \sum\limits_{i=0}^{L}\tbinom{m/2}{i}\tbinom{m/2}{L-i}\dfrac{1}{n^i}(\dfrac{2}{n})^{L-i}\\

= 2\tbinom{m}{L}\dfrac{1}{n^L} (范德蒙德卷积,此时情形和上课讲的一样，略去细节)\\

\leq 2\dfrac{m^L}{L!n^L}\\

\leq 2\dfrac{e^Lm^L}{L^Ln^L}$

当$m=\Theta(n)$时有$存在c，L=\dfrac{c\log n}{\log\log n}$

$Pr[X_i\geq L] \leq (\dfrac{e}{L})^L\leq \dfrac{1}{n^2}$

所以最大值大于L的概率为$Pr[\max X_i \geq L] \leq \dfrac{1}{n},L=\dfrac{c\log n}{\log\log n}$

下界显然是随机选取$\dfrac{n}{2}$的下界$\Theta(\dfrac{\log \dfrac{n}{2}}{\log\log\dfrac{n}{2}}) = \Theta(\dfrac{\log n}{\log\log n})$，所以结果仍为$L=\Theta(\dfrac{\log n}{\log\log n})$

## 第三题

设$Y_i=I[(1-\epsilon)Z\leq \hat{Z_i}\leq (1+\epsilon)Z]$,$E[Y_i]\geq \dfrac{3}{4}$

$Y=\sum\limits_{i=1}^sY_i,\mu = E[Y]\geq \dfrac{3}{4}s$

当$Y\geq \dfrac{1}{2}s$时，$\{\hat{Z_i}\}$的中位数X一定满足$(1-\epsilon)Z\leq X\leq (1+\epsilon)Z$

所以只要$Pr[(1-\epsilon)Z\leq X\leq (1+\epsilon)Z]\geq Pr[Y\geq \dfrac{1}{2}s]\geq 1-\delta$,即$\delta\geq Pr[Y\leq \dfrac{1}{2}s]$

只要$Pr[Y\leq \dfrac{1}{2}s]\leq Pr[\sum\limits_{i=1}^sT_i\leq (1-\dfrac{1}{3})\mu]\leq e^{-\dfrac{\mu/9}{2}}(chernoff bound)\leq e^{-\dfrac{s}{24}}$

即$e^{-\dfrac{s}{24}\leq \delta}\Rightarrow S\geq 24\ln \dfrac{1}{\delta},S=\Omega(\log \dfrac{1}{\delta})$

## 第四题

### (1)

$Pr[\\|X\\|\geq \delta]\leq \dfrac{\sum\limits_{k=1}^{+\infty}\dfrac{t^k}{k!}E[\\|X\\|^k]}{\sum\limits_{k=1}^{+\infty}\dfrac{t^k}{k!}\delta^k}$

记$a_k = \dfrac{t^k}{k!}E[\\|X\\|^k],b_k = \dfrac{t^k}{k!}\delta^k$

$m=\mathop{argmin}\limits_{k}\dfrac{a_k}{b_k},c = \dfrac{a_k}{b_k}$

$\forall i\in N,\dfrac{a_i}{b_i}\geq c\Rightarrow a_i\geq cb_i$

得到$\dfrac{\sum\limits_{k=1}^{+\infty}\dfrac{t^k}{k!}E[\

\|X\\|^k]}{\sum\limits_{k=1}^{+\infty}\dfrac{t^k}{k!}\delta^k} \geq \dfrac{\sum\limits_{i=1}^{+\infty}cb_i}{\sum\limits_{i=1}^{+\infty}b_i}= c = \dfrac{a_m}{b_m}=\dfrac{E[\\|X\\|^k]}{\delta^k}$

所以一定存在k阶矩强于chernoff bound

### (2)

矩阵生成函数容易计算，而特定的k阶矩难以找到

## 第五题

### (1)

记$h_k=\prod\limits_{i=1}^{k}f_i(X_i)$，显然$h_k$不减

$E[h_n]=E[h_{n-1}\cdot f_n(X_n)]\leq E[h_{n-1}]E[f_n(X_n)]]\leq ......\leq \prod\limits_{i=1}^{k}E[f_i(x_i)]$

### (2)

$X=\sum\limits_{i=1}^nX_i,E[x]=\mu$

$Pr[X\geq (1+\delta)\mu]\leq Pr[e^{\lambda X}\geq e^{(1+\delta)\mu\lambda}]\leq \dfrac{E[e^{\lambda X}]}{e^{\lambda(1+\delta)\mu}}\leq \dfrac{\prod\limits_{i=1}^nE[e^{\lambda X_i}]}{e^{\lambda(1+\delta)\mu}}$,其余和独立的情形一致，$Pr[X\geq (1+\delta)\mu]\leq \dfrac{e^{(e^{(\lambda-1)\mu})}}{e^{\lambda(1+\delta)\mu}}$

$Pr[X\leq (1-\delta)\mu]\leq Pr[e^{\lambda X}\geq e^{(1-\delta)\mu\lambda}]\leq \dfrac{E[e^{\lambda X}]}{e^{\lambda(1-\delta)\mu}},(\lambda < 0)$,应用后面提到的性质，$X_i$是负相关的$f=e^{\lambda X_i},\lambda < 0$单调递减，满足性质Disjoint monotone aggregation，有$E[e^{\lambda X}]\leq \prod\limits_{i=1}^nE[e^{\lambda X_i}]$,则$Pr[X\leq (1-\delta)\mu]\leq \dfrac{\prod\limits_{i=1}^nE[e^{\lambda X_i}]}{e^{\lambda(1-\delta)\mu}}$,其余和独立的情形一致，$Pr[X\leq (1-\delta)\mu]\leq \dfrac{e^{(e^{(\lambda-1)\mu})}}{e^{\lambda(1-\delta)\mu}}$

Qed.

### (3)

记$p=\\|I\\|,q=\\|J\\|$,记$X_i\in I,X_{i_1},X_{i_2},...,X_{i_p}$,记$X_j\in J,X_{j_1},X_{j_2},...,X_{j_q}$.$I$和$J$对应将$B_{i,k}$划分后的集合

注意到$\sum\limits_{i=1}^nB_{i,k}=1$有且仅有一个为1.

当$X_{i_m}=1$时，其余$X_{i_k},X_{j_k},k\neq m$均为0.

记$f(X_i,i\in I)$为$f_m，其中X_{i_m}=1,f_0表示X_{i_k}均为0,\forall 1\leq k\leq p$，

同理有$g_m$的定义,记$f(X_j,j\in J)$为$g_m，其中X_{j_m}=1,g_0表示X_{j_k}均为0,\forall 1\leq k\leq q$.

记$A=\sum\limits_{m=1}^{\\|I\\|}f_m,B=\sum\limits_{m=1}^{\\|J\\|}g_m$

$S_1 = E[f(X_i,i\in I)g(X_j,j\in J)] = \dfrac{1}{n}g_0A+\dfrac{1}{n}f_0B+\dfrac{n-\\|I\\|-\\|J\\|}{n}f_0g_0$

$S_2=E[f(X_i)]E[g(X_j)]=(\dfrac{1}{n}A+(1-\dfrac{p}{n})f_0)(\dfrac{1}{n}B+(1-\dfrac{q}{n})f_0)\\

=\dfrac{1}{n^2}AB+\dfrac{1}{n}g_0A-\dfrac{q}{n^2}g_0A+\dfrac{1}{n}f_0B-\dfrac{p}{n^2}f_0B+f_0g_0(\dfrac{n-p-q}{n}+\dfrac{pq}{n^2})\\

=S_1 + \dfrac{1}{n^2}(AB-qg_0A-pf_0B+pqf_0g_0)\\

=S_1+\dfrac{1}{n^2}(A-pf_0)(B-qg_0)$

由于$f$是非减函数，所以$\dfrac{1}{n^2}(A-pf_0)(B-qg_0) \geq 0\Rightarrow S_1\leq S_2$,Qed.



