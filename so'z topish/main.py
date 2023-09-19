import random
import os
sozlar = ["olma","nok","qovun","tarvuz","piyoz","sholg'om","oshqovoq"]
soz = random.choice(sozlar)
soz = soz.lower()

urinish = 5
kiritilgan_harflar = []
xabar = ""
while True:
    os.system('cls')
    yashirin_soz = ""
    for h in soz:
        if h in kiritilgan_harflar:
            yashirin_soz += h
        else:
            yashirin_soz += "*"
    print(yashirin_soz)
    print(f"Urinishlar soni: {urinish} ta")
    print(xabar)
    if urinish == 0:
        print("Siz yutqazdingiz")
        break
    elif "*" not  in yashirin_soz:
        print("Siz g'olib bo'ldingiz")
        break
    harf = input("Harf kiriting: ").lower()
    if harf in kiritilgan_harflar:
        xabar = f"Siz {harf} harfini kiritib bo'lgansiz"
    elif harf in soz:
        xabar = f"{harf} harfi so'zda bor"
        kiritilgan_harflar.append(harf)
    else:
        xabar = f"{harf} harfi so'zda yo'q"
        urinish -=1
input("Chiqish uchun entirni bosing")

