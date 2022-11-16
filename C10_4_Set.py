set1 = {"apple", "banana","cherry"}
print(set1)
list1 = [0,1,2,3]
set2 = set(list1)
list1[1]=0
print(list1)
print(set2)
#Sets are like lists but are unodered, undchangeable and unindexed. 
# Also no dublicates allowed
print(set1|set2)
print(set1-set2)
print(set1&set2)
print(set1^set2)