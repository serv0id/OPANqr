from constants.structs import PAN_OUTER_BLOCK_STRUCT


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
        pass

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

