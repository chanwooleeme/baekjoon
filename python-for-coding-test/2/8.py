s = list(input())
num_list = list()
chr_list = list()
for item in s:
	if '0' <= item <= '9':
		num_list.append(int(item))
	else:
		chr_list.append(item)
result = ""
chr_list.sort()
for chr in chr_list:
	result += chr
print(result+str(sum(num_list)))