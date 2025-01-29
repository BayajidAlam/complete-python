collection = set()
collection.add(1)
collection.add(2)
collection.add(3)

print(collection)

collection.remove(2)
print(collection)

collection.discard(3)
print(collection)

collection.clear()
print(collection)


#Set union and intersection
set1 = {1,2,3}
set2 = {3,4,5}

union_set = set1.union(set2)
print(union_set)

intersection_set = set1.intersection(set2)
print(intersection_set)