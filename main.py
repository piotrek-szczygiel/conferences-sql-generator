import sys

from client import *

if __name__ == '__main__':
    commands = [
        delete_clients(),
        insert_clients(100)
    ]

    result = '\n\n'.join(commands)

    if len(sys.argv) == 2:
        file_name = sys.argv[1]
        with open(file_name, 'wb') as file:
            file.write(result.encode('utf-8'))
    else:
        print(result)
