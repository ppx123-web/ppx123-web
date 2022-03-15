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
