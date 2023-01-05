# Imports
import logging




# Relative imports
from .. import util




# Shortcuts
v = util.validate




# Notes
# -




# Set up logger for this module. By default, it produces no output.
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
logger.setLevel(logging.ERROR)
log = logger.info
deb = logger.debug




def setup(
    log_level = 'error',
    debug = False,
    log_timestamp = False,
    log_file = None,
    ):
  # Configure logger for this module.
  util.module_logger.configure_module_logger(
    logger = logger,
    logger_name = __name__,
    log_level = log_level,
    debug = debug,
    log_timestamp = log_timestamp,
    log_file = log_file,
  )
  deb('Setup complete.')




def utf8_latin_1_to_eml(text):
  validate_utf8_latin_1(text)
  s = ''
  for c in text:
    #code_point = hex(ord(c))[2:].zfill(4)
    #print(code_point)
    c2 = convert_character_utf8_latin_1_to_eml(c)
    #print(repr(c), repr(c2))
    s += c2
  return s




def validate_utf8_latin_1(text):
  printable_ascii = get_printable_ascii()
  utf8_latin_1 = get_utf8_latin_1()
  for c in text:
    if c not in printable_ascii and c not in utf8_latin_1:
      msg = "Character '{}' is not in printable_ascii or in utf8_latin_1.".format(c)
      raise ValueError(msg)




def convert_character_utf8_latin_1_to_eml(c):
  printable_ascii = get_printable_ascii()
  conversions = get_utf8_to_eml_latin_1_conversions()
  # Printable ASCII characters are simply followed by an underscore.
  # - Exceptions:
  # -- A tab is prefixed by a minus sign.
  # -- A newline is prefixed by a plus sign.
  # -- A space is doubled.
  if c in printable_ascii:
    if c == '\t':
      return '-\t'
    elif c == '\n':
      return '+\n'
    elif c == ' ':
      return '  '
    else:
      return c + '_'
  return conversions[c]




def get_utf8_to_eml_latin_1_conversions():
  conversions = get_eml_to_utf8_latin_1_conversions()
  conversions2 = {v: k for k, v in conversions.items()}
  return conversions2




def get_utf8_latin_1():
  conversions = get_eml_to_utf8_latin_1_conversions()
  utf8_latin_1 = sorted(conversions.values())
  return utf8_latin_1




def get_eml_to_utf8_latin_1_conversions():
  conversions = {
    'nb': "\u00a0",  # 00A0 NO-BREAK SPACE
    '!i': "\u00a1",  # 00A1 INVERTED EXCLAMATION MARK
    # Note: 'i' indicates inverted
    'c/': "\u00a2",  # 00A2 CENT SIGN
    'L-': "\u00a3",  # 00A3 POUND SIGN
    'ox': "\u00a4",  # 00A4 CURRENCY SIGN
    'Y=': "\u00a5",  # 00A5 YEN SIGN (= yuan sign)
    '||': "\u00a6",  # 00A6 BROKEN BAR
    'se': "\u00a7",  # 00A7 SECTION SIGN
    '_:': "\u00a8",  # 00A8 DIAERESIS
    # Note: ':' in the second position is used to place a diaeresis / umlaut over a letter. here the first character is 'empty' (an underscore), so the result is a diaeresis symbol by itself. note that the reverse combination :_ signifies a single colon (:).
    'co': "\u00a9",  # 00A9 COPYRIGHT SIGN
    '^a': "\u00aa",  # 00AA FEMININE ORDINAL INDICATOR
    # Note: '^' in the first position indicates superscript height
    '<<': "\u00ab",  # 00AB LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    '-|': "\u00ac",  # 00AC NOT SIGN
    'so': "\u00ad",  # 00AD SOFT HYPHEN
    're': "\u00ae",  # 00AE REGISTERED SIGN
    '^-': "\u00af",  # 00AF MACRON
    # Note: '^' in the first position indicates superscript height
    '^O': "\u00b0",  # 00B0 DEGREE SIGN
    # Note: '^' in the first position indicates superscript height. note the use of capital o (O) to distinguish this character from the masculine ordinal indicator.
    '+-': "\u00b1",  # 00B1 PLUS-MINUS SIGN
    '^2': "\u00b2",  # 00B2 SUPERSCRIPT TWO
    # Note: '^' in the first position indicates superscript height
    '^3': "\u00b3",  # 00B3 SUPERSCRIPT THREE
    # Note: '^' in the first position indicates superscript height
    "_'": "\u00b4",  # 00B4 ACUTE ACCENT
    # Note: "'" in the second position is used to place an acute accent over the character in the first position. here the first character is 'empty' (an underscore), so the result is an acute accent symbol by itself.
    'mi': "\u00b5",  # 00B5 MICRO SIGN
    'pi': "\u00b6",  # 00B6 PILCROW SIGN
    'm.': "\u00b7",  # 00B7 MIDDLE DOT
    '_,': "\u00b8",  # 00B8 CEDILLA
    # Note: ',' in the second position is used to place a cedilla underneath the character in the first position. here the first character is 'empty' (an underscore), so the result is a cedilla symbol by itself.
    '^1': "\u00b9",  # 00B9 SUPERSCRIPT ONE
    # Note: '^' in the first position indicates superscript height
    '^o': "\u00ba",  # 00BA MASCULINE ORDINAL INDICATOR
    # Note: '^' in the first position indicates superscript height
    '>>': "\u00bb",  # 00BB RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    # Vulgar fractions
    '14': "\u00bc",  # 00BC VULGAR FRACTION ONE QUARTER
    '12': "\u00bd",  # 00BD VULGAR FRACTION ONE HALF
    '34': "\u00be",  # 00BE VULGAR FRACTION THREE QUARTERS
    # Punctuation
    '?i': "\u00bf",  # 00BF INVERTED QUESTION MARK
    # Letters
    'A`': "\u00c0",  # 00C0 LATIN CAPITAL LETTER A WITH GRAVE
    # Note: "`" in the second position is used to place a grave accent over the character in the first position.
    "A'": "\u00c1",  # 00C1 LATIN CAPITAL LETTER A WITH ACUTE
    # Note: "'" in the second position is used to place a acute accent over the character in the first position.
    'A^': "\u00c2",  # 00C2 LATIN CAPITAL LETTER A WITH CIRCUMFLEX
    # Note: '^' in the second position is used to place a circumflex over the character in the first position.
    'A~': "\u00c3",  # 00C3 LATIN CAPITAL LETTER A WITH TILDE
    # Note: '~' in the second position is used to place a tilde over the character in the first position.
    'A:': "\u00c4",  # 00C4 LATIN CAPITAL LETTER A WITH DIAERESIS
    # Note: ':' in the second position is used to place a diaeresis over the character in the first position.
    'Ao': "\u00c5",  # 00C5 LATIN CAPITAL LETTER A WITH RING ABOVE
    # Note: 'o' in the second position is used to place a ring over the character in the first position.
    'AE': "\u00c6",  # 00C6 LATIN CAPITAL LETTER AE
    'C,': "\u00c7",  # 00C7 LATIN CAPITAL LETTER C WITH CEDILLA
    'E`': "\u00c8",  # 00C8 LATIN CAPITAL LETTER E WITH GRAVE
    "E'": "\u00c9",  # 00C9 LATIN CAPITAL LETTER E WITH ACUTE
    'E^': "\u00cA",  # 00CA LATIN CAPITAL LETTER E WITH CIRCUMFLEX
    'E:': "\u00cB",  # 00CB LATIN CAPITAL LETTER E WITH DIAERESIS
    'I`': "\u00cc",  # 00CC LATIN CAPITAL LETTER I WITH GRAVE
    "I'": "\u00cd",  # 00CD LATIN CAPITAL LETTER I WITH ACUTE
    'I^': "\u00ce",  # 00CE LATIN CAPITAL LETTER I WITH CIRCUMFLEX
    'I:': "\u00cf",  # 00CF LATIN CAPITAL LETTER I WITH DIAERESIS
    '-D': "\u00d0",  # 00D0 LATIN CAPITAL LETTER ETH
    'N~': "\u00d1",  # 00D1 LATIN CAPITAL LETTER N WITH TILDE
    'O`': "\u00d2",  # 00D2 LATIN CAPITAL LETTER O WITH GRAVE
    "O'": "\u00d3",  # 00D3 LATIN CAPITAL LETTER O WITH ACUTE
    'O^': "\u00d4",  # 00D4 LATIN CAPITAL LETTER O WITH CIRCUMFLEX
    'O~': "\u00d5",  # 00D5 LATIN CAPITAL LETTER O WITH TILDE
    'O:': "\u00d6",  # 00D6 LATIN CAPITAL LETTER O WITH DIAERESIS
    # Mathematical operator
    'xx': "\u00d7",  # 00D7 MULTIPLICATION SIGN
    # Letters
    'O/': "\u00d8",  # 00D8 LATIN CAPITAL LETTER O WITH STROKE
    'U`': "\u00d9",  # 00D9 LATIN CAPITAL LETTER U WITH GRAVE
    "U'": "\u00da",  # 00DA LATIN CAPITAL LETTER U WITH ACUTE
    'U^': "\u00db",  # 00DB LATIN CAPITAL LETTER U WITH CIRCUMFLEX
    'U:': "\u00dc",  # 00DC LATIN CAPITAL LETTER U WITH DIAERESIS
    "Y'": "\u00dd",  # 00DD LATIN CAPITAL LETTER Y WITH ACUTE
    'Ip': "\u00de",  # 00DE LATIN CAPITAL LETTER THORN
    'B.': "\u00df",  # 00DF LATIN SMALL LETTER SHARP S
    # Note: '.' chosen as second character just because it's small and ignorable.
    'a`': "\u00e0",  # 00E0 LATIN SMALL LETTER A WITH GRAVE
    "a'": "\u00e1",  # 00E1 LATIN SMALL LETTER A WITH ACUTE
    'a^': "\u00e2",  # 00E2 LATIN SMALL LETTER A WITH CIRCUMFLEX
    'a~': "\u00e3",  # 00E3 LATIN SMALL LETTER A WITH TILDE
    'a:': "\u00e4",  # 00E4 LATIN SMALL LETTER A WITH DIAERESIS
    'ao': "\u00e5",  # 00E5 LATIN SMALL LETTER A WITH RING ABOVE
    # Note: 'o' in the second position is used to place a ring over the character in the first position.
    'ae': "\u00e6",  # 00E6 LATIN SMALL LETTER AE
    'c,': "\u00e7",  # 00E7 LATIN SMALL LETTER C WITH CEDILLA
    'e`': "\u00e8",  # 00E8 LATIN SMALL LETTER E WITH GRAVE
    "e'": "\u00e9",  # 00E9 LATIN SMALL LETTER E WITH ACUTE
    'e^': "\u00ea",  # 00EA LATIN SMALL LETTER E WITH CIRCUMFLEX
    'e:': "\u00eb",  # 00EB LATIN SMALL LETTER E WITH DIAERESIS
    'i`': "\u00ec",  # 00EC LATIN SMALL LETTER I WITH GRAVE
    "i'": "\u00ed",  # 00ED LATIN SMALL LETTER I WITH ACUTE
    'i^': "\u00ee",  # 00EE LATIN SMALL LETTER I WITH CIRCUMFLEX
    'i:': "\u00ef",  # 00EF LATIN SMALL LETTER I WITH DIAERESIS
    '-d': "\u00f0",  # 00F0 LATIN SMALL LETTER ETH
    'n~': "\u00f1",  # 00F1 LATIN SMALL LETTER N WITH TILDE
    'o`': "\u00f2",  # 00F2 LATIN SMALL LETTER O WITH GRAVE
    "o'": "\u00f3",  # 00F3 LATIN SMALL LETTER O WITH ACUTE
    'o^': "\u00f4",  # 00F4 LATIN SMALL LETTER O WITH CIRCUMFLEX
    'o~': "\u00f5",  # 00F5 LATIN SMALL LETTER O WITH TILDE
    'o:': "\u00f6",  # 00F6 LATIN SMALL LETTER O WITH DIAERESIS
    # Mathematical operator
    '-:': "\u00f7",  # 00F7 DIVISION SIGN
    # Note: here, the ':' in second position does not indicate a diaeresis over the character in first position.
    # Letters
    'o/': "\u00f8",  # 00F8 LATIN SMALL LETTER O WITH STROKE
    'u`': "\u00f9",  # 00F9 LATIN SMALL LETTER U WITH GRAVE
    "u'": "\u00fa",  # 00FA LATIN SMALL LETTER U WITH ACUTE
    'u^': "\u00fb",  # 00FB LATIN SMALL LETTER U WITH CIRCUMFLEX
    'u:': "\u00fc",  # 00FC LATIN SMALL LETTER U WITH DIAERESIS
    "y'": "\u00fd",  # 00FD LATIN SMALL LETTER Y WITH ACUTE
    'ip': "\u00fe",  # 00FE LATIN SMALL LETTER THORN
    'y:': "\u00ff",  # 00FF LATIN SMALL LETTER Y WITH DIAERESIS
  }
  return conversions




def get_printable_ascii():
  data_characters = "!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~"
  escaped_characters = "\"" + "\\"
  whitespace_characters = " \t\n"
  permitted_data_characters = data_characters + escaped_characters + whitespace_characters
  return permitted_data_characters



