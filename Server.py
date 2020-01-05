import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), 4345))
serversocket.listen(1)

#for i in range(100):
while True:
    clientsocket,addr = serversocket.accept()
    print("Got a connection from {}".format(addr))
    msg = clientsocket.recv(1024)
    al = msg.decode('ascii')
    al = str(al)
   # msg1 = 'Thank you for connecting'+ al
   # clientsocket.send(msg1.encode('ascii'))
    print(al)
    clientsocket.close()
