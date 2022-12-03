---
layout: post
title: Software Foundations
description: >
    Reading
tags: [Courses]
author: author1
---

> list of book reading

# Volume 1--logic

## Configuration in Win 10

coq 8.15 has a noisy output. Vscode with extension VScoq works well.(Setting path is enough.)

## Compile

Usage: coqc file.v -o _CoqProject

_CoqProject是默认的编译文件夹

## Poly -- Another definition of nat

```coq
Definition nat := forall X : Type, (X -> X ) -> X -> X.

Definition zero : nat := fun (X : Type) (f : X -> X) (x : X) => x.

Definition one : nat := fun (X : Type) (f : X -> X) (x : X) => f x.

Definition succ (n : nat) : nat := 
fun (X : Type) (f : X -> X) (x : X) => f(n X f x).

Definition plus (n m : nat) : nat := 
fun (X : Type) (f : X -> X) (x : X) => n X f (m X f x).

Definition mult (n m : nat) : nat :=
fun (X : Type) (f : X -> X) (x : X) => n X (m X f) x.
    
Definition exp (n m : nat) : nat :=
fun (X : Type) (f : X -> X) (x : X) => m (X -> X) (n X)  f x.

```

在exp中，需要注意函数式编程中的运算符或构造符的结合顺序，将$X->X$作为新的Type，以得到的函数作为输入，最后结合x.
