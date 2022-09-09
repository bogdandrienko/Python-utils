ball = 4.8

if ball >= 5:
    print("Вы прошли экзамен")
else:
    if ball >= 4.5:
        print("Есть ещё одна попытка!")
    else:
        print("Вы провалили экзамен")

if ball >= 5:
    print("Вы прошли экзамен")
elif ball >= 4.5:
    print("Есть ещё одна попытка!")
elif ball >= 4.5:
    print("Есть ещё одна попытка!")
elif ball >= 4.5:
    print("Есть ещё одна попытка!")
elif ball >= 4.5:
    print("Есть ещё одна попытка!")
elif ball >= 4.5:
    print("Есть ещё одна попытка!")
elif ball >= 4.5:
    print("Есть ещё одна попытка!")
elif ball >= 4.5:
    print("Есть ещё одна попытка!")
else:
    print("Вы провалили экзамен")

svetofor = 'Жёлтый'
match svetofor:
    case "Красный":
        print("Стоять")
    case "Жёлтый":
        print("Готовьтесь")
    case "Зелёный":
        print("Можно идти")
    case _:
        print("Светофор сломался")

















#  if else, elif,  / switch case

# GO TO
val1 = 4

if val1 > 5:
    print("Правда")

if val1 >= 5:
    print("Правда")
else:
    print("Ложь")

if val1 >= 5:
    print("Правда")
elif val1 >= 0:
    print("Ложь")
else:
    print("Число отрицательное!")

fruit = "абрикос"

if fruit == "абрикос":
    print("У Вас аллергия, будьте осторожны")
elif fruit == "банан":
    print("Всё в норме")
else:
    print("Неизвестный фрукт")

# if fruit == "абрикос":
#     print("У Вас аллергия, будьте осторожны")
# else:
#     if fruit == "банан":
#         print("Всё в норме")
#     else:
#         print("Неизвестный фрукт")

match fruit:
    case "абрикос":
        print("У Вас аллергия, будьте осторожны")
    case "банан":
        print("Всё в норме")
    case _:
        print("Неизвестный фрукт")