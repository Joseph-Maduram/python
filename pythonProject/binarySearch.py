def binary_search(li, num):
    i=0
    j=len(li)-1
    while i<=j:
        midpoint=(i+j)//2
        if li[midpoint]<num:
            i=midpoint+1
        elif li[midpoint]>num:
            j=midpoint-1
        if li[midpoint]==num:
            print("able to get the midpoint and match",li[midpoint])
            return midpoint
    else:
        print("num is not present in the list")

li=[20,22,30,40,50,65,90]
num=100
mid_index=binary_search(li, num)
print("midindex is -{} for num-{} is".format(mid_index,num))