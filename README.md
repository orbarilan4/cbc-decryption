# CBC Decryption
Contains two main things:
* `cbc_custom_decrypt(key, n, cipher)` function is implementation of CBC decryption by using only ECB decryption.
* Suppose that bit number j of block ci of the ciphertext got flipped (namely, if
the original value of the bit was 0 then it changed to 1, and if the original value
of the bit was 1 then it changed to 0). The decryption
process will decrypt all blocks correctly, except for blocks i and i + 1. The
decryption of block i will be completely random, and the decryption of block
i + 1 will be correct, except for bit j in this block that will be flipped. `cbc_flip_fix(key, n, cipher)` function gets the original value of the block whose encryption was completely corrupted (by definition)
