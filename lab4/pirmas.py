'''1. Enigma  šifro (be atspindžio) raktas =[24, 5]
Rotoriai:
 L_1=[10, 2, 21, 18, 23, 6, 16, 14, 8, 11, 1, 25, 15, 20, 0, 24, 17, 19, 22, 5, 4, 3, 9, 12, 13, 7]
 L_2=[10, 2, 11, 18, 8, 20, 19, 25, 23, 1, 15, 9, 14, 6, 24, 0, 17, 7, 22, 21, 4, 12, 5, 3, 16, 13]
Iššifruokite šifrą 
DZDSD QWAWP VUYIF ZHTCN WCIKW 
IGRNO YKBXL WYVLP NIRFZ RUQIW 
SHBVC NRGAZ GLPAU FGWGB GMMCD 
UXJVC ABRPN GCFFO OICSK RNDCX 
UCYHQ AKOAC BJZBA SWXRI JTURK 
ZZPWV SPIES JDDOF KLCNO DEIGA 
IDUBG IAZNB CWXEI AMBMC UEJMR 
VNTSR ZOGHV UWZQM NTUFW HVCEK 
IQWSU XWVKK JLEDG RLRXU VREBL 
BCZKS AJLUV '''

cp=u'''DZDSD QWAWP VUYIF ZHTCN WCIKW 
IGRNO YKBXL WYVLP NIRFZ RUQIW 
SHBVC NRGAZ GLPAU FGWGB GMMCD 
UXJVC ABRPN GCFFO OICSK RNDCX 
UCYHQ AKOAC BJZBA SWXRI JTURK 
ZZPWV SPIES JDDOF KLCNO DEIGA 
IDUBG IAZNB CWXEI AMBMC UEJMR 
VNTSR ZOGHV UWZQM NTUFW HVCEK 
IQWSU XWVKK JLEDG RLRXU VREBL 
BCZKS AJLUV'''

abc='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n=len(abc)

[k1,k2]  =[24, 5] #initial positions of the rotors
L_1=[10, 2, 21, 18, 23, 6, 16, 14, 8, 11, 1, 25, 15, 20, 0, 24, 17, 19, 22, 5, 4, 3, 9, 12, 13, 7]
L_2=[10, 2, 11, 18, 8, 20, 19, 25, 23, 1, 15, 9, 14, 6, 24, 0, 17, 7, 22, 21, 4, 12, 5, 3, 16, 13]

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

# def encrf(c,k,k1,k2): #encription and decription with reflector | can be 
#     c=encr(c,k,k1,k2)
#     c=s[c] #reflection
#     return dencr(c,k,k1,k2)

result=u''
for i in range(0, len(cpn)):
    result+=abc[dencr(cpn[i], i,k1,k2)]

print(result)
