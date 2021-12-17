#!/usr/bin/python3
import mailbox
import sys

#for msg in mailbox.mbox('./mbox'):
#for msg in mailbox.mbox(sys.argv[1]):
#for f in sys.stdin:
#	for msg in mailbox.mbox(f):
#		print(msg['from'], msg['from'].replace('<','\t').replace('>','').replace('@', '\t'), '\t', msg['subject'], '\t', msg['date'], '\t', msg['Message-ID'], msg['Message-ID'].replace('<','\t').replace('>','').replace('@', '\t'))
for msg in mailbox.mbox(sys.argv[1]):
	frm = msg['from']
	frm = frm.replace('<', '\t')
	frm = frm.replace('>', '')
	frm = frm.replace('@', '\t')
	msgid = msg['Message-ID']
	msgid = msgid.replace('<', '\t')
	msgid = msgid.replace('>', '')
	msgid = msgid.replace('@', '\t')
	print(msg['from'], '\t', frm, '\t', msg['subject'], '\t', msg['date'], '\t', msg['Message-ID'], '\t', msgid)
