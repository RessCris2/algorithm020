
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree( preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    def buildNode(preorder, inorder):
        """
         按照这个设定，它最后会返回一个Node， 有根，有left， right 节点。
        """
        if len(preorder)==0:
            return None
            
        root = TreeNode(preorder[0])

        # print(root)
        if  len(preorder)==1  or len(inorder)==1:
            return root
        
        in_ind = inorder.index(preorder[0])
        #if in_ind >= 1:
        #     pre_ind = preorder.index(inorder[in_ind-1])
        # else:
        #     pre_ind = 0
        print(in_ind)
        
        if in_ind == len(inorder)-1:
            pre_ind = len(inorder)
        else:
            pre_ind = preorder.index(inorder[in_ind+1])

        
        preorder_left = preorder[1: pre_ind]
        #print(preorder[1:2])
        print("preorder_left",preorder_left)
        
        inorder_left  = inorder[:in_ind]
        print(inorder_left)

        root.left = buildNode(preorder_left, inorder_left)

        preorder_right = preorder[pre_ind:]
        inorder_right  = inorder[in_ind+1 : ]
        print(preorder_right, inorder_right)

        root.right = buildNode(preorder_right, inorder_right)
            
        return root
    
    return buildNode(preorder, inorder)