# -*- coding: utf-8 -*-
with open("deneme.txt") as f:
    okunacak=10
    icerik=f.read(10)
    while len(icerik)>0:
        print(icerik,end="")
        icerik=f.read(okunacak)