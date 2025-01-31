with open("practice.txt","r") as f:
     data = f.read()

newData =  data.replace("python","java")
print(newData)

with open("practice.txt","w") as f:
     f.write(newData)