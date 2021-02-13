
clients = 'pablo,ricardo,'

def create_client(client_name):
    global clients

    clients += client_name
    _add_comma()


def list_clients():
    global clients

    print(clients)

def update_client(client_name, update_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', update_client_name + ',')
    else:
        print('Clients is not in clients list')

def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        print('Client is not in clients list')

def search_client(client_name):
    clients_list = clients.split(',')

    for client in clients_list:
        if client != client_name:
            continue
        else:
            return True

def _add_comma():
    global clients

    clients += ","


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[L]ist client')
    print('[D]elete client')
    print('[S]earch client')

def _get_client_name():
    return input('What is the client name?')

if __name__ == '__main__':
    _print_welcome()

    commad = input()
    commad = commad.upper()  #Sirve para que al pedir llos valores sean em mayuscula

    if commad == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif commad == 'L':
        list_clients()
    elif commad == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif commad == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print('The client is in the client\'s list')
        else:
            print('The client:{} is not in our client\'s list'.format(client_name))


    elif commad == 'U':
        client_name = _get_client_name()
        update_client_name = input('What is the update client name?')
        update_client(client_name, update_client_name)
        list_clients()
        pass
    else:
        print('Invalid command')
