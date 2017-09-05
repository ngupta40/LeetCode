class Solution(object):
    def mergeTrees(self, t1, t2):
        return mtree(t1, t2)


def mtree(t1, t2):
    if (t1 == None):
        return t2
    if (t2 == None):
        return t1

    t1.val = t1.val + t2.val
    t1.left = mtree(t1.left, t2.left)
    t1.right = mtree(t1.right, t2.right)

    return t1
