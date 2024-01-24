class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # Checks whether we can make a palindrome from this dictionary or not.
        # It should have at most 1 odd count number and as many even count numbers
        # as it wants.
        def checkDictionary(curDict):
            oddCount = 0
            for _, v in curDict.items():
                 oddCount += (v % 2)
                 if oddCount > 1:
                     return 0
            return 1
        
        def dfs(root, curDict):
            if not root:
                return 0
            # Add the value of this node to the dictionary
            curDict.setdefault(root.val, 0)
            curDict[root.val] += 1

            # It is a leaf node. So, check the dictionary and then
            # remove the value it was contributing to the current path.
            if not root.left and not root.right:
                c = checkDictionary(curDict)
                curDict[root.val] -= 1
                return c
            
            # Check how many palindromic pseudopaths children have
            val = dfs(root.left, curDict) + dfs(root.right, curDict)
            # remove the value it was contributing to the current path.
            curDict[root.val] -= 1
            return val
        return dfs(root, {})
