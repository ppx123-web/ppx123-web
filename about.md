---
layout: about
title: About
description: >
  How to use and test
menu: true
order: 3
---

# About

## 本地测试

因路径问题，本地不能显示图片

```shell
gem install jekyll bundler
bundler install
bundler add webrick
bundle exec jekyll serve
```

## List管理

```
Directory: _featured_tags
```

在文件夹中添加文件，头部格式

```
---
layout: list
title: [content]
slug: [tag] #用于链接到该list的文件
menu: true
order: num
description: >
  content
accent_color: '#268bd2'
accent_image:
  background: '#202020'
  overlay:    false
---
```

## Post管理

```
Direcoty: _posts
```

在文件夹中添加文件，头部格式如下

```
---
layout: post
title: Content
description: >
  Content
tags: [tag] #对应上面的tag
author: zcy
---
```

