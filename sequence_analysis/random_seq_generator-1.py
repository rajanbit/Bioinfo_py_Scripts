# Importing modules
import numpy as np
import pandas as pd
from random import uniform, randint, sample

# Functions to generate random sequence of length -> l and gc_content -> gc

# Approach 1 | Using Probabilistic Model 
# Iterate through all the positions in increasing order
# and for each position generate random probablity between
# 1% and 100%. If the probablity is < given GC percent
# then randomly assigning G/C to that positions and 
# else randomly assigning A/T to that position
def generate_seq_1(l:int, gc:float):
	seq = ""
	nt = ["A", "T", "G", "C"]
	for i in range(l):
		if uniform(0.01, 1.0) < gc:
			seq += nt[randint(2, 3)]
		else:
			seq += nt[randint(0, 1)]
	return seq

# Approach 2 | Using Random Sampling
# Sample random positions where nt should be G/C
# and then randomly assigning G/C to that positions and 
# for rest of the positions randomly assigning A/T
def generate_seq_2(l:int, gc:float):
	seq = ""
	nt = ["A", "T", "G", "C"]
	gc_pos = sample(range(l), int(gc*l))
	for i in range(l):
		if i in gc_pos:
			seq += nt[randint(2, 3)]
		else:
			seq += nt[randint(0, 1)]
	return seq
