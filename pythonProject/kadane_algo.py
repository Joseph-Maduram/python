#
def kadane_algo(li):
    curr_sum=0
    startingpoint=0
    res=0
    for i in range(len(li)):
        curr_sum=curr_sum+li[i]
        # print(curr_sum)
        if curr_sum<0:
            curr_sum=0
            startingpoint=i+1
        if curr_sum> res:
            s=startingpoint
            e=i
        res=max(res,curr_sum)
    print(li[s:e+1])
    return res

li=[-2,-3,4,-1,-2,1,5,-3]
# print(len(li))
res=kadane_algo(li)
print(res)

