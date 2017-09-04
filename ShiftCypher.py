def frequency(Enc):
	result = 0
	total = 0
	alphabet = [0] * 26
	percentages = [0.00] * 26
	totalpercent = 0

	#check to see if this works, keeping for chr command
	#for i in range(0,26):
		#print chr(alphabet[i] + 97 + i), ": ", alphabet[i]
		
	#now we need to find the frequency
	for i in xrange(0,len(Enc)):
		alphabet[ord(Enc[i]) - 97] += 1
		total += 1
	
	#this prints the numbers for the alphabet	
	#for i in range(0,26):
		#print alphabet[i]
		
	#calculates percentages to see if shift is correct
	for i in range(0,26):
		percentages[i] = alphabet[i] / float(total)
		totalpercent += (float(correctFreq[i]) * percentages[i])
		#print percentages[i]
	print "\n", "Total: ", totalpercent

	return totalpercent



i = 0
x = 0
index = 0
correctFreq = []


file = open("Shift_Enc.txt", "r")
Enc = file.read()
listEnc = list(Enc)


file2 = open("Shift_Freq.txt", "r")
for line in file2:
	correctFreq.append(line)
	
for i in range(0, 26):
	for j in xrange(0,len(listEnc)):
		listEnc[j] = chr(((ord(listEnc[j]) + i) % 97) + 97)
		#print Enc[i]
	print ''.join(listEnc)
	print "\n"
	frequency(listEnc)