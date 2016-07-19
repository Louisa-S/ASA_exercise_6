import sys
from itertools import product


#for each qgram in the dictionary compute how many neigbors exist with distance d
def computesize(reference, qgrams, d):
	
	for i in range(len(reference)-len(qgrams.keys()[0])):		
		for key in qgrams:
			distance = computehamming(key, reference[i:i+len(key)], d)
			
			if distance <= d:
				qgrams[key] += 1
	
				

#precomputation of all possible kmers of size q
def computeqgrams(q):
	
	bases = ["A", "C", "G", "T"]
	
	qgrams = dict()
	
	for gram in product(bases, repeat = q):
		qgrams["".join(gram)] = 0
			
	return qgrams
			
					
#computation of hamming distance between two qgrams
#if distance is above the maximal d the computations stops		
def computehamming(qgram1, qgram2, d):
	
	distance = 0
	
	for i in range(len(qgram1)):
		if distance > d:
			break
		if qgram1[i] != qgram2[i]:
			distance += 1
		
	return distance
	

#computation of the maximum number of neigbors, if two have the same, both are returned
def computemax(qgrams):
	
	temp = 0
	maxi = [("", 0)]
	
	for key in qgrams:
		if qgrams[key] > temp:
			maxi = [(key, qgrams[key])]
			temp = qgrams[key]
		elif qgrams[key] == temp:
			maxi.append((key, qgrams[key]))
			
	return maxi
	
	
## MAIN
def main():
	
	#reading of the input reference file
	reference = ""
	with open(str(sys.argv[1])) as f:
		for line in f:
			if line == "\n":
				break				
			if line[0] == ">":
				continue
			else:
				reference += line[:-1]
	
	q = int(sys.argv[2])
	
	d = int(sys.argv[3])
	
	qgrams = computeqgrams(q)

	computesize(reference, qgrams, d)
	
	maxi = computemax(qgrams)
	
	for m in maxi:
		print m[0], m[1]
	
main()
