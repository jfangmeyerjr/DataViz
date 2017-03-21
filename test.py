from ParseRockville import Rockville 

df = Rockville()
#calendar = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
month_dbs = []

for m in range (0,12):
	month_dbs.append(df[df['Month'] == m+1])
	print(len(month_dbs[m]))
print(type(month_dbs))

calendar = {}
month_names = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
for m in range(0,12):
	calendar[month_names[m]] = month_dbs[m]
print(type(calendar))
print(type(calendar['enero']))
print(month_dbs[0] == calendar['enero'])
	