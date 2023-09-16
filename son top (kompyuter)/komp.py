import random
print("1 dan 100 gacha son o'yladim topa olasizmi?")
a = int(input("Men o'ylagan son: "))
boshi = 1
ohiri = 100
n = 0
for i in range(1000):
    komp = random.randint(boshi, ohiri)
    n += 1
    javob = input(f"{komp} soni tengmi (t),"
                  f" soni kattami (k),"
                  f" soni kichikmi (c): ")
    if javob == "t":
        print(f"Siz {n} ta urinishda topdingiz")
        break
    elif javob == "k":
        ohiri = komp-1
    elif javob == "c":
        boshi =komp+1

