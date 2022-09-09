int1 = 10  # int()
float1 = 10.0  # float()
str1 = "Python"  # str()
bool1 = True  # bool()

print(type(int1))
# print(input("Введите: "))

list1 = [13, 15, 13]  # список - множество элементов
list1[0] = 12
set1 = {1, 2}  # множество уникальных элементов
tuple1 = (1, 2,)  # кортеж множество неизменяемых
tuple2 = (10, *tuple1[1:])  # (10, 2, 23)  # способ перезаписать кортеж


def clear_copy(arr: list) -> list:
    return list(set(arr))


print(list1)
print(set(list1))


str2 = "Меруерт"
# str2[3] = "J"
print()


dict1 = {"key_1": "va1", (10,): {"key1": "va1"}}  # ключом словаря может быть только неизменяемый тип данных
# (хэшируемый), т.е. он проходит через хэш функцию и генерирует уникальную комбинацию символов
# "контейнерные" типы данных могут быть ключом словаря, только при условии, что всё внутри хэшируемое
print(dict1["key_1"])
dict1["key_3"] = 666
print(dict1)
# print(hash("Python"))







class TypeVariablesClass:
    @staticmethod
    def example_get_type_of_variable(variable):
        return type(variable)

    @staticmethod
    def example_check_type_of_variable(variable, type_variable: str):
        if type_variable == 'bool':
            if isinstance(variable, bool):
                return True
            else:
                return False
        elif type_variable == 'int':
            if isinstance(variable, int):
                return True
            else:
                return False
        elif type_variable == 'float':
            if isinstance(variable, float):
                return True
            else:
                return False
        elif type_variable == 'str' or type_variable == 'string':
            if isinstance(variable, str):
                return True
            else:
                return False
        elif type_variable == 'list':
            if isinstance(variable, list):
                return True
            else:
                return False
        elif type_variable == 'dict' or type_variable == 'dictionary':
            if isinstance(variable, dict):
                return True
            else:
                return False
        elif type_variable == 'tuple':
            if isinstance(variable, tuple):
                return True
            else:
                return False
        elif type_variable == 'set':
            if isinstance(variable, set):
                return True
            else:
                return False
        else:
            return None

    class Example:
        @staticmethod
        def example_get_type():
            value = TypeVariablesClass.example_get_type_of_variable(variable=12.5)
            print(value)

        @staticmethod
        def example_check_type():
            value = TypeVariablesClass.example_check_type_of_variable(variable=12.5, type_variable='int')
            print(value)


#########################################################################################


class DictionaryClass:
    @staticmethod
    def get_all_keys(dictionary: dict):
        return dictionary.keys()

    @staticmethod
    def get_all_values(dictionary: dict):
        return dictionary.values()

    @staticmethod
    def get_all_sources(dictionary: dict, values: dict):
        dictionary_local = dictionary.copy()
        for key, value in values.items():
            dictionary_local[key] = value
        return dictionary_local
