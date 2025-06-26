from constants.values import IMAGE_HEADER_RIFF, IMAGE_HEADER_WEBP, IMAGE_HEADER_VP8


class ImageProcessor(object):
    def __init__(self, image: bytes):
        self.image_bytes: bytes = image

    def retrieve_length(self) -> bytes:
        return self.image_bytes[2:6]

    def fix_header(self) -> bytes:
        fixed_image = bytearray()
        fixed_image[0:4] = IMAGE_HEADER_RIFF
        fixed_image[4:8] = self.retrieve_length()
        fixed_image[8:12] = IMAGE_HEADER_WEBP
        fixed_image[12:16] = IMAGE_HEADER_VP8
        fixed_image[16:] = self.image_bytes[16:]

        return fixed_image
