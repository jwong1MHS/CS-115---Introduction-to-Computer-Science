#
# A. Nicolosi
#
# 9/9/19
#
# Demonstrate recursion through the factorial and list length


def myFactorial(x):
    '''return the factorial of x (assumes x to be a Natural number'''
#    if x == 0:
#        return 1
#
#    else:
#        return x * myFactorial(x - 1)
    return 1 if x == 0 else x * myFactorial(x - 1)
#    return 1 if not x else x * myFactorial(x - 1)
#    return x * myFactorial(x - 1) if not x == 0 else 1


def myLength(L):
    '''return the length of a L (assumed to be a list)'''
#    if L == []
#        return 0
#    else:
#        return 1 + myLength(L[1:])

#    return 0 if L == [] else 1 + myLength(L[1:])
    return 0 if not L else 1 + myLength(L[1:])

def LCS(S1, S2): #longest common subsequence
    if 0==len(S1) or 0==len(S2):
        return 0
    elif S1[0] == S2[0]:
	# A common first chatacter adds 1 to the LCS
        return 1 + LCS(S1[1:], S2[1:])
    else:
        #Drop either first character and recurse
        return max(LCS(S1[1:], S2[1:]))
#AGTAC
#ATTCG
#AGTCCGC
#GTCAGC
    


#    if not S1 or not S2
#        return 0
#    else:
#        head1, tail1 = S1[0], S1[1:]
#        head2, tail2 = S2[0], S2[1:]


#    if head1 == head2:
#        return 1 + LCS(tail1, tail2)
#    else:
#        reutrn max(LCS(tail1, tail2))

