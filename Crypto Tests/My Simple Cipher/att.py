a=open("encrypted.txt").read().rstrip("\n").decode("hex")
def change(j):
	global message
	for i in range(j, 36, 13):
		message[i]=chr((ord(a[i])-(ord(key[(i-1)%13])+ord(a[i-1]))) % 128 )
	
message=36 * "0"
message=list(message)
key=13 * "0"
key=list(key)

key[8]=chr((ord(a[22])-(ord("|")+ord(a[21])))% 128)
change(9)
x=12
for i in range(13):
	key[x]=message[23+x]
	change(x+1)
	x= (x+4)%13
		
print "".join(key)
print "".join(message)
