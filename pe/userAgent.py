import re
s = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2267.7 Safari/537.36    Chrome  40"
new = re.split(r'\t+', s.rstrip('\t'))
print new
