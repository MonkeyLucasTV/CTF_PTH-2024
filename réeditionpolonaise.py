import socket

def Equation(x):
    x = list(x)
    symbole = ["*", "+", "-"]    
    IEC = 0                         #IndiceEmplacementCaractere
    for Character in x:                                                                 # Analyse du type de caractere
        if Character in symbole:
            EmplacementMax = IEC                                 #Emplacement Max du dernier caractere
        else:
            pass
        IEC += 1
    LaVal1 = x[EmplacementMax+1]
    LOperateur = x[EmplacementMax]
    LeCalc = LaVal1 + LOperateur + x[EmplacementMax+2]
    LeCalcResul = eval(LeCalc)
    xdelta = x
    xdelta[EmplacementMax:EmplacementMax+3] = [] 
    xdelta.insert(EmplacementMax,str(LeCalcResul))
    salut = ''
    if(xdelta[0] in symbole):
        return Equation(xdelta)
    else:
        for i in xdelta:
            salut += str(i)
        return(salut)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('37.59.31.202', 2000))
msg = s.recv(1024)
print(msg.decode('utf-8'))
s.send(bytes('2', 'utf-8'))
a = 0
msg = s.recv(1024)
print(msg.decode('utf-8'))
print(msg.decode('utf-8'))
print("Truc", msg.decode('utf-8'))


while(True):
    msg = s.recv(1024)
    a = msg.decode('utf-8')
    a = a.replace(" ", "")
    print("a : ", a)
    if a.startswith("Felicitations!"): break
    g = Equation(a)
    print("voici equation : ", g)
    s.send((bytes(g,'utf-8')))
    msg = msg.decode('utf-8')
    print(msg)


    
    

    








