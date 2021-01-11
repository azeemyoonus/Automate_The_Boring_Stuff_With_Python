tableData = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]


def printTable(table):
	len_max=[]
	for i in range(len(table[0])):
		size=len(table[0][i])
		len_max.append(size)
	for i in range(len(table)):
		for j in range(len(table[i])):
			print(table[i][j].rjust(len_max[j]),end=' ')
		print()

printTable(tableData)

