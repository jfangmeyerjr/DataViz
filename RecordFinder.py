from ParseRockville import Rockville 

df = Rockville()
print(df)

# Mask for January only
# df[(df['colname'] == value)]

#calendar = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
calendar = {}

for m in range (0,12):
	#print(calendar[m])
	calendar[m] = df[df['Month'] == m+1]
	print(len(calendar[m]))
print(type(calendar))

#enero = df[df['Month']==1]
#enero01 = df[df['Month'] == 01]
# Visual check. Checks out. Somos vvvvergas.
#enero.to_csv('January_Rockville_Weather.csv')

# months = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']

# for m in range (0,12):
# 	months = calendar[m]['Data Type'] == 'TMAX'
# 	print(len('{}'.format(months[m])+'max'))

# eneromax = enero[enero['Data Type'] == 'TMAX']
# # #print(len(eneromax), len(eneromax.columns))

# eneromin = enero[enero['Data Type'] == 'TMIN']
# # #print(len(eneromin), len(eneromin.columns))

# print(eneromax['Value1'].max())
for month 
	for day
		monthmin[monthmin['Valueday'] != -9999]['Valueday'].min()


		
print(eneromin[eneromin['Value1'] != -9999]['Value1'].min())
