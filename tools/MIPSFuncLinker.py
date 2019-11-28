# Takes a simplified Checksum disassembly file and a simplified sm64.us.map
# with caret output to a file
# and outputs a complete labeled disassembly that one can assemble
# to a US Super Mario 64 image with armips
import sys
import binascii
regList = ['r0','at','v0','v1','a0','a1','a2','a3','t0','t1','t2','t3','t4','t5','t6','t7','s0','s1','s2','s3','s4','s5','s6','s7','t8','t9','k0','k1','gp','sp','s8','ra']
r0=0
at=1
v0,v1=2,3
a0,a1,a2,a3=4,5,6,7
t0,t1,t2,t3,t4,t5,t6,t7=8,9,10,11,12,13,14,15
s0,s1,s2,s3,s4,s5,s6,s7=16,17,18,19,20,21,22,23
t8,t9=24,25
k0,k1=26,27
gp=28
sp=29
s8=30
ra=31
GPRs = {}
for i in range(0,32):
	GPRs[i]=0x00000000

# Gets function list
funcList={}
with open(sys.argv[1],'r') as funcFile:
	for line in funcFile:
		addr,name=line.split()
		if name[:2] != '0x':
			funcList[addr]=name

def addressFromLW(imm,reg):
	if GPRs[reg]==0:
		hi=0
	else:
		hi = int(GPRs[reg],16)
	if imm>0x7fff: # Epic MIPS quirky thing
		hi-=1
	hi *= 0x10000
	return hex(hi+imm)

addr = 0x80245ff8
jrTimer=-1
funcName=''
optionalComment=''
with open(sys.argv[2]) as asmFile:
	for line in asmFile:
		tokens = line.split()
		if tokens[0] == 'jal':
			if str(hex(int(tokens[1],16))) in funcList:
				tokens[1] = funcList[str(hex(int(tokens[1],16)))]
		if tokens[0] == 'lui':
			reg = tokens[1][:-1].lower()
			GPRs[regList.index(reg)]=hex(int(tokens[2],16))
		if tokens[0] != 'lui' and tokens[0][0]=='l':
			reg = tokens[3]
			reg = reg[1:3].lower()
			imm = int(tokens[2],16)
			getAddr = str(addressFromLW(imm,regList.index(reg)))
			if getAddr in funcList:
				tokens[2] = "lo("+funcList[getAddr]+")"
		if (str(hex(addr))) in funcList:
			funcName=funcList[str(hex(addr))]
			optionalComment='\t; '+funcName
			funcName=''
		if tokens[0] == 'jr' and tokens[1] == 'RA':
			jrTimer=1
		print("/*"+str(hex((addr-0x80245000))),str(hex(addr))+"*/",' '.join(tokens)+optionalComment)
		if jrTimer==0:
			print() # Split functions by newline
		addr+=0x0004
		jrTimer-=1
		optionalComment=''