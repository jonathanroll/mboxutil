#!/usr/bin/env python3

import sys
import email
import mailbox
import email.parser
import email.policy

mbox = mailbox.mbox(sys.argv[1], factory=email.parser.BytesParser(policy=email.policy.default).parse)

i=0
for _, message in enumerate(mbox):
	try:
		print(sys.argv[1], '-', i, ':', message['from'],message['date'],message['to'],message['subject'],message['message-id'],sep='\t')
	except:
		continue
	finally:
		i=i+1
		continue
