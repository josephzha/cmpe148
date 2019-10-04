import socket;

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1949))
s.listen(5)


while True:
    clientsocket, address = s.accept()
    print(f"connection from {address} has been established")
    clientsocket.send(bytes("welcome to the server","utf-8"))
    while True:
        data = clientsocket.recv(1024)
        sentence = data.decode("utf-8")
        res = ""
        start = 0
        while start<len(sentence) and sentence[start]==' ':
            start += 1
        for i in range(start,len(sentence)):
            if sentence[i]==' ':
                if sentence[i-1]!= ' ':
                    append = i - start
                    res+= str(append)
                    start = i+1
                    res += " "
                else:
                    start = i+1
        clientsocket.send(bytes(res,"utf-8"))
