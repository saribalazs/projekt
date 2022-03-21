import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1250))
s.listen(2)
lista = [i for i in range(25) if i % 2 ==0]
#with open('data.txt','w') as f:
 #   f.write(str(lista))

#file = open('./data.txt',"r")
#data = file.read()

while True:
    clientsocket, adress = s.accept()
    print(f'connection estabilished from {adress}')
    clientsocket.send(bytes(str(lista),'utf-8'))