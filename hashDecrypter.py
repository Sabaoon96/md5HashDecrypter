# -*- coding: utf-8 -*-

import hashlib
def decrypt(string):
	return(hashlib.md5(string.encode('utf-8')).hexdigest())

# Reading file with common dictionary words	
with open("dictionary.txt") as f:
    content = f.readlines()

# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

# md5 Hash to decrypt
var1 = "085d10e29379c31adee4256137f0ebc2"

for x in content:
	# Following Digest Authentication format
	# username:realm:password 
	var2 = ("user222:Boutique Cassee:" + x)
	result = decrypt(var2)
	if var1 == result:
		print(x)





