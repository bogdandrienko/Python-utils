
#for i in range(1, 10): # [1, 2, 3, ... 10]

for item in [1, 2, 3, 4]:
    print(item)

print("\n")

for item in (1, 2, 3, 4):
    print(item)

print("\n")
for item in {1, 2, 3, 4}:
    print(item)

print("\n")
dict1 = {"key1": 1, "key2": 2}
for item in dict1:
    print(dict1[item])
print("\n")
for item in {"key1": 1, "key2": 2}.values():
    print(item)
print("\n")
for item in {"key1": 1, "key2": 2}.keys():
    print(item)
print("\n")
for key, value in {"key1": 1, "key2": 2}.items():
    print(key, value)
print("\n")



for i in range(1, 10):
    if i <= 3:
        continue  # пропускает эту итерацию
    elif i >= 7:
        break  # останавливает цикл
    print(i)

print("\n")

# index = 0
# while(index <= 7):
#     index = index + 1
#     print(index)


i = 0
while True:
    i = i + 1
    if i <= 3:
        continue  # пропускает эту итерацию
    elif i >= 7:
        break  # останавливает цикл
    print(i)









class CycleClass:
    class Example:
        @staticmethod
        def example_cycle_for():
            for i in range(1, 10):
                print(i)

        @staticmethod
        def example_cycle_while():
            sec = 10
            while sec < 50:
                sec += 1
                print(sec)