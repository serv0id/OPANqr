class BitUnpacker(object):
    """
    The PAN QR string uses a non-standard(?) unpacking subroutine.
    Ported directly from the baksmali.
    """
    def __init__(self, output_stream):
        self.output_stream = output_stream
        self.a = 0
        self.b = 0

    def bit_unpack(self, v: int, v1: int):
        if v1 > 0x20 or v1 < 1:
            raise ValueError(f"{v1} is not between 1 and 32.")

        v2 = self.b
        if v2 > 0 and v2 + v1 >= 8:
            v3 = (self.a | (v << v2)) & 0xFF
            self.a = v3
            v >>= 8 - v2
            v1 -= 8 - v2
            self.output_stream.write(bytes([v3]))
            self.a = 0
            self.b = 0

        while v1 // 8 > 0:
            self.output_stream.write(bytes([v & 0xFF]))
            v >>= 8
            v1 -= 8

        if v1 > 0:
            self.a = ((v << self.b) | self.a) & 0xFF
            self.b += v1
            

if __name__ == "__main__":
    with open('output.bin', 'wb') as f:
        packer = BitUnpacker(f)

        pan_str = "test"
        out = [pan_str[i:i + 4] for i in range(0, len(pan_str), 4)]

        for bit in out:
            packer.bit_unpack(int(bit), 13)
