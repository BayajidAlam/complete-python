list = (1,3,4,6,4,6,7,9,10,11,12,30)

def print_all_elements(list,idx):
    if (idx == len(list)):
        return
    print(list[idx])
    print_all_elements(list,idx+1)

print_all_elements(list,0)