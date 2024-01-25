import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('37.59.31.202', 2000))
msg = s.recv(1024)
print(msg.decode('utf-8'))
s.send(bytes('3', 'utf-8'))
a = 0
msg = s.recv(1024)
print(msg.decode('utf-8'))


def Equilibrage(x):
    if type(x) != 'list' : x = list(x)
    if len(x) != 0 :
        if (x[-1] == '\n') : x.pop()
    symboleTot = ["[]","{}","()"]
    i = 0
    for i in range(len(x)):
    
        if i == len(x) -1 : break
        if len(x) - i < 0 : break
        if i + 1 > len(x): break
        doubles = x[i] + x[i+1]       
        if doubles in symboleTot:
            x.pop(i)
            x.pop(i)
        else: 
            continue
    if( Verif(x)== False):
        if(len(x) == 0):
            return "True"
        else: 
            return "False"
    else: return Equilibrage(x)


def Verif(laValue):
    symboleTot = ["[]","{}","()"] 
    for i in range(len(laValue)):
        if i == len(laValue) -1 : break
        doubles = laValue[i] + laValue[i+1]
        if doubles in symboleTot:
            return True
    return False


while True:
    msg = s.recv(1024)
    msg = msg.decode("utf-8")
    print(msg)
    if (msg.startswith("Erreur")) : break
    if (msg.startswith("Felicitations")) : break
    lemsg = str(msg)
    g = Equilibrage(str(lemsg))
    print(g)
    s.send(bytes(g,'utf-8'))