from base64 import b64decode
from constants.structs import ECC_KEY_STRUCT
from constants.values import ECC_KEY


class Verifier(object):
    def __init__(self):
        self.key_object = ECC_KEY_STRUCT.parse(b64decode(ECC_KEY))
        self.key = self.key_object.key[2:]
