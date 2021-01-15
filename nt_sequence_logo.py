### importing modules
####################################################################################

import sys
import math
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.text import TextPath
from matplotlib.patches import PathPatch
from matplotlib.font_manager import FontProperties

### Functions used
####################################################################################

def base_info(base, x, y, yscale=1, ax=None):
    text = nts[base]

    t = mpl.transforms.Affine2D().scale(1*globalscale, yscale*globalscale) + \
        mpl.transforms.Affine2D().translate(x,y) + ax.transData
    p = PathPatch(text, lw=0, fc=nt_clr[base],  transform=t)
    if ax != None:
        ax.add_artist(p)
    return p

def log2(p):
	if p == 0:
		log_nt = 0
	else:
		log_nt = math.log2(p)
	return(log_nt)

file_f = sys.argv[1]
file_r = open(file_f, "r")
fast_f = file_r.readlines()
seq_list = []
for line in fast_f:
	if line[0] != ">":
		seq_list.append(line.strip())
def score_order(score):  
	lst = len(score)  
	for i in range(0, lst):  
		for j in range(0, lst-i-1):  
			if (score[j][1] > score[j + 1][1]):  
				temp = score[j]  
				score[j]= score[j + 1]  
				score[j + 1]= temp  
	return score
### Fasta file handling and bit_score calculation
####################################################################################

nt_scores = []
for i in range(0,len(seq_list[0])):
	A = T = G = C = 0
	for data in seq_list:
		if data[i] == "A":
			A += 1
		elif data[i] == "G":
			G += 1
		elif data[i] == "T":
			T += 1
		elif data[i] == "C":
			C += 1
	tot = A+G+C+T

	pA = A/tot
	pG = G/tot
	pC = C/tot
	pT = T/tot

	I = (math.log2(4.0)) + (pA*log2(pA)) + (pG*log2(pG)) +(pT*log2(pT)) + (pC*log2(pC))

	score = [("A", pA*I), ("G", pG*I), ("T", pT*I), ("C", pC*I)]
	nt_scores.append(score_order(score))
	A = G = C = T = 0

### plotting the bit_score for bases
####################################################################################

font_p = FontProperties(weight="bold")

globalscale = 1.35

nts = { "T" : TextPath((-0.305, 0), "T", size=1, prop=font_p),
            "G" : TextPath((-0.384, 0), "G", size=1, prop=font_p),
            "A" : TextPath((-0.35, 0), "A", size=1, prop=font_p),
            "C" : TextPath((-0.366, 0), "C", size=1, prop=font_p) }
nt_clr = {'G': 'orange', 
          'A': 'limegreen', 
          'C': 'blue', 
          'T': 'red'}


fig, ax = plt.subplots(figsize=(10,3))

x = 1
maxi = 0

for scores in nt_scores:
    y = 0
    for base, score in scores:
        base_info(base, x,y, score, ax)
        y += score
    x += 1
    maxi = max(maxi, y)

plt.xticks(range(1,x))
plt.xlim((0, x)) 
plt.ylim((0, maxi)) 
plt.tight_layout()      
plt.show()
