maxvalues = []
minvalues = []

monthNames = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'november', 'december']
calendar={}
for m in range(0, 12):
	# Assign a data value to a key in a dictionary, reference value by name instead of a number
	calendar[monthNames[index]]=pandasDataFrame; # change pandasDataFrame for code that actually gets the dataframe for the selected month

	month=calendar['January']
	month=calendar[monthNames[index]]

	monthmax=month[month['Data Type']=='TMAX']
	monthmin=month[month['Data Type']=='TMIN']

	for d in range(1,32):
		minvalues.append(monthmin[monthmin["Value"+str(d)] != -9999]['Value'+str(d)].min())
		maxvalues.append(monthmax['Value'+str(d)].max())



# maxvalues.append(monthmax.max())
# minvalues.append(monthmin[monthmin["Value"+???] != -9999].min())
