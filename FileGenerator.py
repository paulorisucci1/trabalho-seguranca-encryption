import os

MEGA_BYTE = 10


class FileGenerator:
    def __init__(self, input_name):
        self.__file_path = input_name

    @property
    def input_file_name(self):
        return self.__file_path


    def get_file_content(self):

        text_file = open(self.__file_path, 'r')
        file_content = text_file.read()
        text_file.close()

        return file_content

    def get_file_content_binary(self):

        text_file = open(self.__file_path, 'rb')
        file_content = text_file.read()
        text_file.close()

        return file_content

    def overwrite_content(self, content):
        text_file = open(self.__file_path, 'w')
        text_file.write(content)
        text_file.close()

    def overwrite_content_binary(self, content):
        text_file = open(self.__file_path, 'wb')
        text_file.write(content)
        text_file.close()

if __name__ == '__main__':
    print(os.path.getsize('./teste.txt'))