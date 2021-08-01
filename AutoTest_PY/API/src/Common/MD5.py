import hashlib


class MD5:

    def encrypt_md5(self, str):
        hash = hashlib.md5()
        betys = str.encode(encoding='utf-8')
        hash.update(betys)
        return hash.hexdigest()

    def decrypt_md5(self):
        pass


if __name__ == "__main__":
    MD5 = MD5()

    print(MD5.encrypt_md5("hwx927099"))
