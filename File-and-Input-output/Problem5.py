with open("New_file.txt","r") as f:
     data = f.read()
     
     num=""
     for i in range(len(data)):
         if(data[i] == ","):
            print(num)
            num = ""
         else:
           num += data[i]