# Two arrays are called similar if one can be obtained from another
# by swapping at most one pair of elements in one of the arrays.

# Given two arrays a and b, check whether they are similar.

def areSimilar(a, b):

    tmp1=list()
    tmp2=list()
    for i in range(len(a)):
        if a[i]!=b[i]:
            tmp1.append(a[i])
            tmp2.append(b[i])
    if len(tmp1)==0:
        return True
    elif len(tmp1)>2:
        return False
    else:
        return tmp1==list(reversed(tmp2))