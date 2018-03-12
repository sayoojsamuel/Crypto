from N1ES import N1ES
import base64
import string
key = "wxy191iss00000000000cute"
n1es = N1ES(key)
flag = "N1CTF{*****************************************}"
cipher = n1es.encrypt(flag)
print base64.b64encode(cipher)  

base="HRlgC2ReHW1/WRk2DikfNBo1dl1XZBJrRR9qECMNOjNHDktBJSxcI1hZIz07YjVx".decode('base64')

chars=string.printable
te=[8,
 9,
 10,
 11,
 12,
 13,
 14,
 15,
 0,
 1,
 2,
 3,
 4,
 5,
 6,
 7,
 24,
 25,
 26,
 27,
 28,
 29,
 30,
 31,
 16,
 17,
 18,
 19,
 20,
 21,
 22,
 23,
 40,
 41,
 42,
 43,
 44,
 45,
 46,
 47,
 32,
 33,
 34,
 35,
 36,
 37,
 38,
 39]


message=""
pt=["*"] * 48
for i in range(48):
        for j in chars:
                pt[i]=j
                test=n1es.encrypt("".join(pt))
                if(test[i]==base[i]):
                        message+=j
                        break

for i in range(6,48):
        for j in chars:
                pt[i]=j
                test=n1es.encrypt("".join(pt))
                if(test[8:i+9] in base):
                        message+=j
                        print pt
                        break
#message=F3
for i in range(8,16):
        for j in chars:
                pt[i]=j
                test=n1es.encrypt("".join(pt))
                if(test[:9-i]== base[:9-i]):
                        message+=j
                        print pt
                        break
#message=F3i0

for i in range(len(tptenc)):
	tpt[i]="0"
    	ar=n1es.encrypt("".join(tpt))
	print ar
	print tptenc
	for j in range(len(ar)):
        	if(ar[j]!=tptenc[j]):
                	test+=[j]
			break


for i in range(len(tptenc)):
            tpt[i]="0"
            ar=n1es.encrypt("".join(tpt))
            print ar
            print prev  
            for j in range(len(ar)):
                        if(ar[j]!=prev[j]):
                        	test+=[j]
                                prev=ar
				break

-----------------------------------------



for i in range(8,15):
        for j in chars:
                pt[i]=j
                test=n1es.encrypt("".join(pt))
                if(test[i-8] == base[i-8]):
                        message+=j
                        print pt
                        break
for i in range(0,7):
        for j in chars:
                pt[i]=j
                test=n1es.encrypt("".join(pt))
                if(test[i+8] == base[i+8]):
                        message+=j
                        print pt
                        break
for i in range(24,31):
        for j in chars:
                pt[i]=j
                test=n1es.encrypt("".join(pt))
                if(test[i-8] == base[i-8]):
                        message+=j
                        print pt
                        break


for i in range(16,23):
        for j in chars:
                pt[i]=j
                test=n1es.encrypt("".join(pt))
                if(test[i+8] == base[i+8]):
                        message+=j
                        print pt
                        break

for i in range(40,47):
        for j in chars:
                pt[i]=j
                test=n1es.encrypt("".join(pt))
                if(test[i-8] == base[i-8]):
                        message+=j
                        print pt
                        break
for i in range(32,39):
        for j in chars:
                pt[i]=j
                test=n1es.encrypt("".join(pt))
                if(test[i+8] == base[i+8]):
                        message+=j
                        print pt
                        break
"".join(pt)
Out[196]: 'N1CTF{F*istel_n*tw0rk_c*n_b3_ea*i1y_s0l*3d_/s--/*'

