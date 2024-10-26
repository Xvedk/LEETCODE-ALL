# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        depth_map = defaultdict(lambda :(-1, -1, 0))
        level_map = {}
        def travel(root, level):
            if not root:
                return 0
            depth = max(travel(root.left, level + 1), travel(root.right, level + 1))
            level_map[root.val] = (level, depth)
            max_, second_max, size = depth_map[level]
            if depth >= max_:
                depth_map[level] = (depth, max_, size + 1)
            elif depth > second_max:
                depth_map[level] = (max_, depth, size + 1)
            else:
                depth_map[level] = (max_, second_max, size + 1)
            return depth + 1
        travel(root, 0)
        result = []
        for q in queries:
            level, depth = level_map[q]
            max_, second_max, size = depth_map[level]
            if size == 1:
                result.append(level - 1)
                continue
            if depth == max_:
                result.append(level + second_max)
            else:
                result.append(level + max_) 
        return result
