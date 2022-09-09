# file = open('new.txt', 'w')
# file.write("Python is awesome!123")
# file.close()

with open('new.txt', 'r') as file:  # a w r rb wb
    raw1 = r"""\nwefw""sef'"""
    bytes1 = b'wefwsef'
    line1 = file.read()
    print(line1)

import json


# with open('new.json', 'w') as file:
#     json.dump({"name": "Kvwefwefok"}, file)

with open('new.json', 'r') as file:
    dict2 = json.load(file)
    print(dict2)













class FileReadWriteClass:
    @staticmethod
    def write_to_file(file_name, text_file, mode='a'):
        with open(file_name, mode=mode) as file:
            file.write(text_file)

    @staticmethod
    def read_from_file_lines(file_name, mode='r'):
        with open(file_name, mode=mode) as file:
            return file.readlines()

    @staticmethod
    def read_from_file(file_name, mode='r'):
        with open(file_name, mode=mode) as file:
            return file.read()

    @staticmethod
    def example_write_to_file_add():
        FileReadWriteClass.write_to_file(file_name='file.txt', text_file='text\n', mode='a')

    @staticmethod
    def example_write_to_file_rewrite():
        FileReadWriteClass.write_to_file(file_name='file.txt', text_file='text\n', mode='w')

    @staticmethod
    def example_read_from_file_lines():
        print(FileReadWriteClass.read_from_file_lines(file_name='file.txt', mode='r'))

    @staticmethod
    def example_read_from_file():
        print(FileReadWriteClass.read_from_file(file_name='file.txt', mode='r'))
        
#############################################################################################