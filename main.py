from Timer import Timer
from FileCrypto import FileCrypto
from ExcelGenerator import ExcelGenerator

def generate():
    text_file = open('input.txt', 'w')

    for _ in range(0, 283399):
        text_file.write('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\r')

    text_file.close()

generate()

file_encryptor = FileCrypto('input.txt', 'encrypt.txt', 'output.txt')

async_encrypt_time = Timer.time(file_encryptor.async_encrypt)
async_decrypt_time = Timer.time(file_encryptor.async_decrypt)

generate()

sync_encrypt_time = Timer.time(file_encryptor.sync_encrypt)
sync_decrypt_time = Timer.time(file_encryptor.sync_decrypt)

print('Async encrypt time: '+str(async_encrypt_time))
print('Async decrypt time: '+str(async_decrypt_time))
print('Sync encrypt time: '+str(sync_encrypt_time))
print('Sync decrypt time: '+str(sync_decrypt_time))

excel = ExcelGenerator()
excel.recieve_times([async_encrypt_time, async_decrypt_time, sync_encrypt_time, sync_decrypt_time])