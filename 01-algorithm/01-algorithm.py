def zero_sort(li):
    for j in range(0,len(li)-1):
        swap_count = 0
        for i in range(0,len(li)-1): 
            if zero_check(i,li):
                swap(i,i+1,li)
                swap_count += 1
            pass
        if swap_count == 0:
            return(li)
    return(li)

def zero_check(e1, li):
    if li[e1] == 0:
        return True
    return False

def swap(e1, e2, li):
    temp = li[e1]
    li[e1] = li[e2]
    li[e2] = temp
    return li

print(zero_sort([0,0,0,0,1,4,5,0,6,7,8]))