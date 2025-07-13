from base64 import b64decode
from constants.structs import ECC_KEY_STRUCT
from ecdsa import VerifyingKey, NIST384p
from hashlib import sha384


class Verifier(object):
    def __init__(self, key: str):
        self.key_object = ECC_KEY_STRUCT.parse(b64decode(key))
        self.key = self.key_object.key[2:]

    def verify(self, message: bytes, signature: bytes) -> bool:
        verifier = VerifyingKey.from_string(self.key, curve=NIST384p, hashfunc=sha384, validate_point=True)
        return verifier.verify(signature, data=message)
