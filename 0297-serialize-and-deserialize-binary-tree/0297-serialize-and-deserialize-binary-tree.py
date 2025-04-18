# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        encode = []

        def bfs(root):
            q = deque([root])

            while q:
                node = q.popleft()
                if node is None:
                    encode.append("null")
                else:
                    encode.append(str(node.val))
                    q.append(node.left)
                    q.append(node.right)

        bfs(root)
        return ",".join(encode)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data is None or len(data) == 0:
            return None

        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        q = deque([root])

        i = 1
        while q:
            node = q.popleft()

            if nodes[i] != "null":
                left_node = TreeNode(int(nodes[i]))
                node.left = left_node
                q.append(left_node)

            i += 1

            if i < len(nodes) and nodes[i] != "null":
                right_node = TreeNode(int(nodes[i]))
                node.right = right_node
                q.append(right_node)
            i += 1
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
