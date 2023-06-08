"""
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""
import math







f = open('task02a.txt','r')
data = f.read()


lineData = data.split("\n")
#print(lineData)
newList = [int(i) for i in lineData if len(i) > 0]


#print(newList)


split_points = [i for i in range(0, len(newList), 3)]

parts = [newList[ind:ind + 3] for ind in split_points]

def triples(n):
    data = []
    for a in range (1, n):
        for b in range (a,n):
            c = math.sqrt(a*a+b*b)
            if c. is_integer()and c <= n:
                x = [a,b,int(c)]
                #print(x)
                data.append(x)
    return data

x = triples(65)

#print(x)
counter = 0
list1 = []
for i in parts:
    i = sorted(i)
    list1.append(i)

#print(list1)
for i in x:
   for j in list1:
        #print(i, j , i == j)
        a = (i == j)
        if a == True:
            counter += 1
print(f"the set of number which are Pythagorean triples is {counter}")
