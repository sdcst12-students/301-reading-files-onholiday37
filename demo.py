"""
x = [[1,2,3],[3,4,5],[4,5,6]]
y = [[4,5,6],[1,1,1]]
x =str(x)
y = str(y)
for i in x:
    for j in y:
        print(i , j , i==j)
"""

f = open('task02a.txt','r')
data = f.read()


lineData = data.split("\n")
print(lineData)
newList = [i for i in lineData if len(i) > 0]


print(newList)


split_points = [i for i in range(0, len(newList), 3)]

parts = [newList[ind:ind + 3] for ind in split_points]

list1 = []
for i in parts:
    for i in i:
        i.split()
        list1.append(i)


print(list1)