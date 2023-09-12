import random
# Quduq <- Qaychi, Qog'oz <- Quduq, Qaychi <- Qog'oz kompyuter
# Qaychi -> Quduq, Quduq -> Qog'oz, Qog'oz -> Qaychi foydalanuvchi
# Qaychi = Qaychi, Quduq = Quduq, Qog'oz = Qog'oz Durrang
foy = 0
kom = 0
dur = 0
variant = {1:'Quduq',2:'Qaychi',3:'Qog\'oz'}
for i in range(10):
    k = random.choice(list(variant.keys()))
    f = int(input(f"Bittasini tanlang: {variant}\n"))
    if k == 1 and f == 2 or k == 3 and f == 1 or k == 2 and f == 3:
        print("Kompyuter yutdi")
        kom += 1
    elif k == f:
        print("Durrang")
        dur += 1
    else:
        print("Siz yutdingiz")
        foy +=1
    print(f"(Kompyuter) {variant.get(k)}:{variant.get(f)} (Foydalanuvchi)")
print(f"Hisob: (Kompyuter) {kom}:{foy} (Foydalanuvchi)\nDurranglar soni: {dur}")

