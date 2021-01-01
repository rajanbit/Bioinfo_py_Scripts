class text():
	red = '\033[31m'
	green = '\033[32m'
	yellow = '\033[33m'
	blue = '\033[34m'
	default = '\033[0m'

t_seq = input("Enter the Sequence: ")
c_seq = ""
for i in range(0, len(t_seq)):
	if t_seq[i] == "A":
		c_seq = c_seq + "T"
	elif t_seq[i] == "T":
		c_seq = c_seq + "A"
	elif t_seq[i] == "G":
		c_seq = c_seq + "C"
	elif t_seq[i] == "C":
		c_seq = c_seq + "G"


spacer_list = [3,2,1,0,0,1,2,3]
bp_list = [0,2,4,6,6,4,2,0]
data = "\n"
x = 0
l = len(t_seq)
while x != l:

	for y in range(0,len(spacer_list)):
		try:
			data += "\t"+" "*spacer_list[y] + t_seq[x] + "-"*bp_list[y] + c_seq[x] + "\n"
			x+=1
		except:
			break
	
data = data.replace("A",(text.red+"A"+text.default))
data = data.replace("T",(text.blue+"T"+text.default))
data = data.replace("G",(text.green+"G"+text.default))
data = data.replace("C",(text.yellow+"C"+text.default))
print("\n\tDNA Helix\n"+data)

# python dna_helix_visualizer.py
