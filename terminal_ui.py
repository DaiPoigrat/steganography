import sys

from command_manager import CMDManager


def get_command_list():
    command_list = sys.argv[1:]

    manager = CMDManager()

    if '-h' in command_list or '--help' in command_list:
        manager.help_command()
        return sys.exit()

    if len(command_list) < 2:
        print('Wrong set of parameters!')
        return sys.exit()

    if '-c' not in command_list and '--container' not in command_list:
        print('Can`t find required parameter -c (--container)!')
        return sys.exit()

    use_container_command = False
    use_message_command = False
    use_stego_command = False

    while len(command_list) > 0:
        try:
            arg = command_list.pop(0)

            if arg.startswith('-'):
                match arg:
                    case '-c' | '--container':
                        if not use_container_command:
                            path_to_container = command_list.pop(0)
                            manager.container_path = path_to_container
                            use_container_command = True

                    case '-s' | '--stego':
                        if not use_stego_command:
                            path_to_stego = command_list.pop(0)
                            manager.stego_path = path_to_stego
                            use_stego_command = True

                    case '-m' | '--message':
                        if not use_message_command:
                            path_to_message = command_list.pop(0)
                            manager.message_path = path_to_message
                            use_message_command = True

        except Exception as e:
            print(f'CODE EXCEPTION: {e = }')

    manager.start()


if __name__ == '__main__':
    get_command_list()
