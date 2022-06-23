class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Three orders of DFS -> stack-based (recursive is just stack based since recursive calls are scheduled in a stack)
pre = []
def pre_order_traversal(node):
    if (node):
        pre.append(node.val)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

in_order = []
def in_order_traversal(node):
    if (node):
        in_order_traversal(node.left)
        in_order.append(node.val)
        in_order_traversal(node.right)

post_order = []
def post_order_traversal(node):
    if (node):
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        post_order.append(node.val)

# Iterative DFS - stack-based pre-order traversal
def iterative_dfs(root):
    if (not root):
        return

    dfs = []
    stack = [root]
    while (len(stack) > 0):
        top = stack.pop()
        dfs.append(top.val)
        if (top.right):
            stack.append(top.right)
        if (top.left):
            stack.append(top.left)
    print(dfs)

# Iterative BFS - Queue based pre-order traversal
def levelOrder(root):
    if (not root):
        return

    queue = [root]
    levels = []
    while (len(queue) > 0):
        sz = len(queue)
        level = []
        for i in range(sz):
            top = queue.pop(0)
            level.append(top.val)
            if (top.left):
                queue.append(top.left)
            if (top.right):
                queue.append(top.right)
        levels.append(level)
    return levels


def isSymmetric(root):
    if not root:
        return True
    def isSymmetricHelper(left, right):
        if (not left and not right):
            return True
        elif (not left or not right):
            return False
        else:
            if (left.val != right.val):
                return False
            return isSymmetricHelper(left.left, right.right) and isSymmetricHelper(left.right, right.left)
    return isSymmetricHelper(root.left, root.right)


# def maxDepth(root):
#     if (not root):
#         return 0
#     return 1 + max(maxDepth(root.left), maxDepth(root.right))

maxVal = 0
def maxDepthHelper(root, depth):
    global maxVal
    if (root):
        maxVal = max(maxVal, depth)
        maxDepthHelper(root.left, depth + 1)
        maxDepthHelper(root.right, depth + 1)

def maxDepth(root):
    maxDepthHelper(root, 1)

if __name__ == "__main__":
    node = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
    # node = TreeNode(1, None, TreeNode(2))
    pre_order_traversal(node)
    print(pre)
    iterative_dfs(node)
    iterative_bfs(node)
    # in_order_traversal(node)
    # post_order_traversal(node)
    # print(pre)
    # print(in_order)
    # print(post_order)
    # print(isSymmetric(node))
    # maxDepth(node)
    # print(maxVal)
