# Read RockvilleData and parse that jawn. :)

f = open('RockvilleData.txt', 'r')

# ID            1-11   Character
# YEAR         12-15   Integer
# MONTH        16-17   Integer
# ELEMENT      18-21   Character
# VALUE1       22-26   Integer
# MFLAG1       27-27   Character
# QFLAG1       28-28   Character
# SFLAG1       29-29   Character

#line[21:26], line[26:27],line[27:28], line[28:29]

line = f.readline()

a = 21
# a2 = a + 5
# b = a2
# b2 = b + 1
# c = b2
# c2 = c + 1
# d = c2
# d2 = d + 1
while a < 262:
	a2 = a + 5
	b = a2
	b2 = b + 1
	c = b2
	c2 = c + 1
	d = c2
	d2 = d + 1
	print(('line[{}:{}]'.format(a,a2), 'line[{}:{}]','line[{}:{}]', 'line[{}:{}]'))
	a += 8



# line_parsed = [line[:11],line[11:15],line[15:17],line[17:21], line[21:26], line[26:27],line[27:28], line[28:29]]
# print(line_parsed)

# for line in f:
# 	to_parse = f.readline()

