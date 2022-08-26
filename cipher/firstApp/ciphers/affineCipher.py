from secretpy import Affine
BINARY = u"01"
DECIMAL = u"0123456789"
DOZENAL = u"0123456789ab"
HEX = u"0123456789abcdef"
OCTAL = u"01234567"

ENGLISH = u"abcdefghijklmnopqrstuvwxyz"
alphabet = ENGLISH
# plaintext = "thequickbrownfoxjumpsoverthelazydog"
# key = (7, 8)

cipher = Affine()
def affineEnc(plaintext,key):
    enc = cipher.encrypt(plaintext, key, alphabet)
    return enc
def affineDec(plaintext,key):
    dec = cipher.decrypt(plaintext, key, alphabet)
    return dec