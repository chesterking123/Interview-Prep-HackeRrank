def twoStrings(s1, s2):
    if(len(s1)>100 or len(s2)>100):
        s1=sorted(s1[0:100])
        s2=sorted(s2[0:100])

    for i in range(len(s1)):
        for j in range(len(s2)):
            if(s1[i]==s2[j]):
                Result = 'YES'
                return Result
    Result='NO'
    return Result
