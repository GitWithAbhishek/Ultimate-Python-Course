import os

if(not os.path.exists("Day 23/data")):
    os.mkdir("Day 23/Lec 46/data")

for i in range (0,100):
    os.mkdir(f"Day 23/Lec 46/data/Day {i+1}")