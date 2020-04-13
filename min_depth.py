class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None: 
            return 0
        
        if root.left==None and root.right==None: 
            return 1
        
        if root.left==None:
            return self.minDepth(root.right)+1
        
        if root.right==None:
            return self.minDepth(root.left)+1
        
        return min(self.minDepth(root.left)+1,self.minDepth(root.right)+1)


