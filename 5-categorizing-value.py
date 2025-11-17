## Pembuktian bahwa composite data type bisa menyimpan banyak tipe data sekaligus
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
print(type(myMixedTypeList))
print(type(myMixedTypeList[0])) # 45
print(type(myMixedTypeList[0])) # 1.02  
print(type(myMixedTypeList[0])) # True
print(type(myMixedTypeList[0])) # My dog is on the bed.
print(type(myMixedTypeList[0])) # 290578
print(type(myMixedTypeList[0])) # "45"

print("--------------------------------------------------------------------------------------")
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))
    
print("--------------------------------------------------------------------------------------")
for item in myMixedTypeList:
    print(type(item))