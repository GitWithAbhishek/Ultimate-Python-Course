f = open('Day 25/test.txt','r')
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    m1 = int(line.split(" ")[0])
    m2 = int(line.split(" ")[1])
    m3 = int(line.split(" ")[2])
    print(f"Marks of Student {i} in maths is {m1*2}")
    print(f"Marks of Student {i} in Science is {m2*2}")
    print(f"Marks of Student {i} in sst is {m3*2}")