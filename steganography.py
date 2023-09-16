import sys
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
        # byte_code = format(unicode_char, '08b')

        temp = 8 - len(byte_code)
        if temp != 0:
            byte_code = '0' * temp + byte_code

        return byte_code

    def _encode(self):
        # '0' - eng
        # '1' - ru
        if isinstance(self.message_data, str):
            encoded_text = ''.join(self.convert_to_byte_code(ord(char)) for char in self.message_data)
        else:
            encoded_text = ''.join(self.convert_to_byte_code(char) for char in self.message_data)

        encoded_text += '11111111'

        encoded_byte_list = [char for char in encoded_text]

        result_text = ''
        index_counter = -1
        for char in self.container_data:
            index_counter += 1
            if not encoded_byte_list:
                result_text += self.container_data[index_counter:]
                break

            is_ru = char in self.ru_letters
            is_en = char in self.en_letters
            if not is_en and not is_ru:
                result_text += char
                continue

            byte = encoded_byte_list.pop(0)

            print(byte, char, ord(char), file=sys.stderr)

            if byte == '0':
                if is_ru:
                    char_index = self.ru_letters.index(char)
                    en_char = self.en_letters[char_index]
                    result_text += en_char
                else:
                    result_text += char

            elif byte == '1':
                if is_en:
                    char_index = self.en_letters.index(char)
                    ru_char = self.ru_letters[char_index]
                    result_text += ru_char
                else:
                    result_text += char
            else:
                result_text += char

            print('put "{}" : {}'.format(result_text[-1], ord(result_text[-1])))


        self.stego_data = result_text

    def _decode(self):
        str_of_bytes = ''

        for char in self.stego_data:
            if char in self.ru_letters:
                str_of_bytes += '1'

            if char in self.en_letters:
                str_of_bytes += '0'

        # print(f'{str_of_bytes = }')

        result_string = []
        while True:
            if len(str_of_bytes) > 8:
                binary_char = str_of_bytes[:8]

                str_of_bytes = str_of_bytes[8:]
                unicode_char = int(binary_char, base=2)
                result_string.append(unicode_char)
            else:
                break

        i = len(result_string) - 1
        while i >= 0 and result_string[i] == 0:
            i -= 1

        import sys
        print(f'{result_string = }', file=sys.stderr)

        result_string = result_string[0:i]

        print(f'{result_string = }', file=sys.stderr)

        self.decoded_message = bytes(result_string)
