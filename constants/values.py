CHARACTER_SETS = {
    "Numeric_1": "0123456789+-.%/*",
    "Numeric_2": "0123456789-.%<>/",
    "Text": None,
    "AlphaNumericUpperCase": r"01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ ~!@#$%^&*()+-={[}]\\;:/?<.>",
    "AlphaNumericLowerCase": r"01234567890abcdefghijklmnopqrstuvwxyz ~!@#$%^&*()+-={[}]\\;:/?<.>",
    "AlphaNumeric": r"01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ~!@#$%^&*()+-={[}]\\;:/?<.>\',|`",
    "AlphabetsUpperCase": r"ABCDEFGHIJKLMNOPQRSTUVWXYZ .\\-/\'",
    "AlphabetsLowerCase": r"abcdefghijklmnopqrstuvwxyz .\\-/\'",
    "Alphabets": r"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz .,-@\'*!|?_=",
    "HexaDecimal": "0123456789ABCDEF"
}

WHITELISTED_VERSION_1 = {
    0x9990, 0x998F
}

WHITELISTED_VERSION_2 = {
    0x1E, 0x20  # ECC_KEY_1
}

WHITELISTED_VERSION_3 = {
    0x998E, 0x998D
}

WHITELISTED_VERSION_4 = {
    0x1F, 0x21  # ECC_KEY_2
}

IMAGE_HEADER_RIFF = b"RIFF"
IMAGE_HEADER_WEBP = b"WEBP"
IMAGE_HEADER_VP8 = b"VP8 "  # with a space (0x20)

ECC_KEY_1 = ("AwEAA0VDQ1UAAAABAAwxLjMuMTMyLjAuMzQAYwRhBI1vbBVnA1KE/T1UpdQYzG6LLot++cuCP5DdEdeKtedw5G8RKAhU0KbNXVUwym8CSw"
             "UyzdAPC98DAgvkJGOZA/x+cnJOWhVvYTqJvy+IlcOgjSe9kqs0O7zEBy26UmvlIw==")
ECC_KEY_2 = ("AwEAA0VDQ1UAAAABAAwxLjMuMTMyLjAuMzQAYwRhBJ+fsFQNaIohp5JnCmGArWA5i25WAKHqFYnOEpRYsVmxK/O2W7iIy2T9x3vkZHaZm6"
             "61w93VNc/99coCSzL92c1x9y5zxQPJCUztH2kT/EwGphLgvKKe2tK/rKMjNDMpSA==")
