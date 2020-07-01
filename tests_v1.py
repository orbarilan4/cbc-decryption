from project import cbc_custom_decrypt


testsing_dict_decrypt = [{
        "key": b"1111111111111111",
        "iv": b"2222222222222222",
        "plain": [b"hello to you!, task completed!!!", b"you can make your day abcdefpoqa"],
        "cipher": [b"\xae('\x17\xc0<\xcan%\x83\xdf\xae\xddg\xf3\x864\x97\xa3\xc9\x01\x81a\x9e\x0b\x96\x05\x0f\xc3P\x8b\x06",
                   b'\x11\xb3\x8e\xb3,/\x92\x01\x9b\x97\x8b\x05\xdd\xa9\xc6\xebl\xbc\x98\xd80p\x10\xf9o\xfc\x89^p\xd1V\x99']
    },
    {
        "key": b"1123411115461190",
        "iv": b"9122622795742201",
        "plain": [b"hello to you!, task completed!!!", b"you can make your day abcdefpoqa"],
        "cipher": [b'\xeb+\xd0\xd2\x04\x9d\x9b\x0c\xe3Dez\xff\x03\xdfd\xa8\x9f{3&5P\x95\xf5\x15*x\xdc!\x978',
                   b'0\x94\x9e6\xb6\xf2+\xaeMyb\x1f\x94\xea\xcd\x84s\x98\x99\xe0\xda`U\x8d6\x91\x1a\x00S\x7f{=']
    }
]


def testing_decrypt(testsing_dict):
    errors = 1
    test_num = 1
    for test in testsing_dict:
        key, iv = test["key"], test["iv"]
        for plain_text, c in zip(test["plain"], test["cipher"]):
            num_of_blocks = len(c) // 16
            my_output = cbc_custom_decrypt(key, num_of_blocks, iv + c)
            if my_output != plain_text:
                print("Error #{} in Test #{}".format(errors, test_num))
                print("in: {}\n\tplain text should be: {}\n\tcipher is: {}\n".format(errors, my_output, plain_text, c))
                errors += 1
            else:
                print("Passed Test #{}".format(test_num))
            test_num+=1
    if errors == 1:
        print("Passed The Test: testing_decrypt")
    else:
        print("Didn't Pass The Test")


if __name__ == "__main__":
    testing_decrypt(testsing_dict_decrypt)
