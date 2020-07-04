from Crypto.Cipher import AES


def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])


# Fix the second broken plaintext block
def fix_second_broken_plaintext_block(block):
    sorted_block = sorted(block)
    if sorted_block[0] != sorted_block[1]:
        return (chr(sorted_block[1]) * 16).encode('utf_8')
    else:
        return (chr(sorted_block[1]) * 16).encode('utf_8')


def cbc_custom_decrypt(key, n, ct):
    plaintext = b''
    cipher = AES.new(key, AES.MODE_ECB)
    for i in range(1, n + 1):
        # After decrypting this block of cipher-text, the resultant data is XOR'd
        # with the previous block of cipher-text to recover the original plaintext
        plaintext = plaintext + byte_xor(cipher.decrypt(ct[16 * i:16 * (i + 1)]), ct[16 * (i - 1):16 * i])
    return plaintext


def cbc_flip_fix(key, n, ct):
    broken_plaintext = cbc_custom_decrypt(key, n, ct)
    broken_block_found_flag = False

    # Search for the first broken block (the one that his bit number j of the cipher-text got flipped)
    for i in range(0, n + 1):
        for byte_index in range(0, 15):
            if broken_plaintext[16 * i:16 * (i + 1)][byte_index] != \
                    broken_plaintext[16 * i:16 * (i + 1)][byte_index + 1]:
                broken_block_found_flag = True
                break
        # If broken block was found
        if broken_block_found_flag:
            break

    print("sami" + str(i))
    # Fix the second broken plaintext block
    bit_to_flip = byte_xor(fix_second_broken_plaintext_block(broken_plaintext[16 * (i + 1):16 * (i + 2)]),
                           broken_plaintext[16 * (i + 1):16 * (i + 2)])
    print(bit_to_flip)
    #print(byte_xor(ct[16 * i:16 * (i + 1)], bit_to_flip))
   # print(ct[16 * i:16 * (i + 1)])
    #cipher = AES.new(key, AES.MODE_ECB)
    return 0#byte_xor(cipher.decrypt(byte_xor(ct[16 * i:16 * (i + 1)], bit_to_flip)), ct[16 * (i-1):16 * i])
