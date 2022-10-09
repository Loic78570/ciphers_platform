class CaesarCipher:
    def __init__(self):
        self.plaintext = None
        self.ciphertext = None
        self.key = int(0)

    def set_plaintext(self, plaintext: str):
        self.plaintext = str(plaintext)
        self.ciphertext = None

    def set_ciphertext(self, ciphertext: str):
        self.ciphertext = str(ciphertext)
        self.plaintext = None

    def set_key(self, key: int):
        self.key = int(key)

    def __str__(self):
        if self.plaintext:
            return f'\033[1mClé {self.key}:\033[0m {self.plaintext}'
        else:
            return f'\033[1mClé {self.key}:\033[0m \x1B[3m(chiffré)\x1B[0m {self.ciphertext}'

    @staticmethod
    def __compute(message: str, key: int = None):
        stringcipher = str()
        localplaintext = message.lower()

        for c in localplaintext:
            if c != ' ':
                originalAlphabetPosition = ord(c) - ord('a')
                newAlphabetPosition = (originalAlphabetPosition + (key % 26)) % 26
                newchar = chr(ord('a') + newAlphabetPosition)
                stringcipher += newchar
            else:
                stringcipher += c

        return stringcipher

    def encrypt(self, key: int = None):
        if not key: key = self.key
        # if not self.plaintext: raise Exception("Il n'y a rien à chiffrer.")

        stringcipher = self.__compute(self.plaintext, key)
        self.ciphertext = stringcipher
        return stringcipher

    def decrypt(self, key: int = None):
        if not key: key = self.key
        reverse_key = 26 - (key % 26)
        string_decrypt = self.__compute(self.ciphertext, reverse_key)
        self.plaintext = string_decrypt
        return string_decrypt

    def brute_decipher(self):
        for i in range(26):
            decode = self.decrypt(key=i)
            print(f"\033[1mClé {str(i).zfill(2)}:\033[0m {decode}")
        print("\n")
