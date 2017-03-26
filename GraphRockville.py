import numpy as np
import matplotlib.pyplot as plt
from RecordFinder import DailyRecords
[dailymin, dailymax, df] = DailyRecords()

# print(dailymax)
# print(dailymin)

startYear=df['Year'].min()
endYear=df['Year'].max()

x = np.arange(1, 366, 1)
y1 = dailymax
y2 = dailymin

plt.plot(x, y1, 'r-', label = 'Record High')
plt.plot(x, y2, 'b-', label = 'Record Low')
plt.legend()
plt.xlim(1,365)
plt.xlabel('Day of Year')
plt.ylabel('Temperature (Celsius)')
plt.title('Daily Record Temperatures in Rockville, MD\n (Data 1907-2007)')
plt.fill_between(x, y1, y2, facecolor = 'purple')
plt.savefig('RockvilleWeather.png')
 
# fig, ax1 = plt.subplots()
 
# ax2 = ax1.twinx()
# ax1.plot(x, y1, 'g-')
# ax2.plot(x, y2, 'b-')
# plt.axis(1,365,-50,50) 

