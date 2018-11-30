key = "a"


def encryption_xor(my_str, key):
    encryption_str = ""
    for letter in my_str:
        if type(key) is int:
            encryption_str += chr(ord(letter) ^ key)
        else:
            encryption_str += chr(ord(letter) ^ ord(key))
    print(encryption_str)
    return encryption_str


def decryption_xor(crypt_str, key):
    decryption_str = ""
    for letter in crypt_str:
        if type(key) is int:
            decryption_str += chr(ord(letter) ^ key)
        else:
            decryption_str += chr(ord(letter) ^ ord(key))
    print(decryption_str)


def main():
    new_str = encryption_xor("А роза упала на лапу Азора", key)
    decryption_xor(new_str, key)


if __name__ == "__main__":
    main()


