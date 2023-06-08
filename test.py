listVaue = ['Server1,Command1,9182,Running,START,Server2,Command2,8888,Running,RESTART,ServerN,CommandN,N,Running,restart']
listVaue = listVaue[0].split(',')
a = ['START', 'RESTART', 'STOP', 'BOUNCE']
s = []
l2 = []
for i in listVaue:
    s.append(i)
    if i.upper() in a:
        l2.append(s)
        s = []
print (l2)