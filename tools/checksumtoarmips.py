import sys
import binascii

print(".orga 0x1000")
print(".headersize 0x80245000")

LabelStack = ['']

# RegisterMap = 

ROMFile = open(sys.argv[2],'rb')
ROM = ROMFile.read()

# addrFile = open("ROM Adresses.txt","w")

address = 0x1000
compAddr = 0x0
succWriteCount=0

funcBuffer=address
with open(sys.argv[1],'r') as checkSumFile:
	for line in checkSumFile.readlines():
		if len(line.split(":"))>=2:
			addr,instruction = line.split(':')[0:2]
			tokens = instruction.split(' ')[1:]
			tokenCount=len(tokens)
			# if(tokenCount>4):
				# tokens = tokens[:4]
			opcode,p1,p2,im=['']*4
			opcode = tokens[0].strip()
			if opcode=='CACHE' or opcode=='BREAK':
				print('.word 0x'+str(binascii.hexlify(ROM[address:address+0x4]))[2:-1]+" ;",opcode)
			else:
				if len(tokens)>1:
					p1 = tokens[1].strip()
				if len(tokens)>2:
					p2 = tokens[2].strip()
				if len(tokens)>3:
					im = tokens[3].strip()
					# im = im[]
				if opcode=='CFC1' or opcode== 'CTC1':
					p2='fcr31'
				if p2=='ExceptPC':
					p2='EPC'
				if opcode=='JALR':
					temp = p1
					p1=p2
					p2 = temp
					p2=p2[:-1]
					p1+=','
				print(opcode.lower(),p1,p2,im)#,"\t\t; ",hex(address),hex(address+0x80245000),hex(compAddr))
				# if opcode=='JR' and p1 == 'RA':
				# 	funcBuffer=1
				# if funcBuffer==0:
				# 	print('')
			# addrFile.write(str(hex(address))[-1:]+" ")
			# if str(hex(address))=='c':
			# 	addrFile.write("\n")
			address+=0x0004
			compAddr+=0x0004
			funcBuffer-=1