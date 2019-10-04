import socket;

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((socket.gethostname(),1949))

while True:
    data, address = s.recvfrom(1024)
    sentence = data.decode("utf-8")
    res = ""
    start = 0
    while start<len(sentence) and sentence[start]==' ':
        start += 1
    for i in range(start,len(sentence)):
        if sentence[i]==' ':
            if sentence[i-1] != ' ':
                append = i - start
                res+= str(append)
                start = i+1
                res += " "
            else:
                start = start +1
    s.sendto(bytes(res,"utf-8"),address)
