# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return 'N'
        res = []
        temp = deque([root])
        while temp:
            el = temp.popleft()
            if not el:
                res.append('N')
            else:
                res.append(str(el.val))
                temp.append(el.left)
                temp.append(el.right)
        print(','.join(res))
        return ','.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == 'N':
            return 
        li = data.split(',')
        dummy = TreeNode(li[0])
        start = dummy
        temp = deque([dummy])
        i = 1
        while temp:
            el = temp.popleft()
            if li[i] != 'N':
                el.left = TreeNode(li[i])
                temp.append(el.left)
            if li[i+1] != 'N':
                el.right = TreeNode(li[i+1])
                temp.append(el.right)
            i += 2

        return start