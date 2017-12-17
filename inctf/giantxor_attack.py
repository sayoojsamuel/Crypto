from singcharxor import byte_xor

#to calculate the hamming dist
def hamdist(a,b):
	x=bin(int(a.encode("hex"),16))[2:]
	y=bin(int(b.encode("hex"),16))[2:]
	count=0
	for i,j in zip(x,y):
		if i!=j:
			count+=1
	return count

#to block the string and do the transpose
def block(string, keysize):
	blocks=[]
	transpose=[]

	for i in range(0, len(string), keysize):
		blocks+=[string[i:i+keysize]]
	for i in range(keysize):
		temp=""
		for j in range(len(blocks)):
			temp+=blocks[j][i]
		transpose+=[temp]
	return transpose



#to read from txt and b64 decode
b64=""
with open("ciphertext.txt") as f:
	for lines in f:
		b64+=lines.rstrip('\n')
string = b64


#KEYZIE finder
keyarr=[]
for i in range(2,40):

	key=hamdist(string[0:i],string[i:2*i])/i
	keyarr.append(key)


#keysize=int(min(keyarr))
keysize=int(min(keyarr))
pad=len(string) % keysize
string+= "\x00" * (keysize-pad)
transpose= block(string, keysize)
[byte_xor(transpose[i]) for i in 0,1]
print "check!!"
