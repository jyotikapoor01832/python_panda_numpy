def checkDuplicates(list1):
    flag=0
    list2=[]
    for elem in list1:
        counter = list1.count(elem)
        if counter>1 and elem not in list2:
            list2.append(elem)
    print("Duplicate value is :",list2)
list1=[1,2,3,4,5,4]
checkDuplicates(list1)