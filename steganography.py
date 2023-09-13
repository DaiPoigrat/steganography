from itertools import zip_longest


class Steganography:
    def __init__(self):
        self.ru_letters = 'АВЕКМНОРСТХаеорсух'
        self.en_letters = 'ABEKMHOPCTXaeopcyx'

        self.container_data = ''
        self.message_data = ''
        self.stego_data = ''

    def _encode(self):
        if isinstance(self.message_data, str):
            encoded_text = ''.join(format(ord(char), 'b') for char in self.message_data)
        else:
            encoded_text = ''.join(format(char, 'b') for char in self.message_data)

        encoded_byte_list = [char for char in encoded_text]

        result_text = ''
        index_counter = -1
        for char in self.container_data:
            index_counter += 1
            if not encoded_byte_list:
                result_text += self.container_data[index_counter:]
                break

            if char not in self.en_letters:
                result_text += char
                continue

            byte = encoded_byte_list.pop(0)

            if byte == '0':
                result_text += char
                continue

            char_index = self.en_letters.index(char)
            ru_char = self.ru_letters[char_index]

            result_text += ru_char

        self.stego_data = result_text

    def _decode(self):
        str_of_bytes = ''

        for char in self.stego_data:
            if char in self.ru_letters:
                str_of_bytes += '1'

            if char in self.en_letters:
                str_of_bytes += '0'

        finish = False
        while not finish:
            if len(str_of_bytes) > 8:
                binary_char = str_of_bytes[:8]
                str_of_bytes = str_of_bytes[8:]
                print(f'{binary_char = }')
                char = chr(int(binary_char, 2)).decode('hex').decode('utf-8')
            else:
                finish = True
