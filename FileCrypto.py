import fernet
from cryptography.fernet import Fernet
from numpy import byte
import rsa

from FileGenerator import FileGenerator

MEGA_BYTE = 1024 * 1024
KEY_SIZE = 256
FERNET_KEY_SIZE = 128

class FileCrypto:

    def __init__(self, file_name, encrypt_name, out_file_name):
        self.__pubkey, self.__privkey = rsa.newkeys(KEY_SIZE)
        self.__input = FileGenerator(file_name)
        self.__encrypt = FileGenerator(encrypt_name)
        self.__output = FileGenerator(out_file_name)
        self.__fernet = Fernet(Fernet.generate_key())

    def async_encrypt(self):
        file_data = self.__input.get_file_content_binary()
        file_len = len(file_data)
        chunck_size = 21
        current_pos = 0
        bts = bytearray()

        while current_pos < file_len - chunck_size:
            bt = rsa.encrypt(file_data[current_pos:current_pos + chunck_size], self.__pubkey)
            bts.extend(bt)
            current_pos += chunck_size

        bt = rsa.encrypt(file_data[current_pos:], self.__pubkey)
        bts.extend(bt)

        self.__encrypt.overwrite_content_binary(bts)

    def async_decrypt(self):
        file_data = self.__encrypt.get_file_content_binary()
        file_len = len(file_data)
        current_pos = 0
        chunck_size = KEY_SIZE // 8
        output = ''

        while current_pos < file_len:
            bt = rsa.decrypt(file_data[current_pos:current_pos + chunck_size], self.__privkey).decode()
            output += bt
            current_pos += chunck_size

        self.__output.overwrite_content(output)

    def sync_encrypt(self):
        file_data = self.__input.get_file_content_binary()

        encrypted_content = self.__fernet.encrypt(file_data)

        self.__encrypt.overwrite_content_binary(encrypted_content)

    def sync_decrypt(self):
        file_data = self.__encrypt.get_file_content_binary()

        decrypted_content = self.__fernet.decrypt(file_data).decode()

        self.__output.overwrite_content(decrypted_content)