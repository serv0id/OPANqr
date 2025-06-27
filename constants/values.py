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

WHITELISTED_RESERVED_1 = {
    0x9990, 0x998F, 0x1E, 0x20, 0x998E, 0x998D, 0x1F, 0x21
}

IMAGE_HEADER_RIFF = b"RIFF"
IMAGE_HEADER_WEBP = b"WEBP"
IMAGE_HEADER_VP8 = b"VP8 "  # with a space (0x20)

ECC_KEY_1 = ("AwEAA0VDQ1UAAAABAAwxLjMuMTMyLjAuMzQAYwRhBI1vbBVnA1KE/T1UpdQYzG6LLot++cuCP5DdEdeKtedw5G8RKAhU0KbNXVUwym8CSw"
             "UyzdAPC98DAgvkJGOZA/x+cnJOWhVvYTqJvy+IlcOgjSe9kqs0O7zEBy26UmvlIw==")
