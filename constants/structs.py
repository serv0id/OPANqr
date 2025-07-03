from construct import Int8ub, Int16ub, Int32ub, Struct, Bytes, Padding, BitStruct, BitsInteger, Flag, Nibble, \
    IfThenElse, GreedyBytes, this, BitsSwapped, Enum, Const
from constants.enums import SecureCodeType, CodeType, CharacterSets, SignatureScheme, SCBlobIdentifier

ECC_KEY_STRUCT = Struct(
    "reserved" / Const(b"\x03\x01"),
    Padding(2),  # magic length but constant (0x3)
    "magic" / Const(b"ECC"),
    Padding(5),  # unused
    "curve_oid_length" / Int16ub,
    "curve_oid" / Bytes(this.curve_oid_length),
    "key_length" / Int16ub,
    "key" / Bytes(this.key_length)
)

METADATA_UPPER_STRUCT = BitsSwapped(BitStruct(
    "control_type" / Enum(BitsInteger(3), SecureCodeType),
    "exceed_length_flag" / Flag,  # if set, 2 bytes are read for the parent block's length (exceeds 256)
    "character_set" / Enum(Nibble, CharacterSets)
))

PAN_INNER_BLOCK_STRUCT = Struct(
    "metadata" / METADATA_UPPER_STRUCT,
    "length" / IfThenElse(this.metadata.exceed_length_flag, Int16ub, Int8ub),
    "data" / Bytes(this.length)
)

SCBLOB_STRUCT = Struct(
    "identifier" / Enum(Int16ub, SCBlobIdentifier),
    "data" / GreedyBytes
)

PII_STRUCT = Struct(
    "num_blocks" / Int16ub,
    "data" / GreedyBytes
)

PAN_OUTER_BLOCK_STRUCT = Struct(
    "code_type" / Enum(Int8ub, CodeType),
    Padding(1),  # unused
    "reserved_1" / Int32ub,
    "reserved_2" / Int8ub,
    "reserved_3" / Int16ub,
    "num_blocks_1" / Int8ub,
    "blocks_1" / PAN_INNER_BLOCK_STRUCT[this.num_blocks_1],
    "num_blocks_2" / Int8ub,
    "blocks_2" / PAN_INNER_BLOCK_STRUCT[this.num_blocks_2],
    "reserved_4" / Const(b"\x01"),
    "signature_scheme" / Enum(Int8ub, SignatureScheme),
    Padding(2),  # unused
    "signature_length" / Enum(Int16ub),
    "signature_data" / Bytes(this.signature_length)
)


