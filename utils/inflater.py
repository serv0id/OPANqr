import zlib


class ZlibInflater(object):
    def __init__(self, data: bytes):
        self.compressed_data = data

    def inflate(self) -> bytes:
        return zlib.decompress(self.compressed_data)
