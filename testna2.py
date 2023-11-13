def maxSlidingWindow(nums, k):
    """testna koda moja verzija"""
    if k==0:
        return nums
    if len(nums)<k:
        return []
    resitev=[]
    for i in range(len(nums)-k+1):
        sez=[]
        for j in range(k):  
            sez.append(nums[i+j])
        resitev.append(max(sez))
    return resitev

#print(maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))