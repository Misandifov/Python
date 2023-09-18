import random

x = random.randint(1, 22)
n = 0
for i in range(1000000):
    son = int(input("Sonni kiriting: "))
    n += 1
    if x == son:
        print(f"Siz {n} ta urinishda topdingiz")
        break
    elif x > son:
        print(f"Siz kiritgan son berilgan sondan kichik")
    else:
        print(f"Siz kiritgan son berilgan sondan katta")
