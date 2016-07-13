import sys
from itertools import product

def computesize(reference, qgrams, d):
	
	for i in range(len(reference)-len(qgrams.keys()[0])):		
		for key in qgrams:
			distance = computehamming(key, reference[i:i+len(key)], d)
			
			if distance <= d:
				qgrams[key] += 1
	
				
	
def computeqgrams(q):
	
	bases = ["A", "C", "G", "T"]
	
	qgrams = dict()
	
	for gram in product(bases, repeat = q):
		qgrams["".join(gram)] = 0
			
	return qgrams
					
		
def computehamming(qgram1, qgram2, d):
	
	distance = 0
	
	for i in range(len(qgram1)):
		if distance > d:
			break
		if qgram1[i] != qgram2[i]:
			distance += 1
		
	return distance
	

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
	

def main():
	
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
	print len(qgrams)
	print qgrams
	
	computesize(reference, qgrams, d)
	print qgrams

	maxi = computemax(qgrams)
	
	for m in maxi:
		print m[0], m[1]
	
main()
