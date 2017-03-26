def DailyRecords():
	from ParseRockville import Rockville 

	df = Rockville()
	# print(df)

	# Mask 
	# df[(df['colname'] == value)]

	#Create a dictionary with twelve keys- the months- and each month with its data.
	month_dbs = []

	for m in range (0,12):
		month_dbs.append(df[df['Month'] == m+1])
	# 	print(len(month_dbs[m]))
	# print(type(month_dbs))

	calendar = {}
	month_names = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
	for m in range(0,12):
		calendar[month_names[m]] = month_dbs[m]

	monthmax = []
	for m in range (0,12):
		monthmax.append(month_dbs[m][month_dbs[m]['Data Type'] == 'TMAX'])
		# print(len(monthmax[m]))

	monthmin = []
	for m in range (0,12):
		monthmin.append(month_dbs[m][month_dbs[m]['Data Type'] == 'TMIN'])

	dailymax = []
	dailymin = []
	# attempt at all months
	for m in range (0,12):
		last_day = [32,29,32,31,32,31,32,32,31,32,31,32]
		for i in range (1,last_day[m]):
			dailymax.append(monthmax[m]['Value'+str(i)][monthmax[m]['Value'+str(i)] != -9999].max()/10)
			dailymin.append(monthmin[m]['Value'+str(i)][monthmin[m]['Value'+str(i)] != -9999].min()/10)
	# print(len(dailymax))
	# print(len(dailymin))

	# print(dailymax)
	# print(dailymin)
	return dailymin, dailymax, df 


# Homero graph
# startYear=df['Year'].min()
# endYear=df['Year'].max()

# x = np.arange(0, 372, 1)
# y1 = maxvalues;
# y2 = minvalues;

# fig, ax1 = plt.subplots()

# ax2 = ax1.twinx()
# ax1.plot(x, y1, 'g-')
# ax2.plot(x, y2, 'b-')

# ax1.set_xlabel('Days during year')
# ax1.set_ylabel('Max Temperature in Degrees Celsius Per Day Summary between '+str(startYear)+' and '+str(endYear)+' years', color='g')
# ax2.set_ylabel('Min Temperature in Degrees Celsius Per Day Summary between '+str(startYear)+' and '+str(endYear)+' years', color='b')

# plt.show()

