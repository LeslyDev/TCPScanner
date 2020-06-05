import psutil


def get_list_open_ports(start, end):
    used_ports = []
    open_ports_in_range = []
    connections = psutil.net_connections()
    for connection in connections:
        if str(connection.type) == "SocketKind.SOCK_STREAM":
            used_ports.append(connection.laddr[1])
    for i in range(start, end, 1):
        if i not in used_ports:
            open_ports_in_range.append(i)
    if len(open_ports_in_range) != 0:
        return open_ports_in_range
    return "Все порты в этом диапазоне заняты"


s = int(input("Введите начало диапазона \n"))
e = int(input("Введите конец диапазона \n"))
print(get_list_open_ports(s, e))
