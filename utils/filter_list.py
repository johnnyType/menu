def filter_list(l,mask):
    res = []
    for i in range(len(l)):
        if mask[i]==1:
            res.append(l[i])
    return res
