from cryptography.fernet import Fernet


# from os import urandom
# print(urandom(128))
def generate_key(key_file):
    with open(key_file, 'wb') as fw:
        fw.write(Fernet.generate_key())


def encode_password(key_file, password):
    f = Fernet(open(key_file, 'rb').read())
    return f.encrypt(password)


def decode_password(key_file, token):
    f = Fernet(open(key_file, 'rb').read())
    return f.decrypt(token)


if __name__ == '__main__':
    generate_key('.hashkeys')
    print(encode_password('.hashkeys', b'training'))
