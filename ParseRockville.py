# Read RockvilleData and parse that jawn. :)


# ID            1-11   Character
# YEAR         12-15   Integer
# MONTH        16-17   Integer
# ELEMENT      18-21   Character
# VALUE1       22-26   Integer
# MFLAG1       27-27   Character
# QFLAG1       28-28   Character
# SFLAG1       29-29   Character

#line[21:26], line[26:27],line[27:28], line[28:29]



# a2 = a + 5
# b = a2
# b2 = b + 1
# c = b2
# c2 = c + 1
# d = c2
# d2 = d + 1

#annoying typing column names avoided

import pandas as pd 
def Rockville():

	f = open('RockvilleData.txt', 'r')

	# Hacer appends fuera de pandas y luego convertir con pandas.DataFrame
	#df = pd.DataFrame([])
	abunchoflines = []

	for line in f:

		# not necessary. Homero = Verga. line = f.readline()
		a = 21
		line_parsed = [line[:11],int(line[11:15]),int(line[15:17]),line[17:21]]

		while a < 262:
			a2 = a + 5
			b = a2
			b2 = b + 1
			c = b2
			c2 = c + 1
			d = c2
			d2 = d + 1
			line_parsed.extend([int(line[a:a2]),line[b:b2],line[c:c2],line[d:d2]])
			a += 8

		abunchoflines.append(line_parsed) 

	colnames = ["ID","Year",'Month','Data Type']

	for i in range(1,32):
		colnames.extend(('Value'+str(i),'Mflag'+str(i),'Qflag'+str(i),'Sflag'+str(i)))
	df = pd.DataFrame(abunchoflines,columns = colnames)
	# print(len(df), ' rows by ',len(df.columns),' columns ',type(df))
	# print(type(df['Value1'][0]))
	return df



# Homero == Verga
# TRUE

# use extend instead of various append
# line_parsed.append(line[a:a2])
# 	line_parsed.append(line[b:b2])
# 	line_parsed.append(line[c:c2])
# 	line_parsed.append(line[d:d2])

# # other parse idea to print string showing line[lim:lim]....
# print(('line[{}:{}]'.format(a,a2), 'line[{}:{}]','line[{}:{}]', 'line[{}:{}]'))

# line_parsed = [line[:11],line[11:15],line[15:17],line[17:21], line[21:26], line[26:27],line[27:28], line[28:29]]
# print(line_parsed)

# for line in f:
# 	to_parse = f.readline()

