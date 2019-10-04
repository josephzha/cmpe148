import socket;

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    sentence = input("enter a sentence: ")
    sentence += " "
    tup = (socket.gethostname(),1949)
    arr = bytes(sentence,'utf-8')
    s.sendto(arr,tup)
    data,addr = s.recvfrom(1024)
    print(data.decode("utf-8"))
    




