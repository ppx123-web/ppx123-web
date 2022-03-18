---
layout: post
title: Algorithm
description: >
    Algorithm Problem
tags: [Programming]
author: author1
---

> 刷题中遇到的算法的问题

- [欧拉回路问题](#head1)
- [字符串问题](#head2)
- [二分搜索](#head3)
- [DP](#head4)
	- [划分数组](#head5)


## <span id="head1">欧拉回路问题</span>

dfs进行搜索（）

```C++
ans是经过的节点的路径
void dfs(string cur) {
    for(for each edge from node cur) {
        if (this edge never uses) {
            dfs(nxt node);
            ans.push_back(it.first);
        }
    }
}
```

## <span id="head2">字符串问题</span>

马拉车算法

## <span id="head3">二分搜索</span>

```C++
while (begin < end) {
    int mid = (begin + end) / 2;
    int mid = (begin + end) >> 1;
}
```

注意以上两种写法的区别，直接除以2是向0取证，而>>1是向下取证，建议使用后者（当大于等于0时不所谓，但是当是负的单数时则产生区别。

二分搜索的用法

一种是在一个给定的有序列表中找到值是value的项

一种是在解空间搜索，每次判断当前是否满足要求的条件，根据判断的条件进行判断

## <span id="head4">DP</span>

### <span id="head5">划分数组</span>

求划分出来的最小数组的个数没事的每个数组的最左边的元素和最右边的元素最大公约数不为1

定义了数组dp[i]表示当前将质数i在最右侧加入数组后将数组划分的最小的数组个数

设当前遍历到数组的第i个位置，对于第i个数x，x有其质因子，将x加入数组划分后的结果一定是x单独一个数组或者x和之前的某个数及其之间的树构成一个数组，此时对于x的一个因子y，dp[y]记录了在i-1处加入y可以的划分，如果x不是单独一个划分构成一个数组，那么dp[y]即为x非单独一个数组构成合法划分的最小的数组个数。

```C++
#define MAXN 100005
int min_prime[MAXN],prime[MAXN],dp[MAXN];
int splitArray(vector<int>& nums) {
    int m = *max_element(nums.begin(),nums.end());
    int cnt = 0;
    for(int i=2; i<=m; i++){
        if(!min_prime[i]){
            min_prime[i] = i; // i 的最小质数是自己
            prime[++cnt] = i; // 记录质数 i
        }
        for(int j=1; j<=cnt && i*prime[j]<=m; j++){
            min_prime[i*prime[j]] = prime[j]; // 数 i*prime[j] 的最小质数是 prime[j]
            if(i % prime[j] == 0) break; // 欧拉筛的核心是让每一个合数被最小的质因数筛去, 所以这里必须break
        }
    }
    int ans;
    memset(dp,0x3f,sizeof(dp));
    for (auto it: nums) {
        int temp = INT32_MAX;
        while (it > 1) {
            int factor = min_prime[it];
            dp[factor] = min(dp[factor],ans + 1); //更新了it的因子
            temp = min(temp,dp[factor]);
            it = it / min_prime[it];
        }
        ans = temp;
    }
    return ans;
}
```
