import re

def main():
	sdtdic={'S':1, 'D':2, 'T':3}
	result = 0
	inp = raw_input()
	exp = re.compile('\d+[SDT][*#]?')
	dart = exp.findall(inp)
	for i in range(len(dart)):
		sdtidx = (0 if dart[i].find('S') == -1 else dart[i].find('S')) | (0 if dart[i].find('D') == -1 else dart[i].find('D')) | (0 if dart[i].find('T') == -1 else dart[i].find('T'))
		number = int(dart[i][:sdtidx])
		score = number ** sdtdic[dart[i][sdtidx]]
		if i != len(dart)-1:
			if dart[i+1][-1] == '*':
				score *=2
		if dart[i][-1] == '*':
			score *=2
		if dart[i][-1] == '#':
			score*=-1
		result += score
	print result

if __name__ == '__main__':
	main()