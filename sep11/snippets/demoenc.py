import Crypto
import base64



def encrypt(hstr, payload, encryptionKey):
    hstr = Crypto.Cipher.XOR().new(encryptionKey).encrypt(hstr)
    hstr = base64.b64encode(hstr)

    payload = Crypto.Cipher.XOR().new(encryptionKey).encrypt(payload)
    payload = base64.b64encode(payload)

    return [hstr, payload]



print(encrypt('a sample string', 'peter', 'xxx'))
