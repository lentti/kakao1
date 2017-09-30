class T:
	def __init__(self,value):
		self.time = value

	def __add__(self,minuites):
		orig_min = int(self.time[3:])
		orig_min += minuites
		if orig_min >= 60:
			self.time = '%02d' % (int(self.time[:2])+1)+':'+'%02d' % (orig_min-60)
		else:
			self.time = '%02d' % (int(self.time[:2])) + ':'+'%02d' % (orig_min)

	def __str__(self):
		return self.time

cur_time = T('09:00')
bus_table = []
n=1
t=1
m=5
crew_table = '["00:01", "00:01", "00:01", "00:01", "00:01"]'
crew_table = eval(crew_table).sort()

for _ in range(n):
	for _ in range(m):
		bus_table.append(cur_time.time)
	cur_time+t

print 'bus_table'
print bus_table
print 'crew_table'
print crew_table