#!/usr/bin/env python3

import sys
import re
import copy
import itertools
import more_itertools

with open(sys.argv[1]) as f:
	for line in f:
		l = line.split('\t')
		#print(l[4:5], l[5:6], l[7:8], l[8:9])
		#print("\t".join(l[4:5]+l[5:6]+l[7:8]+l[8:9]).replace('@','\t').replace('\n',''))
		o = "\t".join(l[4:5]+l[5:6]+l[7:8]+l[8:9]).replace('@','\t').replace('\n','')
		print(re.sub(r'\.([A-Z][A-Z][A-Z])','\t\\1', o, flags=re.IGNORECASE))
		#print(l[4:5].replace('@','\t'))
