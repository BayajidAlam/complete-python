try:
    with open("demo.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("Error: demo.txt file not found")
except IOError:
    print("Error: Unable to read the file")