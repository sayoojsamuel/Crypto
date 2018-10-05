string="Hello my name is Sayooj Samuel. I study in Amrita College at Amritapuri. I am currently in semester 2 under CSE Branch. I am named Sayooj Samuel"

list=string.split()
freq=[]
for w in list:
	freq.append(list.count(w))

print "String\n"+string+"\n"
print "List\n"+str(list)+"\n"
print "Frequency\n"+str(freq)+"\n"
print "Pairs\n"+str(dict(zip(list,freq)))

freqdict=dict(zip(list,freq))
aux=[(freqdict[key], key) for key in freqdict]
aux.sort()
aux.reverse()
print aux
