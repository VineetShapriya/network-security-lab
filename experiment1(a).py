class CaesarCipher:
    def __init__(self, shift):
        if not isinstance(shift, int):
            raise ValueError("Shift must be an integer.")
        self.shift = shift % 26
    
    def _shift_char(self, char, shift):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            return chr((ord(char) - base + shift) % 26 + base)
        return char

    def encrypt(self, text):
        return "".join(self._shift_char(c, self.shift) for c in text)

    def decrypt(self, text):
        return "".join(self._shift_char(c, -self.shift) for c in text)


# Example usage
cipher = CaesarCipher(3)

encrypted = cipher.encrypt("Hello World!")
decrypted = cipher.decrypt(encrypted)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
