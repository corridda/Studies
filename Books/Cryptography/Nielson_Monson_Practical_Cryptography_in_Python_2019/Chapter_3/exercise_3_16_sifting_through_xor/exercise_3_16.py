import json


def xor_data(data_1: bytes, data_2: bytes):
    """XOR the data_1 with the data_2.

    :param data_1: bytes
    :param data_2: bytes
    """
    return bytes(pair[0] ^ pair[1] for pair in zip(data_1, data_2))


if __name__ == '__main__':
    # Plain text - XML
    m1_path = '../exercise_3_15_riding_the_keystream/message_1.txt'
    m2_path = '../exercise_3_15_riding_the_keystream/message_2.txt'

    with open(m1_path, 'rb') as m1:
        plaintext_1 = m1.read()
        with open(m2_path, 'rb') as m2:
            plaintext_2 = m2.read()
            print(f"xor_data(plaintext_1, plaintext_2):\n{xor_data(plaintext_1, plaintext_2)}\n")

    # JSON
    with open('first.json', 'rb') as j1:
        json_1 = bytes(json.dumps(json.load(j1)), encoding='utf-8')
        with open('second.json', 'rb') as j2:
            json_2 = bytes(json.dumps(json.load(j2)), encoding='utf-8')
            print(f"xor_data(json_1, json_2):\n{xor_data(json_1, json_2)}\n")