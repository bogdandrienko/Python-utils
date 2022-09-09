
list_compr1 = [i for i in [1, 2, 3, 4]]
print(list_compr1)

list_compr2 = [{f"key_{x}": x} for x in [1, 2, 3, 4] if x % 2 != 0]
print(list_compr2)

list_compr3 = []
for x in [1, 2, 3, 4]:
    if x % 2 != 0:
        list_compr3.append({f"key_{x}": x})
print(list_compr3)



list4 = []
for i in range(1, 10+1):
    if i % 2 == 0:
        list4.append(i)
print(list4)

print([i for i in range(1, 10+1) if i % 2 == 0])









fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
# print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
# print(newlist)

list1 = [" apple ", " banana ", " cherry ", "kiwi ", " mango"]
list2 = [str(char).strip() for char in list1 if "i" in char and len(str(char).strip()) > 3]
print(list2)

list3 = [str(x).strip() for x in "Яблоко, банан, груша       , киви      ".split(",")]
print(list3)