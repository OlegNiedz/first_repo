def transform_list(list_in):
    list_odd = [x for x in list_in if x%2!=0]
    list_odd.sort()
    j=0
    for i,x in enumerate(list_in):
        if x%2!=0:
            list_in[i] = list_odd[j]
            j+=1
    return list_in
print(transform_list([9,7,8,6,7,5,3,4,10,2,1,10]))