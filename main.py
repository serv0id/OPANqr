from io import BytesIO

from construct import ValidationError
from loguru import logger
from time import time
from utils.unpacker import BitUnpacker
from utils.parser import Parser
import click


class OPANQr(object):
    def __init__(self, string):
        self.output_dir: str = f"output/{time()}"
        self.photo: bytes
        self.name: str
        self.pan_number: str
        self.scanned_string: str = string
        self.unpacked_string: bytes = self.unpack()

    def unpack(self) -> bytes:
        stream = BytesIO()
        unpacker = BitUnpacker(stream)

        sliced_bytes = [self.scanned_string[i:i + 4] for i in range(0, len(self.scanned_string), 4)]
        for sliced in sliced_bytes:
            unpacker.bit_unpack(int(sliced), 13)

        stream.seek(0)
        return stream.read()

    def parse(self) -> dict:
        parser = Parser(self.unpacked_string)

        if not parser.validate():
            logger.error("The PAN QR could not be validated.")
            raise ValidationError

        parser.handle_control()


@click.command()
@click.option("--string", help="The scanned QR Code string as-is")
def main(string) -> None:
    opanqr = OPANQr(string)
    opanqr.parse()


if __name__ == "__main__":
    main()
