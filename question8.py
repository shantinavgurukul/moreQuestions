def same_duplicate():
    list1 = [1, 5, 10, 12, 16, 20]
    list2 = [1, 2, 10, 13, 16]
    i=0
    a=[]
    while(i<len(list1)):
        if list1[i] not in list2:
            list2.append(list1[i])
        i=i+1
    return(list2)
print(same_duplicate())