#!/usr/bin/env python3
###
##!/usr/bin/python3
###
import sys
import email
from email.policy import default
import mailbox

#for msg in mailbox.mbox('./mbox'):
#for msg in mailbox.mbox(sys.argv[1]):
#for f in sys.stdin:
#	for msg in mailbox.mbox(f):
#		print(msg['from'], msg['from'].replace('<','\t').replace('>','').replace('@', '\t'), '\t', msg['subject'], '\t', msg['date'], '\t', msg['Message-ID'], msg['Message-ID'].replace('<','\t').replace('>','').replace('@', '\t'))
#for msg in mailbox.mbox(sys.argv[1]):
#	frm = msg['from']
#	frm = frm.replace('<', '\t')
#	frm = frm.replace('>', '')
#	frm = frm.replace('@', '\t')
#	msgid = msg['Message-ID']
#	msgid = msgid.replace('<', '\t')
#	msgid = msgid.replace('>', '')
#	msgid = msgid.replace('@', '\t')
#	print(msg['from'], '\t', frm, '\t', msg['subject'], '\t', msg['date'], '\t', msg['Message-ID'], '\t', msgid)
i=0
for msg in mailbox.mbox(sys.argv[1]):
	print(sys.argv[1], '-', i, ":\t", msg['from'], '\t', msg['Message-ID'])
	i=i+1
