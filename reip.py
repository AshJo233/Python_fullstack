#!/usr/bin/python
import re

test_str = '<address>1.2.3.4 aghjsdfdf <address>5.6.7.8 hlkjhklj1<address>103.543.54.55h'
#result = re.findall(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", test_str)


result = re.findall('(?:\d{1,3}\.){3}\d{1,3}', test_str)
print(result)
