---
layout: post
title: Archlinux install
description: >
    Install Archlinux
tags: [ArchLinux]
author: author1
---


> Archlinux安装过程中的一些问题，后续配置需要注意的一些事项，以及linux中遇到的一些问题

- [List](#head1)
- [Archlinux的安装](#head2)
- [显卡驱动](#head3)
- [独显下屏幕亮度调节](#head4)
- [boot空间不足（100M）](#head5)
- [选择kde](#head6)
- [v2ray代理](#head7)
- [pytorch的安装](#head8)
- [Arch install on removable media](#head9)


## <span id="head1">List</span>



## <span id="head2">Archlinux的安装</span>

可以看这一篇：https://zhuanlan.zhihu.com/p/138951848 （注意：建议wiki，安装细节有可能随着更新改变）

1. 制作好镜像

2. 启动后，联网，更新，安装vim

3. cfdisk分盘

4. mount挂载，在有windows的情况下，分的硬盘挂到/mnt上，把efi挂载到/mnt/boot上，然后按照wiki开始安装

    ```shell
    pacstrap /mnt base linux linux-firmware nano
    ```

5. 生成fstab文件

    ```shell
    genfstab -U /mnt >> /mnt/etc/fstab
    ```

6. 配置系统

7. 进入/mnt

   ```shell
   arch-root /mnt
   ```

8. 建议swap文件，用于休眠

   ```shell
   dd if=/dev/zero of=/swapfile bs=2048 count=1048576 status=progress
   chmod 600 /swapfile
   mkswap /swapfile
   swapon /swapfile
   vim /etc/fstab 在文件末尾输入 /swapfile none swap defaults 0 0
   ```

9. 设置时区

   ```shell
   timedatectl set-timezone Asia/Shanghai
   hwclock
   ```

10. 取消/etc/locale.gen文件中的en_US UTF-8和zh_CN UTF-8的注释

    ```shell
    locale-gen
    ```

    创建/etc/locale.cong, 输入LANG=en_US.UTF-8

    创建/etc/hostname  $name

11. 修改/etc/hosts

    ```shell
    127.0.0.1	localhost
    ::1			localhost
    127.0.1.1	$name.localdomain		$name
    ```

12. root用户密码passwd

13. ```shell
    pacman -S grub efibootmgr networkmanager network-manager-applet dialog wireless_tools wpa_supplicant os-prober mtools dosfstools ntfs-3g base-devel linux-headers reflector git sudo
    ```

    使用grub作为启动器
    安装intel-ucode或amd-ucode

14. 退出，取消挂载，重启,使用root账户登录

15. 登录后

    ```shell
    systemctl enable --now NetworkManager
    nmtui联网
    ```

16. 创建普通用户

    ```shell
    useradd -m -G wheel $user
    passwd $user
    EDITOR=vim visudo
    取消wheel ALL=(ALL) ALL的注释
    ```

    安装显卡驱动

    ```shell
    pacman -S nvidia nvidia-util
    pacman -S xf86-video-amdgpu
    ```

17. 安装

    ```shell
    pacman -S xorg
    ```

18. 桌面环境及后续

    ```shell
    pacman -S sddm
    pacman -S plasma packagekit-qt5 kate git kconsole
    ```

19. 添加archlinuxcn源

    ```shell
    [archlinuxcn]
    Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch
    并取消multilib的注释

    pacman -Syu && pacman -S archlinuxcn-keyring
    pacman -S ttf-sarasa-gothic noto-fonts-cjk
    ```

20. 重启

## <span id="head3">显卡驱动</span>

如果安装时使用核显，则后续怎么都转不了独显的驱动

所以建议直接从头到尾使用独显，驱动问题轻松解决

## <span id="head4">独显下屏幕亮度调节</span>

wiki Nvidia中

创建/etc/X11/xorg.conf.d/20-nvidia.conf 

```
Section "Device"
    Identifier   "Device0"
    Driver     "nvidia"
    VendorName   "NVIDIA Corporation"
    Option "RegistryDwords" "EnableBrightnessControl=1"
EndSection
```

然后更新grub

## <span id="head5">boot空间不足（100M）</span>

https://wusiyu.me/archlinux-remove-initramfs-linux-fallback-img/

删除fallback.img

然后在/etc/mkinitcpio.d/linux.preset中去掉fall back的部分

## <span id="head6">选择kde</span>

新的gnome十分难用，不建议使用

## <span id="head7">v2ray代理</span>

开启系统代理，命令行用proxychains

## <span id="head8">pytorch的安装</span>

2021-1-16  python3.10好像有点问题，安装不了torch

yay安装python39


## <span id="head9">Arch install on removable media</span>

安装同上，不同点在于安装bootloader

以grub举例：安装需要增加--removable选项，见wiki，refind同样需要选项

原理：对于普通的电脑安装，在grub安装时会将grubx64.efi这样的文件放到一个位置，也会写入到uefi的条目中，条目存在于主板的固件中。同时对于陌生设备想要直接启动，uefi会扫描每一个fat分区的/efi/boot/分区中的*.efi文件，如果有，在boot menu则会显示