def print_Down_Stream(num):
    if num == 0:
        return
    print(num)
    print_Down_Stream(num - 1)

num = int(input("Enter a number: "))
print_Down_Stream(num)