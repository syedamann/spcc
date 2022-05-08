f = open("code.py", "r")
line = f.readlines()

for i in range(len(line)):
    line[i] = line[i][:-1]

print("Code Before Optimization:")
for element in line: 
    print(element)

for element in list(line):
    newEq = ""
    Eq=list(element.split("=")[1])
    rhs=element.split('=')[0]+'='
    if '*' in Eq:
        mulIndex = Eq.index('*')
        ind = int(Eq[mulIndex-1])
        for i in range(ind):
            newEq += Eq[int(mulIndex)+1] + "+"
        newEq = newEq[:-1]
        pos = line.index(element)
        line.remove(element)
        element = rhs + ''.join(newEq)
        line.insert(pos,element)
print("\nCode After Optimization")
for element in line:
    print(element)        