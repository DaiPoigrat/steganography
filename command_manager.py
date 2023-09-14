import sys

from steganography import Steganography


class CMDManager(Steganography):
    def __init__(self):
        super().__init__()
        self.container_path = ''
        self.message_path = ''
        self.stego_path = ''
        self.decoded_message_path = ''

    @staticmethod
    def help_command(module_type: str):
        """
        printing help information
        :param module_type: 'put' or 'get'
        :return:
        """
        if module_type == 'put':
            print('Command list:')
            print('-h --help\tcommand list')
            print('-m --message\tpath to input message file')
            print('-s --stego\tpath to output stego container')
            print('-c --container\tRequired! path to container file')
        if module_type == 'get':
            print('Command list:')
            print('-h --help\tcommand list')
            print('-m --message\tpath to output message file')
            print('-s --stego\tpath to input stego container')
        else:
            print('Module type error!')
            sys.exit()

    def container_command(self):
        with open(f'{self.container_path}', 'r') as file:
            self.container_data = file.read()

    def message_command(self):
        if not self.message_path:
            self.message_data = input()
            return

        with open(f'{self.message_path}', 'rb') as file:
            self.message_data = file.read()

    def message_command_decode(self):
        self._decode()

        if not self.decoded_message_path:
            print(self.decoded_message)
            return

        with open(f'{self.decoded_message_path}', 'w') as file:
            file.write(self.decoded_message)

    def stego_command(self):
        self._encode()

        if not self.stego_path:
            print(self.stego_data)
            return

        with open(f'{self.stego_path}', 'w') as file:
            file.write(self.stego_data)

    def stego_command_decode(self):
        if not self.stego_path:
            self.stego_data = input()
            return
        with open(f'{self.stego_path}', 'r') as file:
            self.stego_data = file.read()

    def encode(self):
        # читаем контейнер
        self.container_command()
        # читаем сообщение
        self.message_command()
        # шаманим данные
        self.stego_command()

    def decode(self):
        self.stego_command_decode()
        self.message_command_decode()
