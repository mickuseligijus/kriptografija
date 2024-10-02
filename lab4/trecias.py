'''3. Enigma  šifro (su atspindžiu) raktas =[7, 24]
Rotoriai:
 L_1=[10, 2, 21, 18, 23, 6, 16, 14, 8, 11, 1, 25, 15, 20, 0, 24, 17, 19, 22, 5, 4, 3, 9, 12, 13, 7]
 L_2=[10, 2, 11, 18, 8, 20, 19, 25, 23, 1, 15, 9, 14, 6, 24, 0, 17, 7, 22, 21, 4, 12, 5, 3, 16, 13]
Atspindžio keitinys s=[2, 4, 0, 6, 1, 11, 3, 8, 7, 13, 16, 5, 15, 9, 18, 12, 10, 19, 14, 17, 25, 22, 21, 24, 23, 20]
Iššifruokite šifrą 
RBKZF IHOGN LRJDD TVWFT GSEDH 
DWDLO FOOFB GVCOM TPGVZ ATDQD 
SUHTE WONIB TDOEG SOVAR DYWNZ 
ECABQ OFKDI TZSNU PXKSS WMLFJ 
OIAZF DSWVN AZFWZ WUYDH ZIPDL 
QWPWW OOOOQ FVBHV IDZJS CMGEI 
IQTLU QMZIK NSFVM CYEVH JHOLN 
DAIZM TVWJJ QOGIB SRAIH EHQDB 
JNIJQ QWOML MTXDJ TEUZL JKDUA 
DBMUF FDRWH NJQEV PGUWE OGYIN 
CDGZA PBMUB TCDSB RVZLQ OBSVF 
PNBBL NLMIL BUTAX URDEH EIXBX 
QMTGU TUZXM EQPYV ODEYF WZWLZ 
ANCMF UQFOA HYUAU BVEQK RMDCN 
NXGPL TUPHW KNELM KMZXI FOCMM 
LUCXV NUEVO JWZWG IMCLX BBDVG 
CXLPE KDJKB PCPBQ AROUE XB'''

cp=u'''RBKZF IHOGN LRJDD TVWFT GSEDH 
DWDLO FOOFB GVCOM TPGVZ ATDQD 
SUHTE WONIB TDOEG SOVAR DYWNZ 
ECABQ OFKDI TZSNU PXKSS WMLFJ 
OIAZF DSWVN AZFWZ WUYDH ZIPDL 
QWPWW OOOOQ FVBHV IDZJS CMGEI 
IQTLU QMZIK NSFVM CYEVH JHOLN 
DAIZM TVWJJ QOGIB SRAIH EHQDB 
JNIJQ QWOML MTXDJ TEUZL JKDUA 
DBMUF FDRWH NJQEV PGUWE OGYIN 
CDGZA PBMUB TCDSB RVZLQ OBSVF 
PNBBL NLMIL BUTAX URDEH EIXBX 
QMTGU TUZXM EQPYV ODEYF WZWLZ 
ANCMF UQFOA HYUAU BVEQK RMDCN 
NXGPL TUPHW KNELM KMZXI FOCMM 
LUCXV NUEVO JWZWG IMCLX BBDVG 
CXLPE KDJKB PCPBQ AROUE XB'''

abc='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n=len(abc)

[k1,k2]  =[7, 24] #initial positions of the rotors
L_1=[10, 2, 21, 18, 23, 6, 16, 14, 8, 11, 1, 25, 15, 20, 0, 24, 17, 19, 22, 5, 4, 3, 9, 12, 13, 7]
L_2=[10, 2, 11, 18, 8, 20, 19, 25, 23, 1, 15, 9, 14, 6, 24, 0, 17, 7, 22, 21, 4, 12, 5, 3, 16, 13]
#20 is connected to the 8, 3 is connected to the 13
s=[2, 4, 0, 6, 1, 11, 3, 8, 7, 13, 16, 5, 15, 9, 18, 12, 10, 19, 14, 17, 25, 22, 21, 24, 23, 20]
L_1a=[L_1.index(i) for i in range(0,len(L_1))]
L_2a=[L_2.index(i) for i in range(0,len(L_2))]

def prep(t):
    tn=''
    for r in t:
        if r in abc: tn+=r
    return [abc.index(r) for r in tn]

cpn=prep(cp)
def rotor(a,m,lb): #leter a, rotor,
    c=(a+m)%n
    c=lb[c]
    return (c-m)%n

def encr(r,k,k1,k2): #letter, the index of letter | letter r in position k - cp tekste
    # print(k1,k2)
    m1=k%n
    m2=(k-m1)//n
    m1=m1+k1
    m2=m2+k2
    c=rotor(r,m1,L_1)
    return rotor(c,m2,L_2)

def dencr(c,k,k1,k2): #letter, the index of letter | letter r in position k
    m1=k%n
    m2=(k-m1)//n
    m1=m1+k1
    m2=m2+k2
    c=rotor(c,m2,L_2a)
    return rotor(c,m1,L_1a)

# print(encr(0,124,2,14))
# print(dencr(14,124,2,14))

def encrf(c,k,k1,k2): #encription and decription with reflector | can be 
    c=encr(c,k,k1,k2)
    c=s[c] #reflection
    return dencr(c,k,k1,k2)

result=u''
for i in range(0, len(cpn)):
    result+=abc[encrf(cpn[i], i,k1,k2)]

print(result)
