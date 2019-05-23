import random
#ku zairu wan cheng
print("Das ist XOSpielen\n")
# chang liang
X = "X"
O = "O"
KONG = "*"
SIGE = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
B_S = [5,1,3,7,9,2,4,6,8]
# qi pan lei
class Qipan:
    def __init__(self,heng,zong):
        self.heng = heng
        self.zong = zong
        self.platte = []
    def neu_platte(self):
        for a in range(self.heng*self.zong):
            self.platte.append(KONG)
    def zeichnen_platte(self):
        print("\n")
        platte_as = qp.platte[:]
        platte_h = []
        for i in range(len(self.platte)):
            if self.platte[i] == KONG:
                platte_as[i] = i+1
        for z in range(self.zong):# mei hua wai guan ---
            platte_h = ""
            for h in range(self.heng):
                platte_h += str(platte_as[(z*self.heng)+h])
                if h < (self.heng-1):
                    platte_h += " | "# mei hua wai guan jie shu ---
            print("\t",platte_h)
            if z < (self.zong-1):
                print("\t","----------")
        self.f_s()
        print("\nFrei Stelle:",fs.platte)
    def f_s(self):
        fs.platte = []
        for s in range(self.heng*self.zong):
            if self.platte[s] == KONG:
                fs.platte.append(s+1)
# gui ze lei
def zwei():
    for r in SIGE:
        if qp.platte[r[0]] == qp.platte[r[1]] != KONG:
            zweit = qp.platte[r[0]]
            return zweit
        if qp.platte[r[1]] == qp.platte[r[2]] != KONG:
            zweit = qp.platte[r[1]]
            return zweit
        if qp.platte[r[0]] == qp.platte[r[2]] != KONG:
            zweit = qp.platte[r[0]]
            return zweit
def op_sieg():
    for r in SIGE:
        if qp.platte[r[0]] == qp.platte[r[1]] == qp.platte[r[2]] != KONG:
            sieger = qp.platte[r[0]]
            return sieger
    if KONG not in qp.platte:
        return "K"
    return False
def ntun(tun):
    if tun == X:
        return O
    else:
        return X
def end():
    gewinner = op_sieg()
    if gewinner == com.spit:
        print("Computer sieg !\n")
    elif gewinner == spi.spit:
        print("Sie sieg !\n")
    elif gewinner == "K":
        print("Kein man sieg.  ---end \n")
# wan jia lei
class Spieler:
    def __init__(self,AI):
        self.spit = None
        self.AI = AI
        self.mi = 1
        self.ma = 10
    def frage_ja_nein(self,fragennn):
        self.res=None;
        while self.res not in("j","n"):
            self.res=str(input(fragennn)).lower()
        return self.res
    def input_nume(self,fragennn):
        self.res=None
        while self.res not in range(self.mi,self.ma):
            self.res=int(input(fragennn))
        return self.res
    def xuan_ze(self):
        gehen_zuerst=spi.frage_ja_nein("erst:(jn)")
        if gehen_zuerst=="j":
            print("\nSie zu erst.")
            spi.spit=X
            com.spit=O
        else:
            print("\nIch gehe erst.")
            com.spit=X
            spi.spit=O
    def gehen(self):
        if self.AI == 1:
            for s in fs.platte:
                qp.platte[s-1] = com.spit
                if op_sieg() == com.spit:
                    print("Ich gehe ...",s)
                    return
                else:
                    qp.platte[s-1] = KONG
            for s in fs.platte:
                qp.platte[s-1] = spi.spit
                if op_sieg() == spi.spit:
                    print("Ich gehe ...",s)
                    qp.platte[s-1] = com.spit
                    return
                else:
                    qp.platte[s-1] = KONG
            for s in B_S:
                if s in fs.platte:
                    print("Ich gehe ...",s)
                    qp.platte[s-1] = com.spit
                    break
        elif self.AI == 0:
            s = None
            while s not in fs.platte:
                s = self.input_nume("Wo gehen Sie ? (1-9)")
                if s not in fs.platte:
                    print("Es gibt kein mehr Platz.")
                qp.platte[s-1] = spi.spit
        elif self.AI == 2:
            for s in fs.platte:
                qp.platte[s-1] = com.spit
                if op_sieg() == com.spit:
                    print("Ich gehe ...",s)
                    return
                else:
                    qp.platte[s-1] = KONG
            for s in fs.platte:
                qp.platte[s-1] = spi.spit
                if op_sieg() == spi.spit:
                    print("Ich gehe ...",s)
                    qp.platte[s-1] = com.spit
                    return
                else:
                    qp.platte[s-1] = KONG
            for s in fs.platte:
                qp.platte[s-1] = com.spit
                if zwei() == com.spit:
                    print("Ich gehe ...",s)
                    return
                else:
                    qp.platte[s-1] = KONG
            for s in B_S:
                if s in fs.platte:
                    print("Ich gehe ...",s)
                    qp.platte[s-1] = com.spit
                    break
        elif self.AI == 3:
            s3 = random.choice(fs.platte)
            if s3 in fs.platte:
                print("Ich gehe ... ",s3)
                qp.platte[s3-1] = com.spit

# zhu han shu
tun = X
qp=Qipan(3,3)
fs=Qipan(0,0)
qp.neu_platte()
qp.zeichnen_platte()
spi=Spieler(0)
com=Spieler(1)
c = int(input("LEVEL des Computer (1-3)"))
if c == 2:
    com.AI = 2
elif c == 3:
    com.AI = 3
spi.xuan_ze()
while not op_sieg():
    if tun == spi.spit:
        spi.gehen()
    else:
        com.gehen()
    qp.zeichnen_platte()
    tun = ntun(tun)
end()
# jian cha 
input()
