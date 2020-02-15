import os

counter = 0

for d in  os.listdir("annotations"):
    
    f = open(f"{os.getcwd()}/annotations/{d}").read()
    counter += f.count("mFalcon")

print(counter)
