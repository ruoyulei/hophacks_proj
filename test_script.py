
temp_str = ""
for character in "adsaf (*12 ) ^LLL":
	if ord(character) not in range(48,57) and ord(character) not in range(65,90) and ord(character) not in range(97,122):
		temp_str+=" "
	else:
		temp_str+=character
print temp_str