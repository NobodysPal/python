#!/usr/bin/env python

import re, base64, binascii, datetime

s = "SGFwcHkgQmlydGhkYXk=:" \
    "aHR0cHM6Ly95b3V0dS5iZS9yM2d4YUtKTmpjQQ==:" \
    "2042656c6174656420"
n = 1, 24, 53, 63, 20
bday = datetime.datetime(2016, 9, 4)
now = datetime.datetime.now()
if bday < now:
    print re.sub('\s+',
                 binascii.unhexlify(s.split(base64.b64decode("Og=="))[2]),
                 base64.b64decode(s.split(binascii.unhexlify("3a"))[0]), 1)
    for x in n:
        print [s[i:i + 1] for i in range(0, len(s), 1)][x],
    print "%s" % (""),
    print base64.b64decode(s.split(s[20])[1][0:])
else:
    print base64.b64decode(s.split(binascii.unhexlify("3a"))[0])

