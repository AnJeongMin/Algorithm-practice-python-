import random
f = open("input.txt", "w")

f.write("1000\n")

for i in range(10000):
    rand = random.randrange(1, 10000)
    f.write(str(rand)+"\n")
    
