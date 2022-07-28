#coding = utf-8

list1 = [10,5,7,38,11,2,4,3]

for s in range(len(list1)):
    for i in range(len(list1)- s - 1):
        j = i + 1
        if list1[i] > list1[j]:
            list1[i], list1[j] = list1[j], list1[i]
            print(list123)
# print(list1)
