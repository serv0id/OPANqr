from enum import Enum


class SecureCodeType(Enum):
    SCTextH1 = 0
    SCTextH2 = 1
    SCTextCaption = 2
    SCTextNormal = 3
    SCTable = 4  # TODO: implement SCTable parsing
    SCBlob = 5
    SCPlaceHolder = 6
    SCIdentifier = 7
    SCAlign = 8
    SCNewLine = 9
    SCBackground = 10
    SCLIne = 11  # not a typo
    SCHyperLink = 12


class CodeType(Enum):
    SingleCode = 3
    MultiCode = 6


class CharacterSets(Enum):
    Numeric_1 = 0
    Numeric_2 = 1
    Text = 2
    AlphaNumericUpperCase = 3
    AlphaNumericLowerCase = 4
    AlphaNumeric = 5
    AlphabetsUpperCase = 6
    AlphabetsLowerCase = 7
    Alphabets = 8
    HexaDecimal = 9


class SignatureScheme(Enum):
    ECC = 0
    RSA = 1


class SCBlobIdentifier(Enum):
    PII = 0x0302
    Image = 0x0102
    Mixed = 0x0301  # unimplemented


class AlignPosition(Enum):
    LeftTop = 0
    LeftCenter = 1
    LeftBottom = 2
    CenterTop = 3
    CenterCenter = 4
    CenterBottom = 5
    RightTop = 6
    RightCenter = 7
    RightBottom = 8
