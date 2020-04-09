from Crypto.Cipher import AES
import base64
from pbkdf2 import PBKDF2
from conf import encryption_key


class EncryptionClient:

    def __init__(self):
        self.iv = bytes([83, 71, 26, 58, 54, 35, 22, 11,
                         83, 71, 26, 58, 54, 35, 22, 11])
        self.enc_key = encryption_key

    def _pad_and_convert_to_bytes(self, text):
        return bytes(text+chr(16-len(text) % 16)*(16-len(text) % 16), encoding="utf-8")

    def encrypt(self, text):
        padded_text = self._pad_and_convert_to_bytes(text)
        key_gen = PBKDF2(self.enc_key, self.iv)

        aesiv = key_gen.read(16)
        aeskey = key_gen.read(32)
        cipher = AES.new(aeskey, AES.MODE_CBC, aesiv)

        return str(base64.b64encode(cipher.encrypt(padded_text)), encoding="utf-8")
