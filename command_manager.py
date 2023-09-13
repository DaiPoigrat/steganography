from steganography import Steganography


class CMDManager(Steganography):
    def __init__(self):
        super().__init__()
        self.container_path = ''
        self.message_path = ''
        self.stego_path = ''

    @staticmethod
    def help_command():
        print('Command list:')
        print('-h --help\tcommand list')
        print('-m --message\tpath to message file')
        print('-s --stego\tpath to stego container')
        print('-c --container\tRequired! path to container file')

    def container_command(self):
        with open(f'{self.container_path}', 'r') as file:
            self.container_data = file.read()

        # print(f'{self.container_data = }')

    def message_command(self):
        if not self.message_path:
            self.message_data = input()
            return

        with open(f'{self.message_path}', 'rb') as file:
            self.message_data = file.read()

    def stego_command(self):
        self._encode()

        if not self.stego_path:
            print(self.stego_data)
            return

        with open(f'{self.stego_path}', 'w') as file:
            file.write(self.stego_data)

    def start(self):
        # читаем контейнер
        self.container_command()
        # читаем сообщение
        self.message_command()
        # шаманим данные
        self.stego_command()

        self._decode()
