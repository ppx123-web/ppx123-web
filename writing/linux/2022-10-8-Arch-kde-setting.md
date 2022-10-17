---
layout: post
title: Archlinux and KDE Configuration
description: >
    Configurations
tags: [ArchLinux]
author: author1
---

## List


## 蓝牙设置

```shell
sudo pacman -S bluez bluze-utils
sudo systemctl start bluetooth.service
sudo systemctl enable bluetooth.service
```

### 双系统蓝牙需要重新配对的问题

#### 修改linux

1. 下载[psexec](https://learn.microsoft.com/en-us/sysinternals/downloads/psexec)
2. 管理员权限运行`psexec.exe -si regedit`
3. 在注册表找到`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\BTHPORT\Parameters\Keys\`下面的第一个数字文件夹对应电脑蓝牙的MAC，文件夹中对应的数字文件夹对应连接设备的蓝牙。将信息导出或记录。
4. 重启，进入linux
5. 以root用户进入`/var/lib/bluetooth/MAC1/MAC2`，MAC1是电脑蓝牙的MAC，MAC2是与linux连接的MAC（可能同一个设备与windows的不一致）。
6. 将路径下info文件的`[LinkKey]Key=0551D38262254770124F68E18CB100E9
`进行替换（使用LTK），再更改文件夹名为windows下记下的MAC
7. `reboot` !!!

#### 修改windows (推荐)

1. 同上记录LTK和蓝牙设备MAC
2. 进入注册表，将`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\BTHPORT\Parameters\Keys\MAC1`的右侧文件，修改名称为记下的MAC，值为记下的Key。
3. Connect

## konsole 快捷键

Tab：自动补全。

Ctrl-b：向前移动，相当于(Left)。

Ctrl-f：向后移动，相当于(Right)。

Alt-b：按词向前移动。

Alt-f：按词向后移动。

Ctrl-a：移动到句首。相当于(HOME)键。

Ctrl-e：移动到句尾。相当于(END)键。

Ctrl-x：连续按两下的话，首尾交替。

Ctrl-h：删除光标前一个字符，相当于(Backspace)键。

Ctrl-d：删除光标后一个字符，相当于(Delete)键。

Ctrl-w：删除光标所指的一个单词。

Ctrl-u：删除光标前的所有字符。

Ctrl-k：删除光标后的所有字符。

Ctrl-l：清理屏幕，相当与「clear」命令。


