#!/usr/bin/python
#-*-coding:utf-8-*-
"""
Generate a triangle with N lines of random numbers between 0 and m and find the path with maximum total from top to bottom 
Usage: python path.py N[ m = 99]
Examples:
	$ python path.py 15
	$ python path.py 20 999

See https://projecteuler.net/problem=18 for more details
"""
import sys
from random import randint

def main(N, m):
	# Generate the triangle
	T = []
	for i in xrange(N):
		T.append([randint(0, m) for x in xrange(i + 1)])

	# Find best score
	S = [list(T[i]) for i in xrange(N - 1, -1, -1)]
	for i in xrange(1, N):
		S[i] = [S[i][x] + max(S[i - 1][x], S[i - 1][x + 1]) for x in xrange(0, len(S[i]))]
	score = s = S[-1][0]

	# Find the best path
	path = [T[0][0]]
	S.reverse()
	for i in xrange(1, N):
		s -= path[-1]
		for j, x in enumerate(S[i]):
			if s == x:
				path.append(T[i][j])
				break

	# Display the triangle
	padding = len(str(m))
	for i in xrange(N):
		print " %s%s " % (" " * padding * (N - 1 - i),(" " * padding).join([str(x).zfill(padding) for x in T[i]]))
	print "\nTriangle: %d lines, %d points, %d paths" % (N, N * (N + 1) / 2, 2 ** (N - 1))
	print "Solution: %s = %d" % ("+".join(map(str, path)), score)

if __name__ == '__main__':
	if len(sys.argv) >= 2:
		try:
			N = int(sys.argv[1])
		except:
			N = 0
		if N >= 1:
			try:
				m = int(sys.argv[2])
			except:
				m = 99
			else:
				m = max(0, m)

			main(N, m)
