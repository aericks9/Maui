import us

READ = 'rb'
WRITE = 'wb'
data = {}
with open('prevalence.csv',READ) as f:
	for line in f.read().splitlines():
		state,prevalence = tuple(line.split(','))
		data[us.states.lookup(state).name] = int(prevalence)

with open('prevalence-d3.csv',WRITE) as f:
	print>>f,'state,value'
	for state,prevalence in data.iteritems():
		print>>f,'%s,%d'%(state,prevalence)