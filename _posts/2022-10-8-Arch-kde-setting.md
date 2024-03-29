---
layout: post
title: Archlinux and KDE Configuration
description: >
    Configurations
tags: [ArchLinux]
author: author1
---


- [List](#head1)
- [蓝牙设置](#head2)
	- [双系统蓝牙需要重新配对的问题](#head3)
		- [修改linux](#head4)
		- [修改windows (推荐)](#head5)

## <span id="head1">List</span>


## <span id="head2">蓝牙设置</span>

```shell
sudo pacman -S bluez bluze-utils
sudo systemctl start bluetooth.service
sudo systemctl enable bluetooth.service
```

### <span id="head3">双系统蓝牙需要重新配对的问题</span>

#### <span id="head4">修改linux</span>

1. 下载[psexec](https://learn.microsoft.com/en-us/sysinternals/downloads/psexec)
2. 管理员权限运行`psexec.exe -si regedit`
3. 在注册表找到`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\BTHPORT\Parameters\Keys\`下面的第一个数字文件夹对应电脑蓝牙的MAC，文件夹中对应的数字文件夹对应连接设备的蓝牙。将信息导出或记录。
4. 重启，进入linux
5. 以root用户进入`/var/lib/bluetooth/MAC1/MAC2`，MAC1是电脑蓝牙的MAC，MAC2是与linux连接的MAC（可能同一个设备与windows的不一致）。
6. 将路径下info文件的`[LinkKey]Key=0551D38262254770124F68E18CB100E9
`进行替换（使用LTK），再更改文件夹名为windows下记下的MAC
7. `reboot` !!!

#### <span id="head5">修改windows (推荐)</span>

1. 同上记录LTK和蓝牙设备MAC
2. 进入注册表，将`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\BTHPORT\Parameters\Keys\MAC1`的右侧文件，修改名称为记下的MAC，值为记下的Key。
3. Connect


