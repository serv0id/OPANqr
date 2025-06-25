from constants.structs import PAN_OUTER_BLOCK_STRUCT
from constants.values import WHITELISTED_RESERVED_1


class Parser(object):
    def __init__(self, in_struct):
        self.input: bytes = in_struct
        self.pan_outer = PAN_OUTER_BLOCK_STRUCT.parse(self.input)

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

    def handle_blob(self):
        """
        Handles parsing the SCBlob structure. Most commonly houses PII and Image.
        """
        pass

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
