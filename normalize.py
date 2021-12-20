#!/usr/bin/env python3

import sys
import copy
import itertools
import more_itertools

with open(sys.argv[1]) as f:
	for (i,j) in more_itertools.pairwise(f):
		if j.startswith('\t'):
			i = i[:-1]+j[:-1]

		print(i.replace('\n',''))
