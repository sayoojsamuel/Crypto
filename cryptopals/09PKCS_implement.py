#to implement the PKCS#7 padding
#All the strings padded to block size of 16
block_size=16

def pad(string,block=16):
	string+= (block-len(string)%block) * chr(block-len(string)%block)
	return string

if __name__=="__main__":
	#print "Enter the input"
	n=raw_input()
	print pad(n)

	
