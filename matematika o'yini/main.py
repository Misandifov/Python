from matem import menu, oyin

while True:
    tanlov = menu()
    if tanlov == 1:
        oyin(daraja=10)
    elif tanlov == 2:
        oyin(daraja=100)
    elif tanlov == 3:
        oyin(daraja=1000)
    elif tanlov == 4:
        print("Chiqish")
    if input("O'yinni davom ettirasizmi? Xa(x): ") !="x":
        break