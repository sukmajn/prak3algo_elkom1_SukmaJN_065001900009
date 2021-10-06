# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 09:37:51 2021

@author: Sukma Julia Nada
"""

a,b = (
    int(input('Masukkan angka awal: ')),
    int(input('Masukkan angka terakhir: '))
)

#i = a
while (a and a <= b):
    print (a,b)
    a += 1
    b -= 1