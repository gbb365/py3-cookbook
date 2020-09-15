#! /usr/bin/env python  
# -*- coding:utf-8 -*-  
# 将序列分解为单独的变量
p = (4,5)
x,y = p
print(x,y)

print('------')
data = ['ABCD',50,91,(2012,12,12)]
name,shares,price,(year,month,day) = data

print(name)
print(shares)
print(price)
print(year)

print('-----')
record = ('Dave','data@qq.com','112233','12212')
name,email,*phone_numbers = record
print(name)
print(email)
print(phone_numbers[0])