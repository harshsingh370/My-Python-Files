set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}
items = set1 & set2
set1.update(set2 - items)
print("Updated set1 (excluding common items from set2):",set1)
