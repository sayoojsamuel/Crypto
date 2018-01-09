#Cryptopals task to validate PKCS#7 padding and to throw errors
#the program is set for default of blocksize=16 (default AES size)
blocksize=16

def pad_check(string, block=16):
	pad=string[len(string)-1]
	intpad=ord(pad)
	try:
		for i in range(intpad):
			if(string[::-1][i]!=pad):
				raise
		string=string.rstrip(pad)
		print "The string after padding removal is :\n" + string
		
	except:
		print "Padding is wrong"

if __name__=="__main__":
	print "Enter the padded string: "
	string=raw_input()
	pad_check(string)


