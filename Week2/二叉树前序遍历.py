 # 前序遍历
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def preorder(root):
            if not root:
                return
           
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        res = []
        preorder(root)

        return res

