'''2. Enigma  šifro (be atspindžio) rakto pirma dalis =15
Rotoriai:
 L_1=[10, 2, 11, 18, 8, 20, 19, 25, 23, 1, 15, 9, 14, 6, 24, 0, 17, 7, 22, 21, 4, 12, 5, 3, 16, 13]
 L_2=[14, 2, 7, 20, 18, 9, 19, 25, 23, 1, 13, 17, 22, 5, 3, 0, 24, 8, 21, 10, 11, 12, 15, 4, 6, 16]
Pirma teksto raidė=G
Iššifruokite šifrą 
CELKY IZIVB IVJQF ZWQGV ZIIAR 
TCPVR STOLQ MRMZY WKMHM GKLUY 
BGYWJ HEQAF NXCLL RYBSJ YAXUI 
SHUCA NIAZB NKMDB SPVOT NMFLS 
WHWBD DJIHP SXUJZ RCHEW ZCIWM 
RPZYO VCOJT SMFBK GTITD XNYMA 
HVNWI GSGMJ BTWVN IRMRA AYZJQ 
DTTYQ MAOYB MQORN WTYKN ELLQQ 
FPBGD LOZZW EVOOF NMWOS QNUMB 
RGLFD MZJPX'''

cp='''CELKY IZIVB IVJQF ZWQGV ZIIAR 
TCPVR STOLQ MRMZY WKMHM GKLUY 
BGYWJ HEQAF NXCLL RYBSJ YAXUI 
SHUCA NIAZB NKMDB SPVOT NMFLS 
WHWBD DJIHP SXUJZ RCHEW ZCIWM 
RPZYO VCOJT SMFBK GTITD XNYMA 
HVNWI GSGMJ BTWVN IRMRA AYZJQ 
DTTYQ MAOYB MQORN WTYKN ELLQQ 
FPBGD LOZZW EVOOF NMWOS QNUMB 
RGLFD MZJPX '''

abc='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n=len(abc)
k1=15
L_1=[10, 2, 11, 18, 8, 20, 19, 25, 23, 1, 15, 9, 14, 6, 24, 0, 17, 7, 22, 21, 4, 12, 5, 3, 16, 13]
L_2=[14, 2, 7, 20, 18, 9, 19, 25, 23, 1, 13, 17, 22, 5, 3, 0, 24, 8, 21, 10, 11, 12, 15, 4, 6, 16]

L_1a=[L_1.index(i) for i in range(0,n)]
L_2a=[L_2.index(i) for i in range(0,n)]

def prep(t):
    tn=''
    for r in t:
        if r in abc: tn+=r
    return [abc.index(r) for r in tn]

cpn=prep(cp)
def rotor(a,m,lb):
    c=(a+m)%n
    c=lb[c]
    return (c-m)%n

def encr(r,k,k1,k2):
    m1=k%n
    m2=(k-m1)//n
    m1=m1+k1
    m2=m2+k2
    c=rotor(r,m1,L_1)
    return rotor(c,m2,L_2)

def dencr(c,k,k1,k2):
    m1=k%n
    m2=(k-m1)//n
    m1=m1+k1
    m2=m2+k2
    c=rotor(c,m2,L_2a)
    return rotor(c,m1,L_1a)


for y in range(0,n):
    result=''
    for i in range(0, len(cpn)):
        result+=abc[dencr(cpn[i], i,k1,y)]
    print(y,' ', result,'\n')
    





                   