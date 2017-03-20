from ParseRockville import Rockville 
import math

import numpy as np
import matplotlib.pyplot as plt

df = Rockville()

# Mask for January only
# df[(df['colname'] == value)]

months = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
calendar = []
maxvalues = []
minvalues = []

for m in range (0,12):
	calendar.append(df[df['Month'] == m+1])

# Visual check. Checks out. Somos vvvvergas.
#enero.to_csv('January_Rockville_Weather.csv')

for m in range (0,12):
	month=calendar[m];
	monthTMAX=month[month['Data Type']=='TMAX']
	monthTMIN=month[month['Data Type']=='TMIN']

	for d in range(1,32):
		validatedTMIN=monthTMIN[monthTMIN["Value"+str(d)] != -9999]
		validatedTMAX=monthTMAX[monthTMAX["Value"+str(d)] != -9999]
		minvalues.append(validatedTMIN['Value'+str(d)].min()/10.0)
		maxvalues.append(validatedTMAX['Value'+str(d)].max()/10.0)

# print(maxvalues, len(maxvalues))
# print(minvalues, len(minvalues))

startYear=df['Year'].min()
endYear=df['Year'].max()

x = np.arange(0, 372, 1)
y1 = maxvalues;
y2 = minvalues;

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(x, y1, 'g-')
ax2.plot(x, y2, 'b-')

ax1.set_xlabel('Days during year')
ax1.set_ylabel('Max Temperature in Degrees Celsius Per Day Summary between '+str(startYear)+' and '+str(endYear)+' years', color='g')
ax2.set_ylabel('Min Temperature in Degrees Celsius Per Day Summary between '+str(startYear)+' and '+str(endYear)+' years', color='b')

plt.show()
