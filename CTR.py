import pyaes, pbkdf2, binascii, os, secrets
def _encryption(p):
    password = "s3cr3t*c0d3"
    passwordSalt = os.urandom(16)
    key = pbkdf2.PBKDF2(password, passwordSalt).read(16)

    m=[]
    m.clear()
    iv = secrets.randbits(128)
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    ciphertext = aes.encrypt(p)
    m.append(ciphertext),m.append(key),m.append(iv)
    return m

def _decryption(c,k,iv):
    aes = pyaes.AESModeOfOperationCTR(k, pyaes.Counter(iv))
    decrypted = aes.decrypt(c)
    return decrypted

