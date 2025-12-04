class VigenereCipher:
    def __init__(self, key):
        if not key.isalpha():
            raise ValueError("Key must contain only alphabets.")
        self.key = key.lower()

    def _shift(self, char, key_char, decrypt=False):
        if not char.isalpha():
            return char
        
        base = ord('A') if char.isupper() else ord('a')
        key_shift = ord(key_char) - ord('a')

        if decrypt:
            key_shift = -key_shift

        return chr((ord(char) - base + key_shift) % 26 + base)

    def encrypt(self, text):
        result = []
        key_index = 0
        
        for char in text:
            if char.isalpha():
                result.append(self._shift(char, self.key[key_index % len(self.key)]))
                key_index += 1
            else:
                result.append(char)
        
        return "".join(result)

    def decrypt(self, cipher):
        result = []
        key_index = 0
        
        for char in cipher:
            if char.isalpha():
                result.append(self._shift(char, self.key[key_index % len(self.key)], decrypt=True))
                key_index += 1
            else:
                result.append(char)
        
        return "".join(result)


# Example usage
cipher = VigenereCipher("KEY")

encrypted = cipher.encrypt("Hello World!")
decrypted = cipher.decrypt(encrypted)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
