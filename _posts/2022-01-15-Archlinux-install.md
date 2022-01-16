---

layout: post

title: Archlinux install

description: >

  Install Archlinux

tags: [ArchLinux]

author: author1

---



> Archlinux安装过程中的一些问题，后续配置需要注意的一些事项，以及linux中遇到的一些问题

* this unordered seed list will be replaced by toc as unordered list

{:toc}

#  Archlinux的安装

可以看这一篇：https://zhuanlan.zhihu.com/p/138951848  （注意：建议wiki，安装细节有可能随着更新改变）

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

   1. ```shell

      arch-root /mnt

      ```

   2. 建议swap文件，用于休眠

      ```shell

      dd if=/dev/zero of=/swapfile bs=2048 count=1048576 status=progress

      chmod 600 /swapfile

      mkswap /swapfile

      swapon /swapfile

      vim /etc/fstab 在文件末尾输入 /swapfile none swap defaults 0 0

      ```

   3. 设置时区

      ```shell

      timedatectl set-timezone Asia/Shanghai

      hwclock

      ```

   4. 取消/etc/locale.gen文件中的en_US UTF-8和zh_CN UTF-8的注释

      ```shell

      locale-gen

      ```

      创建/etc/locale.cong, 输入LANG=en_US.UTF-8

      创建/etc/hostname   $name

   5. 修改/etc/hosts

      ```shell

      127.0.0.1	localhost

      ::1			localhost

      127.0.1.1	$name.localdomain		$name

      ```

   6. root用户密码passwd

   7. ```shell

      pacman -S grub efibootmgr networkmanager network-manager-applet dialog wireless_tools wpa_supplicant os-prober mtools dosfstools ntfs-3g base-devel linux-headers reflector git sudo

      ```

      使用grub作为启动器

      安装intel-ucode或amd-ucode

   8. ```shell

      vim /etc/default/grub

      加一行 GRUB_DISABLE_OS_PROBER=false

      grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=Arch

      grub-mkconfig -o /boot/grub/grub.cfg

      ```

   9. 退出，取消挂载，重启,使用root账户登录

   10. ```shell

       systemctl enable --now NetworkManager

       nmtui联网

       ```

   11. ```shell

       useradd -m -G wheel $user

       passwd $user

       ```

       创建用户

       ```shell

       EDITOR=vim visudo

       取消wheel ALL=(ALL) ALL的注释

       ```

   12. 安装显卡驱动

       ```shell

       pacman -S nvidia nvidia-util

       pacman -S xf86-video-amdgpu

       ```

   13. ```shell

       pacman -S xorg

       ```

   14. 桌面环境及后续

       ```shell

       pacman -S sddm

       pacman -S plasma packagekit-qt5 kate git kconsole

       ```

   15. 添加archlinuxcn源

       ```shell

       [archlinuxcn]

       Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch

       并取消multilib的注释

       ```

       ```shell

       pacman -Syu && pacman -S archlinuxcn-keyring

       ```

       ```shell

       pacman -S ttf-sarasa-gothic noto-fonts-cjk

       ```

       重启

##  遇到的问题

###  显卡驱动

如果安装时使用核显，则后续怎么都转不了独显的驱动

所以建议直接从头到尾使用独显，驱动问题轻松解决

###  独显下屏幕亮度调节

wiki Nvidia中

创建/etc/X11/xorg.conf.d/20-nvidia.conf 

```

Section "Device"

        Identifier      "Device0"

        Driver          "nvidia"

        VendorName      "NVIDIA Corporation"

        Option "RegistryDwords" "EnableBrightnessControl=1"

EndSection

```

然后更新grub

###  boot空间不足（100M）

https://wusiyu.me/archlinux-remove-initramfs-linux-fallback-img/

删除fallback.img

然后在/etc/mkinitcpio.d/linux.preset中去掉fall back的部分

###  选择kde

新的gnome十分难用，不建议使用

###  v2ray代理

开启系统代理，命令行用proxychains

