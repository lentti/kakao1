from __future__ import print_function

def main():
	n, arr1, arr2 = input()
	result = []
	for i in range(n):
		num = arr1[i] | arr2[i]
		binnum = bin(num)[2:]
		binstr = ''
		for j in range(len(binnum)):
			binstr += ('#' if binnum[j] == '1' else ' ')
		result.append(binstr)
	print('[',end ='')
	for i in range(len(result)):
		print('\"'+ result[i] + '\"',end ='')
		if i != len(result)-1:
			print(', ',end ='')
		else:
			print(']')

def input():
	n = int(raw_input())
	arr1 = input_arr()
	arr2 = input_arr()
	return (n,arr1,arr2)

def input_arr():
	a = raw_input()
	a = a[1:-1]
	b = a.split(',')
	c = [int(ele) for ele in b]
	return c

if __name__ == '__main__':
	main()