def execute_command(command):
    if command == 'ls':
        print('$ listing files')
    elif command == 'cd':
        print('$ changing directory')
    else:
        print('$ command not implemented')
    print('.... rest of the code')


def execute_command_PM(command):
    match command:
        case 'ls':
            print('$ listing files')
        case 'cd':
            print('$ changing directory')
        case _:  # Não obrigatório
            print('$ command not implemented')
    print('.... rest of the code')


def execute_command2(command):
    match command.split():
        case['ls', path]:
            print('$ listing files from', path)
        case['cd', path]:
            print('$ changing directory to', path)
            
execute_command2('ls /home/gelinski')