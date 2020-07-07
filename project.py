from Crypto.Cipher import AES

BLOCK_SIZE = 16


def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])


# Fix the second corrupted plaintext block
def fix_second_broken_plaintext_block(block):
    sorted_block = sorted(block)
    if sorted_block[0] != sorted_block[1]:
        return (chr(sorted_block[1]) * BLOCK_SIZE).encode('utf_8')
    else:
        return (chr(sorted_block[1]) * BLOCK_SIZE).encode('utf_8')


# Implement CBC decryption by using only ECB decryption
def cbc_custom_decrypt(key, n, cipher):
    plaintext = b''
    crypt = AES.new(key, AES.MODE_ECB)
    for i in range(1, n + 1):
        # After decrypting this block of cipher-text, the resultant data is XOR'd
        # with the previous block of cipher-text to recover the original plaintext
        plaintext = plaintext + byte_xor(
            crypt.decrypt(cipher[BLOCK_SIZE * i:BLOCK_SIZE * (i + 1)]),
            cipher[BLOCK_SIZE * (i - 1):BLOCK_SIZE * i])
    return plaintext


# Getting the original value of the block whose encryption was completely corrupted (by exercise definition)
def cbc_flip_fix(key, n, cipher):
    corrupted_plaintext = cbc_custom_decrypt(key, n, cipher)
    corrupted_block_found_flag = False

    # Search for the first corrupted plain-text block (the one that his bit number j of the cipher-text got flipped)
    for i in range(0, n + 1):
        for byte_index in range(0, BLOCK_SIZE - 1):
            if corrupted_plaintext[BLOCK_SIZE * i:BLOCK_SIZE * (i + 1)][byte_index] != \
                    corrupted_plaintext[BLOCK_SIZE * i:BLOCK_SIZE * (i + 1)][byte_index + 1]:
                corrupted_block_found_flag = True
                break
        # If broken block was found
        if corrupted_block_found_flag:
            break

    # Fix the second broken plaintext block
    bit_to_flip = byte_xor(
        fix_second_broken_plaintext_block(corrupted_plaintext[BLOCK_SIZE * (i + 1):BLOCK_SIZE * (i + 2)]),
        corrupted_plaintext[BLOCK_SIZE * (i + 1):BLOCK_SIZE * (i + 2)])

    crypt = AES.new(key, AES.MODE_ECB)

    # Getting the corrupted cipher and fixing it
    ct_i = byte_xor(cipher[(i + 1) * BLOCK_SIZE: (i + 2) * BLOCK_SIZE], bit_to_flip)

    # Return the fixed plain-text block (using the previous cipher-text block)
    return byte_xor(crypt.decrypt(ct_i), cipher[i * BLOCK_SIZE: (i + 1) * BLOCK_SIZE])
