# ; Mario 64 Main Code Segment Disassembly 2.0
# ; New Features:
# ; 	-Function Names now represent Decompilation Project documented names
# ;		-Beginnnings of functions now labeled
# ;		-Labeled ALL symbol addresses
# ; Future features:
# ; -Labeled struct offsets
# ;	-Labeled Branch targets
# ;	-Realign Behavior Script function calls
import sys

def isAddress(testCase):
	if len(testCase)==18 and testCase[:2]=='0x':
		return True
	return False

startedFuncMapping=False
foundAddr=False
outFile=open("sm64.simple.map","w")
with open(sys.argv[1]) as mapFile:
	for line in mapFile.readlines():
		for word in line.split():
			if word=="EntryPoint":
				startedFuncMapping=True
			if startedFuncMapping:
				if foundAddr:
					outFile.write(word+"\n")
					foundAddr=False
				if isAddress(word):
					outFile.write('0x'+word[10:]+" ")
					foundAddr=True
			if word=="gFrameBuffer2":
				startedFuncMapping=False