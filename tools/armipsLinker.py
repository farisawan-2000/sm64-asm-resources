import sys
funcList={}
with open(sys.argv[1],'r') as inFile:
	for line in inFile:
		addr,name=line.split()
		funcList[addr]=name
for key in list(funcList):
	if funcList[key][:2]=='0x':
		del funcList[key]
for key in funcList:
	if 'build/' not in funcList[key]:
		print(""+funcList[key]+" equ "+key)