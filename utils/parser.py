from constants.structs import PAN_OUTER_BLOCK_STRUCT, PII_STRUCT, SCBLOB_STRUCT
from constants.values import WHITELISTED_RESERVED_1
from constants.enums import SecureCodeType, SCBlobIdentifier
from utils.image import ImageProcessor
from loguru import logger


class Parser(object):
    def __init__(self, in_struct: bytes):
        self.input: bytes = in_struct
        self.pan_outer = PAN_OUTER_BLOCK_STRUCT.parse(self.input)
        self.image: bytes

    def validate(self) -> bool:
        """
        Validates a few fields in the outermost struct to pass it off as valid.
        Checks have been reimplemented directly from the APK. Some of these do not
        make immediate sense.
        """
        if self.pan_outer.reserved_1 not in WHITELISTED_RESERVED_1:
            return False

        if self.pan_outer.reserved_3 > 6:  # maybe version?
            return False

        return True

    def handle_control(self):
        """
        Handles individual units inside the larger pan_outer block.
        """
        logger.debug(f"Found {self.pan_outer.num_blocks_1} block(s) in part 1")

        for block in self.pan_outer.blocks_1:
            control_type = block.metadata.control_type
            if control_type == SecureCodeType.SCBlob.name:
                self.handle_blob(block.data)

        logger.debug(f"Found {self.pan_outer.num_blocks_2} blocks(s) in part 2")

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
            print("PII found!")

    def handle_h1(self):
        """
        Handles parsing the SCTextH1 structure.
        """
        raise NotImplementedError

    def handle_h2(self):
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

    def handle_placeholder(self):
        """
        Handles parsing the SCPlaceHolder structure.
        """
        raise NotImplementedError

    def handle_identifier(self):
        """
        Handles parsing the SCIdentifier structure.
        """
        raise NotImplementedError

    def handle_align(self):
        """
        Handles parsing the SCAlign structure.
        """
        raise NotImplementedError

    def handle_newline(self):
        """
        Handles parsing the SCNewLine structure.
        """
        raise NotImplementedError

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
