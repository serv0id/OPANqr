import re
from constants.structs import PAN_OUTER_BLOCK_STRUCT, SCBLOB_STRUCT, PAN_OUTER_BLOCK_STRUCT_MESSAGE
from constants.values import WHITELISTED_VERSION_1, WHITELISTED_VERSION_2, WHITELISTED_VERSION_3, WHITELISTED_VERSION_4, \
    ECC_KEY_1, ECC_KEY_2
from constants.enums import SecureCodeType, SCBlobIdentifier, PlaceHolderTypes
from utils.image import ImageProcessor
from utils.inflater import ZlibInflater
from loguru import logger
from bitstring import ConstBitStream


class Parser(object):
    def __init__(self, in_struct: bytes):
        self.input: bytes = in_struct
        self.pan_outer = PAN_OUTER_BLOCK_STRUCT.parse(self.input)
        self.signature: bytes = self.pan_outer.signature_data
        self.message = PAN_OUTER_BLOCK_STRUCT_MESSAGE.build(self.pan_outer.message)
        self.public_key: str = self.set_key()
        self.image: bytes
        self.pii: dict

    def validate(self) -> bool:
        """
        Validates a few fields in the outermost struct to pass it off as valid.
        Checks have been reimplemented directly from the APK. Some of these do not
        make immediate sense.
        """
        if self.pan_outer.message.reserved_1 not in (
                WHITELISTED_VERSION_1 | WHITELISTED_VERSION_2 | WHITELISTED_VERSION_3 | WHITELISTED_VERSION_4
        ):
            return False

        if self.pan_outer.message.reserved_3 > 6:
            return False

        return True

    def handle_control(self) -> None:
        """
        Handles individual units inside the larger pan_outer block.
        """
        logger.debug(f"Found {self.pan_outer.message.num_blocks_1} block(s) in part 1")

        for block in self.pan_outer.message.blocks_1:
            control_type = block.metadata.control_type
            if control_type == SecureCodeType.SCBlob.name:
                self.handle_blob(block.data)

        logger.debug(f"Found {self.pan_outer.message.num_blocks_2} blocks(s) in part 2")

        for block in self.pan_outer.message.blocks_2:
            control_type = block.metadata.control_type
            if control_type == SecureCodeType.SCBlob.name:
                self.handle_blob(block.data)

    def handle_blob(self, blob: SCBLOB_STRUCT):
        """
        Handles parsing the SCBlob structure. Most commonly houses PII and Image.
        """
        blob_parsed = SCBLOB_STRUCT.parse(blob)
        if blob_parsed.identifier == SCBlobIdentifier.Image.name:
            logger.debug("Image blob encountered!")
            image_object = ImageProcessor(blob_parsed.data)
            self.image = image_object.fix_header()

        elif blob_parsed.identifier == SCBlobIdentifier.PII.name:
            logger.debug("PII blob encountered!")
            inflater = ZlibInflater(blob_parsed.data)
            inflated_pii = inflater.inflate()
            self.handle_pii(inflated_pii)

        elif blob_parsed.identifier == SCBlobIdentifier.Mixed.name:
            logger.debug("Mixed SCBlob encountered! Parsing has not been implemented!")

        else:
            logger.debug("Unknown SCBlob encountered")

    def handle_pii(self, data: bytes) -> None:
        """
        Handles parsing the PII SCBlob. Currently uses a workaround; not properly implemented.
        """
        # pii_parsed = PII_STRUCT.parse(data)
        # num_elements = pii_parsed.num_blocks
        #
        # logger.debug(f"Found {num_elements} elements in the PII struct")

        # pii_data_stream = ConstBitStream(pii_parsed.data)
        #
        # for i in range(num_elements):
        #     metadata = pii_data_stream.read(8)[::-1]  # type
        #     control_type = SecureCodeType(metadata.read(4).uint)
        #     print(control_type)
        #     if control_type == SecureCodeType.SCTextH2:
        #         self.handle_h2(metadata, pii_data_stream)
        #     elif control_type == SecureCodeType.SCNewLine:
        #         self.handle_newline()
        #     elif control_type == SecureCodeType.SCPlaceHolder:
        #         self.handle_placeholder(metadata, pii_data_stream)

        pattern = re.compile(b'\x08\x02(.)', re.DOTALL)
        results = []

        for match in pattern.finditer(data):
            length_byte = match.group(1)[0]  # convert from bytes to int
            start = match.end()
            end = start + length_byte
            payload = data[start:end]

            results.append({
                'match_start': match.start(),
                'length': length_byte,
                'payload': payload
            })

        self.pii = {
            "PAN": results[0]["payload"].decode(),
            "Name": results[1]["payload"].decode(),
            "FName": results[2]["payload"].decode(),
            "DOB": results[3]["payload"].decode()
        }

    def handle_h1(self):
        """
        Handles parsing the SCTextH1 structure.
        """
        raise NotImplementedError

    def handle_h2(self, metadata: ConstBitStream, stream: ConstBitStream):
        """
        Handles parsing the SCTextH2 structure.
        """
        raise NotImplementedError

    def handle_caption(self):
        """
        Handles parsing the SCTextCaption structure.
        """
        raise NotImplementedError

    def handle_text(self):
        """
        Handles parsing the SCTextNormal structure.
        """
        raise NotImplementedError

    def handle_table(self):
        """
        Handles parsing the SCTable structure.
        """
        raise NotImplementedError

    def handle_placeholder(self, metadata: ConstBitStream, stream: ConstBitStream):
        """
        Handles parsing the SCPlaceHolder structure.
        """
        placeholder_type = PlaceHolderTypes(metadata.read(4).uint)
        text = stream.read("bytes:1")

        logger.debug(f"{placeholder_type} encountered with content: {text.decode()}")

    def handle_identifier(self):
        """
        Handles parsing the SCIdentifier structure.
        """
        raise NotImplementedError

    def handle_align(self):
        """
        Handles parsing the SCAlign structure. Used to align text in the app's XML output string.
        Can be ignored.
        """
        raise NotImplementedError

    @staticmethod
    def handle_newline() -> None:
        """
        Handles parsing the SCNewLine structure. Can be ignored.
        """
        logger.debug("SCNewLine Encountered!")

    def handle_background(self):
        """
        Handles parsing the SCBackground structure.
        """
        raise NotImplementedError

    def handle_line(self):
        """
        Handles parsing the SCLIne structure.
        """
        raise NotImplementedError

    def handle_hyperlink(self):
        """
        Handles parsing the SCHyperLink structure.
        """
        raise NotImplementedError

    def set_key(self):
        """
        Sets the ECC public key responsible for verification based on the
        version of the PAN QR Code.
        """
        if self.pan_outer.message.reserved_1 in WHITELISTED_VERSION_2:
            return ECC_KEY_1
        elif self.pan_outer.message.reserved_1 in WHITELISTED_VERSION_4:
            return ECC_KEY_2
        else:
            return None
