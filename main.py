import io
import json
import os
from construct import ValidationError
from loguru import logger
from time import time
from utils.unpacker import BitUnpacker
from utils.parser import Parser
from utils.verifier import Verifier
import click


class OPANQr(object):
    def __init__(self, string: str, verify: bool):
        self.output_dir: str = os.path.join(os.getcwd(), "output", str(time()))
        self.photo: bytes = None
        self.scanned_string: str = string
        self.unpacked_string: bytes = self.unpack()
        self.verify: bool = verify
        self.pii: dict

    def unpack(self) -> bytes:
        stream = io.BytesIO()
        unpacker = BitUnpacker(stream)

        sliced_bytes = [self.scanned_string[i:i + 4] for i in range(0, len(self.scanned_string), 4)]
        for sliced in sliced_bytes:
            unpacker.bit_unpack(int(sliced), 13)

        stream.seek(0)
        return stream.read()

    def dump(self) -> None:
        os.makedirs(self.output_dir, exist_ok=True)

        with open(os.path.join(self.output_dir, "output.json"), "w") as f:
            json.dump(self.pii, f)
        with open(os.path.join(self.output_dir, "image.webp"), "wb") as f:
            f.write(self.photo)

    def parse(self) -> None:
        parser = Parser(self.unpacked_string)

        if not parser.validate():
            logger.error("The PAN QR could not be validated.")
            raise ValidationError

        parser.handle_control()

        self.photo = parser.image
        self.pii = parser.pii

        if self.verify:
            verifier = Verifier()
            if verifier.verify(parser.message, parser.signature):
                logger.info("Signature successfully verified!")


@click.command()
@click.option("--string", help="The scanned QR Code string as-is")
@click.option("--verify", help="Verify the signature", is_flag=True)
@click.option("--file", help="The scanned QR string from a file")
def main(string: str, verify: bool, file: io.FileIO) -> None:
    opanqr = OPANQr(string, verify)
    opanqr.parse()
    opanqr.dump()


if __name__ == "__main__":
    main()
