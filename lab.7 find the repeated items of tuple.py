my_tuple = (1,2,3,4,5,6,5,3,6,9,4,2,9)
repeated = [item for item in set(my_tuple) if my_tuple.count(item) > 1]
print(repeated)
