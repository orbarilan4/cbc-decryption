from Crypto.Cipher import AES


def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])


def cbc_custom_decrypt(key, n, ct):
    plaintext = b''
    cipher = AES.new(key, AES.MODE_ECB)
    for i in range(1, n+1):
        # After decrypting this block of cipher-text, the resultant data is XOR'd
        # with the previous block of cipher-text to recover the original plaintext
        plaintext = plaintext + byte_xor(cipher.decrypt(ct[16*i:16*(i+1)]), ct[16*(i-1):16*i])
    return plaintext




