def num_to_binary_list(num):
    l = []
    while num>0:
        l.append(num%2)
        num//=2
    while len(l)<12:
        l.append(0)
    return l