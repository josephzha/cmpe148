import socket;

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1949))
msg = s.recv(1024)
print(msg.decode("utf-8"))
while True:
    sentence = input("enter a sentence: ")
    sentence += " "
    s.send(bytes(sentence,"utf-8"))
    response = s.recv(1024)
    print(response.decode("utf-8"))




