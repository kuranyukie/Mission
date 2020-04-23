# -*- coding: UTF-8 -*-
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        d = {}
        def my(root, depth):
            if depth not in d: d[depth] = root.val
            if root.right is not None: my(root.right, depth + 1)
            if root.left  is not None: my(root.left , depth + 1)
        if root is None: return []
        my(root, 1)
        return [*d.values()]