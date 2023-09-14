from itertools import zip_longest


class Steganography:
    def __init__(self):
        self.ru_letters = 'АВЕКМНОРСТХаеорсух'
        self.en_letters = 'ABEKMHOPCTXaeopcyx'

        self.container_data = ''
        self.message_data = ''
        self.stego_data = ''
        self.decoded_message = ''

    @staticmethod
    def convert_to_byte_code(unicode_char):
        byte_code = format(unicode_char, 'b')

        temp = 8 - len(byte_code)
        if temp != 0:
            byte_code = '0' * temp + byte_code

        return byte_code

    def _encode(self):
        if isinstance(self.message_data, str):
            encoded_text = ''.join(self.convert_to_byte_code(ord(char)) for char in self.message_data)
        else:
            encoded_text = ''.join(self.convert_to_byte_code(char) for char in self.message_data)

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

        result_string = ''
        while True:
            if len(str_of_bytes) > 8:
                binary_char = str_of_bytes[:8]

                if binary_char == '00000000':
                    break

                str_of_bytes = str_of_bytes[8:]
                unicode_char = int(binary_char, base=2)
                char = chr(unicode_char)
                result_string += char
            else:
                break

        self.decoded_message = result_string
