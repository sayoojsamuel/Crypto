import string
def byte_xor(a):
	crypt=[]
	for i in range(0,len(a)):
		crypt.append(a[i])

	for i in range(255):
		plain = ""
		#key=hex(i)[2:].zfill(2)          <-- this is very important, especially zfill()
		#xor crypt to get plain
		for j in range(len(crypt)):
			plain += hex(ord(crypt[j]) ^ i)[2:].zfill(2)


		text=plain.decode("hex")
		space=" "
		text=text.rstrip('\n')
		if(all(c in string.printable for c in text)):
			print "--Key is %s--" %hex(i)			
			text=text.rstrip('@')
			print text
			m=len(text)%4
			if m!= 0:
				if m==1:
					text=text[:-1]
				
				else:
					text+="=" * (4-m)
			print text
			print m
			print len(text)%4
			
			try:
				text.decode('base64')	
				print text.decode('base64')
			except binascii.Error:
				print "Testing padding error"
				
	return
