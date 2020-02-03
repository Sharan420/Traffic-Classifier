import socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('192.168.43.64', 4345))
serversocket.listen(1)


while True:
    clientsocket,addr = serversocket.accept()
    print("Got a connection from {}".format(addr))
    msg = clientsocket.recv(1024)
    al = msg.decode('ascii')
    al = str(al)
    print(al)
    al = eval(al)

    if al[0] > al[1]:
        clientsocket.send("GREEN".encode('ascii'))
    else:
        clientsocket.send("RED".encode('ascii'))
